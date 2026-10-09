// The Chill Compass – shared site script (v5)
const SUPABASE_URL = 'https://wekrxtehnrzebkvksfzk.supabase.co';
const SUPABASE_KEY = 'sb_publishable_40y1c-dZeptAiD2YLtx9lQ_CAMMrKGb';
const sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);

const CATS = {
  'Cruise Reviews': { slug: 'cruise-reviews', emoji: '⭐', color: '#0B7F8A', grad: 'linear-gradient(135deg,#14B8C4,#0B7F8A)' },
  'Port Guides':    { slug: 'port-guides',    emoji: '🌴', color: '#FF6B5B', grad: 'linear-gradient(135deg,#FF8A5B,#FFC93C)' },
  'Deals':          { slug: 'deals',          emoji: '💸', color: '#b07d00', grad: 'linear-gradient(135deg,#FFC93C,#FF6B5B)' },
  'Tips & News':    { slug: 'tips',           emoji: '🧭', color: '#0B3954', grad: 'linear-gradient(135deg,#0B3954,#14B8C4)' },
};
const catBySlug = s => Object.keys(CATS).find(k => CATS[k].slug === s);

const SHIPS = {
  Paradise:    { slug: 'paradise',    port: 'Palm Beach, FL',          accent: '#FF6B5B', emoji: '🌺' },
  Islander:    { slug: 'islander',    port: 'Tampa, FL',               accent: '#14B8C4', emoji: '🏝️' },
  Beachcomber: { slug: 'beachcomber', port: 'Miami, FL · Galveston, TX', accent: '#0B3954', emoji: '🐚' },
};
const shipBySlug = s => Object.keys(SHIPS).find(k => SHIPS[k].slug === s);

function esc(s) { return String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])); }
function fmtDate(d) { return d ? new Date(d).toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' }) : ''; }
function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
function slugify(s) { return String(s).toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/&/g, ' and ').replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 90); }
// "2027-01-09" -> local date without timezone shift
function dateOnly(s) { const [y, m, d] = String(s).split('-').map(Number); return new Date(y, m - 1, d); }
function timeAgo(d) {
  const s = (Date.now() - new Date(d)) / 1000;
  if (s < 60) return 'just now'; if (s < 3600) return Math.floor(s / 60) + 'm ago';
  if (s < 86400) return Math.floor(s / 3600) + 'h ago'; if (s < 604800) return Math.floor(s / 86400) + 'd ago';
  return fmtDate(d);
}
function avatar(name, size) {
  const n = String(name || '?').trim(); let h = 0; for (const c of n) h = (h * 31 + c.charCodeAt(0)) % 360;
  const st = size ? `width:${size}px;height:${size}px;font-size:${Math.round(size * .42)}px;` : '';
  return `<span class="avatar" style="${st}background:hsl(${h} 62% 46%)">${esc(n[0].toUpperCase())}</span>`;
}

/* ---------- post cards ---------- */
function postRow(p) {
  const c = CATS[p.category] || CATS['Cruise Reviews'];
  const bg = p.cover_url ? `background-image:url('${esc(p.cover_url)}')` : `background:${c.grad}`;
  return `<a class="row" href="/post/${encodeURIComponent(p.slug)}">
    <div class="img" style="${bg}"><span class="tag" style="color:${c.color}">${esc(p.category)}</span>${p.cover_url ? '' : c.emoji}</div>
    <div class="body"><div class="meta">${fmtDate(p.published_at)}</div><h3>${esc(p.title)}</h3><p>${esc(p.excerpt || '')}</p></div>
  </a>`;
}
const postCard = postRow;
function leadCard(p) {
  const c = CATS[p.category] || CATS['Cruise Reviews'];
  const bg = p.cover_url ? `background-image:url('${esc(p.cover_url)}')` : `background:${c.grad}`;
  return `<a class="lead" href="/post/${encodeURIComponent(p.slug)}">
    <div class="img" style="${bg}"><span class="tag" style="color:${c.color}">${esc(p.category)}</span>${p.cover_url ? '' : c.emoji}</div>
    <div class="txt"><div class="eyebrow">✨ Newest post · ${fmtDate(p.published_at)}</div><h2>${esc(p.title)}</h2><p>${esc(p.excerpt || '')}</p><span class="btn btn-coral">Read the Post →</span></div>
  </a>`;
}
const featuredCard = leadCard;

