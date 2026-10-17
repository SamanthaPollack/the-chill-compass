// The Chill Compass: "Today on board" links for each Margaritaville at Sea ship.
// Reads the cruise line's public Gateway page for the ship (e.g. /paradise-gateway) and returns
// the current Cruise News & Schedule PDF plus the other onboard PDFs (kids club, excursions, spa, map).
// We only LINK to the cruise line's files; nothing is copied or re-hosted.
//   /.netlify/functions/onboard?ship=paradise   -> { ship, schedule, items, checked }

const SHIPS = { paradise: 'paradise-gateway', islander: 'islander-gateway', beachcomber: 'beachcomber-gateway' };
const BASE = 'https://www.margaritavilleatsea.com/';
const TTL = 10 * 60 * 1000;
const cache = {};

const clean = s => String(s || '').replace(/<[^>]+>/g, ' ').replace(/&amp;/g, '&').replace(/&#39;|&rsquo;/g, "'")
  .replace(/&quot;/g, '"').replace(/&nbsp;/g, ' ').replace(/\s+/g, ' ').trim();

function kindOf(title, file) {
  const s = (title + ' ' + file).toLowerCase();
  if (/cruise news|schedule|^day \d/.test(s) && !/kid/.test(s)) return 'schedule';
  if (/kid/.test(s)) return 'kids';
  if (/excursion|shrx/.test(s)) return 'excursions';
  if (/spa/.test(s)) return 'spa';
  if (/map|deck/.test(s)) return 'map';
  if (/dining|menu/.test(s)) return 'dining';
  return 'other';
}

async function load(ship) {
  const hit = cache[ship];
  if (hit && Date.now() - hit.at < TTL) return hit.data;
  const res = await fetch(BASE + SHIPS[ship], { headers: { 'User-Agent': 'Mozilla/5.0 (compatible; TheChillCompass/1.0; +https://thechillcompass.com)' } });
  if (!res.ok) throw new Error('gateway ' + res.status);
  const html = await res.text();
  const groups = new Map();
  for (const m of html.matchAll(/<a\b[^>]*href="([^"]+?\.pdf)(?:\?[^"]*)?"[^>]*>([\s\S]{0,400}?)<\/a>/gi)) {
    let url = m[1].replace(/&amp;/g, '&');
    if (!/^https:\/\//i.test(url)) continue;
    const u = new URL(url);
    if (!/(^|\.)cloudfront\.net$|(^|\.)margaritavilleatsea\.com$/i.test(u.hostname)) continue;
    url = u.origin + u.pathname;
    const txt = clean(m[2]);
    if (!txt) continue;
    if (!groups.has(url)) groups.set(url, []);
    const g = groups.get(url); if (!g.includes(txt)) g.push(txt);
  }
  const items = [...groups.entries()].map(([url, t]) => {
    const file = url.split('/').pop();
    return { kind: kindOf(t[0] || '', file), title: t[0] || file, detail: t[1] || '', url };
  });
  const scheduleItem = items.find(i => i.kind === 'schedule') || null;
  const data = {
    ship,
    schedule: scheduleItem ? { label: scheduleItem.detail || scheduleItem.title, url: scheduleItem.url } : null,
    items: items.filter(i => i !== scheduleItem),
    checked: new Date().toISOString(),
  };
  cache[ship] = { at: Date.now(), data };
  return data;
}

exports.handler = async (event) => {
  const ship = String((event.queryStringParameters || {}).ship || '').toLowerCase();
  const headers = { 'Content-Type': 'application/json; charset=utf-8', 'Access-Control-Allow-Origin': '*' };
  if (!SHIPS[ship]) return { statusCode: 400, headers, body: JSON.stringify({ error: 'unknown ship' }) };
  try {
    const data = await load(ship);
    return { statusCode: 200, headers: { ...headers, 'Cache-Control': 'public, max-age=300', 'Netlify-CDN-Cache-Control': 'public, s-maxage=600, stale-while-revalidate=3600' }, body: JSON.stringify(data) };
  } catch (e) {
    return { statusCode: 200, headers: { ...headers, 'Cache-Control': 'no-store' }, body: JSON.stringify({ ship, schedule: null, items: [], error: 'unavailable' }) };
  }
};
