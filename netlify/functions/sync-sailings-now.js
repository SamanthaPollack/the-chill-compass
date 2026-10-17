// Starts a sailing refresh on demand (for example after a big sale drops).
// Requires the private sync token in the X-Sync-Token header, so the public can't trigger it.
const { runSync } = require('../lib/sailings-sync');

exports.handler = async (event) => {
  const token = process.env.SAILINGS_SYNC_TOKEN;
  const given = (event.headers && (event.headers['x-sync-token'] || event.headers['X-Sync-Token'])) || '';
  if (event.httpMethod !== 'POST' || !token || given !== token) return { statusCode: 403, body: JSON.stringify({ error: 'not allowed' }) };
  try {
    return { statusCode: 200, headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(await runSync()) };
  } catch (e) {
    return { statusCode: 500, headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ error: e.message }) };
  }
};
