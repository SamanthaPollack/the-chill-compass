// Scheduled monthly (see netlify.toml): refreshes the saved Margaritaville at Sea sailings.
const { runSync } = require('../lib/sailings-sync');

exports.handler = async () => {
  try {
    const r = await runSync();
    console.log('sailings sync', r);
    return { statusCode: 200, body: JSON.stringify(r) };
  } catch (e) {
    console.error('sailings sync failed', e.message);
    return { statusCode: 500, body: JSON.stringify({ error: e.message }) };
  }
};
