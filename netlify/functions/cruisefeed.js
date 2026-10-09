// The Chill Compass: server-side proxy for the CruiseFeed API (https://cruisefeed.io),
// LOCKED to Margaritaville at Sea. Keeps CRUISEFEED_API_KEY out of the browser.
//   /.netlify/functions/cruisefeed?resource=meta          -> { line, ships: [...] }
//   /.netlify/functions/cruisefeed?resource=cruises&...   -> Margaritaville at Sea sailings only

const API_BASE = 'https://api.cruisefeed.io/v1';
const LINE_MATCH = /margaritaville/i;
const ALLOWED = ['ship_name', 'embark_port', 'departure_from', 'departure_to',
  'min_nights', 'max_nights', 'has_price', 'sort', 'limit', 'offset', 'currency'];

let cache = { at: 0, line: null, ships: [] };

async function api(path, params, key) {
  const url = new URL(API_BASE + path);
  Object.entries(params || {}).forEach(([k, v]) => { if (v !== undefined && v !== null && v !== '') url.searchParams.set(k, v); });
  const res = await fetch(url.toString(), { headers: { Authorization: 'Bearer ' + key } });
  const text = await res.text();
  let data = null; try { data = JSON.parse(text); } catch (e) {}
  return { ok: res.ok, status: res.status, data, text };
}
const list = d => (d && (d.items || d.lines || d.data || (Array.isArray(d) ? d : []))) || [];
const nameOf = x => typeof x === 'string' ? x : (x && (x.name || x.cruise_line || x.line || x.ship_name)) || '';

async function meta(key) {
  if (cache.line && Date.now() - cache.at < 6 * 3600 * 1000) return cache;
  const lines = await api('/cruise-lines', {}, key);
  const line = list(lines.data).map(nameOf).find(n => LINE_MATCH.test(n)) || 'Margaritaville at Sea';
  let ships = [];
  try {
    const s = await api('/ships', { operator: line, limit: 50 }, key);
    ships = Array.from(new Set(list(s.data).map(nameOf).filter(Boolean))).sort();
  } catch (e) {}
  cache = { at: Date.now(), line, ships };
  return cache;
}

const json = (code, body) => ({ statusCode: code, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'public, max-age=900' }, body: typeof body === 'string' ? body : JSON.stringify(body) });

exports.handler = async function (event) {
  const key = process.env.CRUISEFEED_API_KEY;
  if (!key) return json(500, { error: 'Sailing search is not configured yet.' });
  const qs = event.queryStringParameters || {};
  try {
    const m = await meta(key);
    if (qs.resource === 'meta') return json(200, { line: m.line, ships: m.ships });
    const params = { cruise_line: m.line };
    ALLOWED.forEach(k => { if (qs[k] !== undefined && qs[k] !== '') params[k] = qs[k]; });
    let limit = parseInt(qs.limit, 10); if (!limit || limit < 1 || limit > 24) limit = 12; params.limit = limit;
    const r = await api('/cruises', params, key);
    if (!r.ok) return json(r.status, r.text);
    // Belt and braces: drop anything that isn't Margaritaville at Sea.
    const d = r.data || {};
    const items = list(d).filter(c => LINE_MATCH.test(c.cruise_line || '') || LINE_MATCH.test(c.ship_name || ''));
    return json(200, { items, total: typeof d.total === 'number' ? d.total : null });
  } catch (e) {
    return json(502, { error: 'Could not load sailings right now.' });
  }
};
