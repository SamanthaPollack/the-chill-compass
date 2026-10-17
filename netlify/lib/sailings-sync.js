// Pulls every upcoming Margaritaville at Sea sailing from CruiseFeed ONCE and saves it to Supabase.
// Visitors and Cruise Guides read the saved copy, so CruiseFeed credit is only used by this refresh
// (about 350 results each time). Runs monthly; can also be started by hand with the sync token.

const API_BASE = 'https://api.cruisefeed.io/v1';
const LINE = 'Margaritaville at Sea Cruises';
const LINE_MATCH = /margaritaville/i;
const SUPABASE_URL = 'https://wekrxtehnrzebkvksfzk.supabase.co';
const SUPABASE_KEY = 'sb_publishable_40y1c-dZeptAiD2YLtx9lQ_CAMMrKGb';
const PAGE = 24;
const MAX_PAGES = 30; // hard stop: never pull more than ~720 results in one refresh

const list = d => (d && (d.items || d.data || (Array.isArray(d) ? d : []))) || [];

async function pullAll(key) {
  const today = new Date().toISOString().slice(0, 10);
  const rows = [];
  for (let page = 0; page < MAX_PAGES; page++) {
    const url = new URL(API_BASE + '/cruises');
    url.searchParams.set('cruise_line', LINE);
    url.searchParams.set('departure_from', today);
    url.searchParams.set('sort', 'departure_date');
    url.searchParams.set('limit', String(PAGE));
    url.searchParams.set('offset', String(page * PAGE));
    const res = await fetch(url.toString(), { headers: { Authorization: 'Bearer ' + key } });
    if (!res.ok) throw new Error('CruiseFeed ' + res.status + ': ' + (await res.text()).slice(0, 200));
    const items = list(await res.json()).filter(c => LINE_MATCH.test(c.cruise_line || '') || LINE_MATCH.test(c.ship_name || ''));
    rows.push(...items);
    if (items.length < PAGE) break;
  }
  return rows;
}

async function save(rows, token) {
  const res = await fetch(SUPABASE_URL + '/rest/v1/rpc/sync_sailings', {
    method: 'POST',
    headers: { apikey: SUPABASE_KEY, Authorization: 'Bearer ' + SUPABASE_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ p_token: token, p_rows: rows }),
  });
  const text = await res.text();
  if (!res.ok) throw new Error('Supabase ' + res.status + ': ' + text.slice(0, 200));
  return Number(text) || 0;
}

async function runSync() {
  const key = process.env.CRUISEFEED_API_KEY, token = process.env.SAILINGS_SYNC_TOKEN;
  if (!key || !token) throw new Error('Missing CRUISEFEED_API_KEY or SAILINGS_SYNC_TOKEN');
  const rows = await pullAll(key);
  const saved = await save(rows, token);
  return { pulled: rows.length, saved, at: new Date().toISOString() };
}

module.exports = { runSync };