async function fetchPosts({ limit = 24, category = null, excludeId = null } = {}) {
  let q = sb.from('posts').select('id,slug,title,excerpt,category,cover_url,published_at')
    .eq('published', true).order('published_at', { ascending: false }).limit(limit);
  if (category) q = q.eq('category', category);
  if (excludeId) q = q.neq('id', excludeId);
  const { data, error } = await q;
  if (error) { console.error(error); return []; }
  return data;
}
function emptyBox(msg, sub) {
  return `<div class="empty"><div class="e">🏝️</div><h3>${msg}</h3><p>${sub || 'Grab your free guides and we\'ll let you know when new posts drop!'}</p></div>`;
}

/* ---------- roll call rows ---------- */
function rcRow(r) {
  const d = dateOnly(r.sail_date), s = SHIPS[r.ship] || {};
  return `<a class="rc" href="/rollcall/${r.id}">
    <div class="date-badge"><span>${d.toLocaleDateString('en-US', { month: 'short' })}</span><b>${d.getDate()}</b><span>${d.getFullYear()}</span></div>
    <div><h3><span class="dot d-${s.slug}"></span>${esc(r.ship)} · ${d.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' })}</h3>
      <div class="sub">${esc(r.itinerary || s.port || '')}</div></div>
    <div class="counts"><b>${r.member_count}</b> sailing · <b>${r.post_count}</b> posts<br>${r.last_post_at ? 'last post ' + timeAgo(r.last_post_at) : 'be the first to post!'}</div>
  </a>`;
}

