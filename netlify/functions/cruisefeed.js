// The Chill Compass: sailing search for the Sailings page, sailing details and the quote form.
// Reads the SAVED copy of Margaritaville at Sea sailings in Supabase (refreshed monthly by
// sync-sailings), so visitors never use CruiseFeed credit.
//   /.netlify/functions/cruisefeed?resource=meta          -> { line, ships: [...] }
//   /.netlify/functions/cruisefeed?ship_name=&departure_from=&departure_to=&min_nights=&max_nights=
//        &embark_port=&has_price=true&sort=departure_date|price&limit=&offset=   -> { items, total }

const SUPABASE_URL = 'https://wekrxtehnrzebkvksfzk.supabase.co';
const SUPABASE_KEY = 'sb_publishable_40y1c-dZeptAiD2YLtx9lQ_CAMMrKGb';
const LINE = 'Margaritaville at Sea Cruises';
const SHIPS = ['Margaritaville at Sea Paradise', 'Margaritaville at Sea Islander', 'Margaritaville at Sea Beachcomber'];
const DATE = /^\d{4}-\d{2}-\d{2}$/;

const json = (code, body) => ({ statusCode: code, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'public, max-age=600' }, body: JSON.stringify(body) });

exports.handler = async function (event) {
  const qs = event.queryStringParameters || {};
  if (qs.resource === 'meta') return json(200, { line: LINE, ships: SHIPS });

  const today = new Date().toISOString().slice(0, 10);
  const u = new URL(SUPABASE_URL + '/rest/v1/sailings');
  u.searchParams.set('select', 'data');
  const from = DATE.test(qs.departure_from || '') ? qs.departure_from : today;
  u.searchParams.append('departure_date', 'gte.' + (from < today && !qs.departure_to ? today : from));
  if (DATE.test(qs.departure_to || '')) u.searchParams.append('departure_date', 'lte.' + qs.departure_to);
  if (qs.ship_name) u.searchParams.set('ship_name', 'eq.' + String(qs.ship_name).slice(0, 80));
  if (qs.embark_port) u.searchParams.set('embark_port', 'eq.' + String(qs.embark_port).slice(0, 80));
  const minN = parseInt(qs.min_nights, 10), maxN = parseInt(qs.max_nights, 10);
  if (minN > 0) u.searchParams.append('nights', 'gte.' + minN);
  if (maxN > 0) u.searchParams.append('nights', 'lte.' + maxN);
  if (qs.has_price === 'true') u.searchParams.set('price_amount', 'not.is.null');
  u.searchParams.set('order', qs.sort === 'price' ? 'price_amount.asc.nullslast,departure_date.asc' : 'departure_date.asc,ship_name.asc');
  let limit = parseInt(qs.limit, 10); if (!limit || limit < 1 || limit > 24) limit = 12;
  const offset = Math.max(0, parseInt(qs.offset, 10) || 0);
  u.searchParams.set('limit', String(limit));
  u.searchParams.set('offset', String(offset));

  try {
    const res = await fetch(u.toString(), { headers: { apikey: SUPABASE_KEY, Authorization: 'Bearer ' + SUPABASE_KEY, Prefer: 'count=exact' } });
    if (!res.ok) return json(502, { error: 'Could not load sailings right now.' });
    const rows = await res.json();
    const range = res.headers.get('content-range') || '';
    const total = parseInt(range.split('/')[1], 10);
    return json(200, { items: rows.map(r => r.data), total: isNaN(total) ? null : total });
  } catch (e) {
    return json(502, { error: 'Could not load sailings right now.' });
  }
};