/* ---------- stateroom illustration (used until a real photo is uploaded) ---------- */
function roomArt(tier, accent) {
  const a = accent || '#14B8C4';
  // sea scene drawn with absolute coordinates inside a clipped box
  let cid = 0;
  const sea = (x, y, w, h, r = 0) => { const id = 'c' + (++cid) + Math.random().toString(36).slice(2, 6), hz = y + h * .55;
    let waves = ''; for (let k = 0; k < 2; k++) { const yy = hz + 14 + k * 22; let d = `M${x} ${yy}`; for (let xx = x; xx < x + w; xx += 30) d += ` q7.5 -6 15 0 t15 0`; waves += `<path d="${d}" stroke="#fff" stroke-opacity="${.55 - k * .2}" fill="none" stroke-width="3"/>`; }
    return `<clipPath id="${id}"><rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}"/></clipPath><g clip-path="url(#${id})"><rect x="${x}" y="${y}" width="${w}" height="${h}" fill="url(#sky)"/><circle cx="${x + w * .7}" cy="${y + h * .38}" r="${Math.min(w, h) * .12}" fill="#FFC93C"/><rect x="${x}" y="${hz}" width="${w}" height="${h}" fill="#14B8C4"/>${waves}</g>`; };
  const defs = `<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB8A0"/><stop offset="1" stop-color="#FFE7A3"/></linearGradient><linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF8EC"/><stop offset="1" stop-color="#F6E6C8"/></linearGradient></defs>`;
  let win = '';
  if (tier === 'Ocean View') win = `<rect x="330" y="70" width="240" height="150" rx="75" fill="#0B3954"/>${sea(342, 82, 216, 126, 63)}`;
  if (tier === 'Balcony' || tier === 'Suite') { const wx = tier === 'Suite' ? 500 : 340;
    win = `<rect x="${wx}" y="50" width="250" height="292" fill="#0B3954"/>${sea(wx + 8, 58, 234, 284)}<rect x="${wx + 121}" y="50" width="8" height="292" fill="#0B3954"/><rect x="${wx + 8}" y="240" width="234" height="7" fill="#fff" opacity=".9"/>` +
      [30, 60, 90, 160, 190, 220].map(xx => `<rect x="${wx + xx}" y="247" width="3" height="95" fill="#fff" opacity=".8"/>`).join(''); }
  if (tier === 'Interior') win = `<rect x="350" y="80" width="150" height="104" rx="8" fill="#fff" stroke="${a}" stroke-width="6"/><path d="M362 172 l38 -44 l26 26 l22 -22 l38 40z" fill="${a}" opacity=".7"/><circle cx="470" cy="108" r="11" fill="#FFC93C"/><circle cx="125" cy="170" r="22" fill="#FFC93C" opacity=".85"/><rect x="121" y="190" width="8" height="45" fill="#c9b48e"/>`;
  const bedX = tier === 'Suite' ? 60 : tier === 'Interior' ? 160 : 70;
  const sofa = tier === 'Suite' ? `<rect x="345" y="290" width="130" height="50" rx="14" fill="${a}"/><rect x="337" y="272" width="146" height="28" rx="12" fill="${a}" opacity=".8"/><text x="420" y="250" font-size="40" text-anchor="middle">🌴</text>` : '';
  return `<svg viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" role="img" aria-label="${esc(tier)} stateroom illustration">${defs}
    <rect width="800" height="450" fill="url(#wall)"/><rect y="340" width="800" height="110" fill="#E8D3AE"/><rect y="336" width="800" height="6" fill="#d8bf93"/>
    ${win}
    <g transform="translate(${bedX},0)"><rect x="0" y="235" width="250" height="20" rx="8" fill="#0B3954"/><rect x="0" y="180" width="20" height="160" rx="6" fill="#0B3954"/>
    <rect x="18" y="250" width="232" height="80" rx="14" fill="#fff"/><rect x="18" y="290" width="232" height="40" rx="10" fill="${a}"/><rect x="150" y="285" width="100" height="45" rx="10" fill="${a}" opacity=".7"/>
    <rect x="30" y="228" width="70" height="34" rx="14" fill="#fff" stroke="#e7dccb" stroke-width="3"/><rect x="105" y="228" width="70" height="34" rx="14" fill="#fff" stroke="#e7dccb" stroke-width="3"/>
    <rect x="0" y="330" width="250" height="14" rx="6" fill="#0B3954"/><text x="125" y="318" font-size="26" text-anchor="middle">🦩</text></g>
    ${sofa}</svg>`;
}

/* ---------- member accounts (Roll Calls) ---------- */
const USERNAME_RE = /^[A-Za-z0-9._]{3,20}$/;
let ME = null; // { id, email, display_name, banned }
async function loadMe() {
  const { data: { session } } = await sb.auth.getSession();
  if (!session) { ME = null; return null; }
  const { data } = await sb.from('profiles').select('display_name,hometown,banned').eq('id', session.user.id).maybeSingle();
  ME = { id: session.user.id, email: session.user.email, ...(data || { display_name: session.user.email.split('@')[0] }) };
  try { const { data: md } = await sb.from('member_details').select('first_name,last_name').eq('id', session.user.id).maybeSingle();
    const um = session.user.user_metadata || {};
    ME.first_name = md?.first_name ?? um.first_name ?? ''; ME.last_name = md?.last_name ?? um.last_name ?? ''; } catch (e) {}
  try { const { data: adm } = await sb.rpc('is_admin'); ME.is_admin = !!adm; } catch (e) { ME.is_admin = false; }
  return ME;
}
function renderTopbarUser() {
  const el = document.getElementById('tbUser'); if (!el) return;
  el.innerHTML = ME ? (ME.is_admin ? `<a class="me" href="/admin/" title="Open your admin dashboard">⛱️ ${esc(ME.display_name)} · Dashboard</a>` : `<span class="me">⛱️ ${esc(ME.display_name)}</span>`) + `<button id="tbOut">Sign out</button>`
    : `<button data-auth="in">Sign in</button><button data-auth="up" style="color:var(--sun);font-weight:700">Join the crew</button>`;
  const out = document.getElementById('tbOut'); if (out) out.onclick = async () => { await sb.auth.signOut(); location.reload(); };
  el.querySelectorAll('[data-auth]').forEach(b => b.onclick = () => openAuth(b.dataset.auth));
}
function openAuth(mode = 'in', msg = '') {
  const m = document.getElementById('authModal'); if (!m) return;
  setAuthMode(mode); document.getElementById('authMsg').innerHTML = msg ? `<div class="notice">${msg}</div>` : '';
  m.classList.add('show');
}
function setAuthMode(mode) {
  const m = document.getElementById('authModal');
  m.dataset.mode = mode;
  m.querySelectorAll('.seg button').forEach(b => b.classList.toggle('on', b.dataset.m === mode));
  m.querySelectorAll('.only-up').forEach(e => { e.style.display = mode === 'up' ? 'block' : 'none'; e.querySelector('input') && (e.querySelector('input').required = mode === 'up'); });
  document.getElementById('authGo').textContent = mode === 'up' ? 'Create My Account' : 'Sign In';
  document.getElementById('authErr').style.display = 'none';
}
function wireAuth() {
  const m = document.getElementById('authModal'); if (!m) return;
  m.querySelector('.x').onclick = () => m.classList.remove('show');
  m.addEventListener('click', e => { if (e.target === m) m.classList.remove('show'); });
  m.querySelectorAll('.seg button').forEach(b => b.onclick = () => setAuthMode(b.dataset.m));
  document.getElementById('authForget').onclick = async () => {
    const email = document.getElementById('aEmail').value.trim();
    if (!email) return showAuthErr('Type your email above first, then click "Forgot password?" again.');
    await sb.auth.resetPasswordForEmail(email, { redirectTo: location.origin + '/account' });
    document.getElementById('authMsg').innerHTML = '<div class="notice">📬 If that email has an account, a reset link is on its way.</div>';
  };
  document.getElementById('authForm').addEventListener('submit', async e => {
    e.preventDefault();
    const mode = m.dataset.mode, b = document.getElementById('authGo');
    const email = document.getElementById('aEmail').value.trim(), password = document.getElementById('aPass').value;
    b.disabled = true; document.getElementById('authErr').style.display = 'none';
    let res;
    if (mode === 'up') {
      const first_name = document.getElementById('aFirst').value.trim(), last_name = document.getElementById('aLast').value.trim();
      const display_name = document.getElementById('aName').value.trim();
      if (!first_name || !last_name) { b.disabled = false; return showAuthErr('Please enter your first and last name.'); }
      if (!USERNAME_RE.test(display_name)) { b.disabled = false; return showAuthErr('Usernames are 3–20 letters, numbers, periods or underscores, no spaces.'); }
      try { const { data: free, error: ue } = await sb.rpc('username_available', { u: display_name });
        if (!ue && free === false) { b.disabled = false; return showAuthErr('That username is taken. Try another.'); } } catch (x) {}
      res = await sb.auth.signUp({ email, password, options: { data: { display_name, first_name, last_name }, emailRedirectTo: location.origin + location.pathname } });
      b.disabled = false;
      if (res.error) return showAuthErr(res.error.message);
      if (!res.data.session) {
        document.getElementById('authMsg').innerHTML = '<div class="notice">🎉 Almost there! Check your email and click the link to confirm your account, then come back and sign in.</div>';
        e.target.reset(); setAuthMode('in'); return;
      }
    } else {
      res = await sb.auth.signInWithPassword({ email, password });
      b.disabled = false;
      if (res.error) return showAuthErr(/confirm/i.test(res.error.message) ? 'Please confirm your email first (check your inbox).' : 'Email or password is incorrect.');
    }
    m.classList.remove('show');
    await loadMe(); renderTopbarUser();
    document.dispatchEvent(new CustomEvent('cc:auth'));
  });
}
function showAuthErr(t) { const e = document.getElementById('authErr'); e.textContent = t; e.style.display = 'block'; }

/* ---------- FREE QUOTE form (sidebar) ---------- */
function wireQuote() {
  document.querySelectorAll('form.js-quote').forEach(f => {
    f.addEventListener('submit', async e => {
      e.preventDefault();
      const g = n => (f.elements[n]?.value || '').trim();
      const err = f.parentElement.querySelector('.err'), b = f.querySelector('button[type=submit]');
      err.style.display = 'none'; b.disabled = true;
      const row = { name: g('name'), email: g('email'), phone: g('phone') || null, state: g('state') || null, contact_pref: g('contact_pref') || null,
        ship: g('ship') || null, sail_date: g('sail_date') || null, stateroom: g('stateroom') || null,
        adults: parseInt(g('adults') || '2', 10), children: parseInt(g('children') || '0', 10), notes: g('notes') || null, source: location.pathname };
      const { error } = await sb.from('quotes').insert(row);
      b.disabled = false;
      if (error) { err.textContent = 'Sorry, that didn\'t go through. Please check your email address and try again.'; err.style.display = 'block'; return; }
      f.style.display = 'none'; f.parentElement.querySelector('.qf-done').style.display = 'block';
    });
  });
  document.querySelectorAll('[data-quote]').forEach(b => b.addEventListener('click', e => { e.preventDefault(); prefillQuote(); }));
}
function prefillQuote(ship, room) {
  const f = document.querySelector('form.js-quote'); if (!f) return location.href = '/#quote';
  if (ship) f.elements.ship.value = ship;
  if (room) {
    const sel = f.elements.stateroom;
    if (![...sel.options].some(o => o.value === room)) sel.add(new Option(room, room), 1);
    sel.value = room;
  }
  const w = document.getElementById('quote');
  w.scrollIntoView({ behavior: 'smooth', block: 'start' });
  w.animate([{ boxShadow: '0 0 0 0 rgba(255,107,91,.9)' }, { boxShadow: '0 0 0 14px rgba(255,107,91,0)' }], { duration: 900, iterations: 2 });
  setTimeout(() => f.elements.name.focus({ preventScroll: true }), 600);
}

/* ---------- ADS ----------
   Only 3 ad spots on the whole site (home-mid, blog-bottom, post-bottom).
   Until an ad network is approved, each spot shows a friendly "house ad".
   To turn on Google AdSense later: set enabled:true, paste your ca-pub-… id
   and the slot ids AdSense gives you.  */
const ADS = {
  enabled: false,
  adsenseClient: '',            // e.g. 'ca-pub-1234567890123456'
  slots: { 'home-mid': '', 'blog-bottom': '', 'post-bottom': '' },
};
const HOUSE_ADS = [
  { e: '🗺️', t: 'Free Port Guides', s: 'Palm Beach, Tampa, Miami & Galveston guides for your inbox.', go: 'Send Them!', href: '/newsletter' },
  { e: '📣', t: 'Advertise on The Chill Compass', s: 'Reach cruisers planning their next getaway.', go: 'Get in Touch', href: 'mailto:admin@thechillcompass.com?subject=Advertising' },
];
function renderAds() {
  const slots = document.querySelectorAll('.ad-slot');
  if (!slots.length) return;
  if (ADS.enabled && ADS.adsenseClient) {
    const s = document.createElement('script');
    s.async = true; s.crossOrigin = 'anonymous';
    s.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + ADS.adsenseClient;
    document.head.appendChild(s);
    slots.forEach(el => {
      const id = ADS.slots[el.dataset.slot]; if (!id) return;
      el.innerHTML = `<div class="ad-label">Advertisement</div><ins class="adsbygoogle" style="display:block" data-ad-client="${ADS.adsenseClient}" data-ad-slot="${id}" data-ad-format="auto" data-full-width-responsive="true"></ins>`;
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    });
    return;
  }
  slots.forEach((el, i) => {
    const a = HOUSE_ADS[(i + new Date().getDate()) % HOUSE_ADS.length];
    const ext = a.href.startsWith('http') || a.href.startsWith('mailto') ? ' target="_blank" rel="noopener"' : '';
    el.innerHTML = `<div class="ad-label">Sponsored</div><a class="house-ad" href="${a.href}"${ext} ${a.href === '#quote' ? 'data-quote' : ''}><span class="e">${a.e}</span><div style="text-align:left"><b>${a.t}</b><span>${a.s}</span></div><span class="go">${a.go}</span></a>`;
  });
}

/* Newsletter signup – any form with class js-signup */
function wireSignups() {
  document.querySelectorAll('form.js-signup').forEach(form => {
    form.addEventListener('submit', async e => {
      e.preventDefault();
      const btn = form.querySelector('button');
      const email = form.querySelector('[name=email]').value.trim();
      const first = (form.querySelector('[name=first_name]') || {}).value?.trim() || null;
      const err = form.parentElement.querySelector('.err');
      if (err) err.style.display = 'none';
      btn.disabled = true;
      const { error } = await sb.from('subscribers').insert({ email, first_name: first, source: form.dataset.source || location.pathname });
      btn.disabled = false;
      if (error && error.code !== '23505') {
        if (err) { err.textContent = 'Hmm, something went wrong. Please check your email and try again.'; err.style.display = 'block'; }
        return;
      }
      store('cc_subscribed', '1');
      form.style.display = 'none';
      const thx = form.parentElement.querySelector('.thanks');
      if (thx) thx.style.display = 'block';
    });
  });
}

/* Gentle popup: after 40s or when leaving, once every 14 days, never for subscribers */
function wirePopup() {
  const pop = document.getElementById('pop');
  if (!pop || location.pathname.startsWith('/admin')) return;
  const close = () => pop.classList.remove('show');
  pop.querySelector('.x').addEventListener('click', close);
  pop.addEventListener('click', e => { if (e.target === pop) close(); });
  document.querySelectorAll('a[href="#signup"]').forEach(a => { if (!document.getElementById('signup')) a.addEventListener('click', e => { e.preventDefault(); pop.classList.add('show'); }); });
  if (store('cc_subscribed')) return;
  const last = +store('cc_pop_seen') || 0;
  if (Date.now() - last < 14 * 864e5) return;
  let shown = false;
  const show = () => { if (shown || store('cc_subscribed') || document.querySelector('.modal.show')) return; shown = true; pop.classList.add('show'); store('cc_pop_seen', String(Date.now())); };
  setTimeout(show, 40000);
  document.addEventListener('mouseout', e => { if (!e.relatedTarget && e.clientY < 10) show(); });
}

function wireNav() {
  const path = location.pathname.replace(/\/$/, '') || '/';
  document.querySelectorAll('.dock nav a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === path || (href !== '/' && path.startsWith(href + '/'))) a.classList.add('on');
  });
  const dock = document.querySelector('.dock');
  if (dock && 'IntersectionObserver' in window) {
    const m = document.querySelector('.masthead');
    if (m) new IntersectionObserver(([e]) => dock.classList.toggle('stuck', !e.isIntersecting)).observe(m);
  }
}

document.addEventListener('DOMContentLoaded', async () => {
  wireNav(); wireSignups(); wirePopup(); renderAds(); wireQuote(); wireAuth();
  await loadMe(); renderTopbarUser();
  document.dispatchEvent(new CustomEvent('cc:ready'));
});
