#!/usr/bin/env python3
"""Builds the static pages of The Chill Compass (v5 "Boardwalk" layout) from shared partials.
Run:  python3 build.py   then drag the site/ folder onto Netlify."""
import os
SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
DOMAIN = 'https://margaritavilleatseablog.com'
DESC = "Cruise tips, staterooms, roll calls, port guides and deals from travel advisors who love Margaritaville at Sea so much, we keep going back for more!"
V = '5'

def head(title, desc=DESC, path='/', extra=''):
    full = title if title == 'The Chill Compass' else f'{title} | The Chill Compass'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The Chill Compass">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOMAIN}{path}">
<meta property="og:image" content="{DOMAIN}/assets/img/share.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/icon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/assets/img/icon-180.png">
<meta name="theme-color" content="#0B3954">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css?v={V}">
{extra}
</head>
<body>
'''

def header(tall=False):
    return f'''<div class="topbar"><div class="wrap">
  <div class="l"><a href="/rollcalls">🙋 Roll Calls</a><a href="#signup" class="hide-s">🗺️ Free Port Guides</a><span>Licensed FL Seller of Travel ST150140</span></div>
  <div class="r" id="tbUser"></div>
</div></div>
<header class="masthead{' tall' if tall else ''}"><a class="home" href="/" aria-label="The Chill Compass home"></a><h1 class="sr">The Chill Compass</h1></header>
<div class="dock"><div class="wrap">
  <a href="/" class="mini" aria-label="Home"><img src="/assets/img/logo.jpg" alt="The Chill Compass" width="66" height="44"></a>
  <nav aria-label="Main"><ul>
    <li><a href="/">Home</a></li>
    <li><a href="/staterooms">Staterooms</a></li>
    <li><a href="/rollcalls">Roll Calls</a></li>
    <li><a href="/blog">Blog</a></li>
    <li><a href="/blog?cat=port-guides">Port Guides</a></li>
    <li><a href="/blog?cat=packing-hacks">Packing Hacks</a></li>
    <li><a href="/blog?cat=deals">Deals</a></li>
    <li><a href="/about">About</a></li>
  </ul></nav>
  <a href="#quote" class="btn btn-coral btn-sm quote-btn" data-quote>Free Quote</a>
</div></div>
'''

STATES = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','Outside US']
QUOTE = '''<div class="widget" id="quote">
  <div class="wh"><h3>🛳️ Get a Free Quote</h3><p>Tell us your dream sailing. A real travel advisor will reply, with no cost and no obligation.</p></div>
  <div class="wb">
    <form class="qf js-quote">
      <div class="full"><label for="q_name">Your name</label><input id="q_name" name="name" required maxlength="140" autocomplete="name"></div>
      <div class="full"><label for="q_email">Email</label><input id="q_email" name="email" type="email" required maxlength="250" autocomplete="email"></div>
      <div><label for="q_phone">Phone</label><input id="q_phone" name="phone" type="tel" maxlength="30" autocomplete="tel" placeholder="Optional"></div>
      <div><label for="q_state">State</label><select id="q_state" name="state"><option value="">Choose</option>''' + ''.join(f'<option>{s}</option>' for s in STATES) + '''</select></div>
      <div><label for="q_ship">Ship</label><select id="q_ship" name="ship"><option value="">Not sure yet</option><option>Paradise</option><option>Islander</option><option>Beachcomber</option></select></div>
      <div><label for="q_date">Sail month</label><input id="q_date" name="sail_date" type="month"></div>
      <div class="full"><label for="q_room">Stateroom</label><select id="q_room" name="stateroom"><option value="">Not sure yet</option><option>Interior</option><option>Ocean View</option><option>Balcony</option><option>Suite</option></select></div>
      <div><label for="q_ad">Adults</label><select id="q_ad" name="adults">''' + ''.join(f'<option{" selected" if n == 2 else ""}>{n}</option>' for n in range(1, 9)) + '''</select></div>
      <div><label for="q_ch">Kids</label><select id="q_ch" name="children">''' + ''.join(f'<option>{n}</option>' for n in range(0, 7)) + '''</select></div>
      <div class="full"><label for="q_pref">Best way to reach you</label><select id="q_pref" name="contact_pref"><option>Email</option><option>Phone call</option><option>Text</option></select></div>
      <div class="full"><label for="q_notes">Anything else?</label><textarea id="q_notes" name="notes" rows="2" maxlength="2000" placeholder="Celebrating something? Flexible dates?"></textarea></div>
      <div class="full"><button class="btn btn-coral" type="submit">Get My Free Quote</button></div>
    </form>
    <div class="err"></div>
    <div class="qf-done"><div class="e">🎉</div><h3>Request received!</h3><p>One of our travel advisors will be in touch soon with options and pricing. Cheers! 🍹</p></div>
    <p class="qf-fine">Quotes by Cruises Tours and Travel, LLC · FL ST150140</p>
  </div>
</div>'''

GUIDES_W = '''<div class="widget teal" id="signup">
  <div class="wh"><h3>🗺️ Free Port Guides</h3><p>Palm Beach · Tampa · Miami · Galveston, plus our packing list.</p></div>
  <div class="wb">
    <form class="mini-form js-signup" data-source="sidebar">
      <input type="text" name="first_name" placeholder="First name" aria-label="First name" maxlength="80">
      <input type="email" name="email" placeholder="Email address" aria-label="Email address" required maxlength="250">
      <button class="btn btn-sun" type="submit">Send Me the Guides</button>
    </form>
    <div class="err"></div>
    <div class="thanks">🎉 You're on the list! Watch your inbox.</div>
    <div class="fine">No spam, ever. Unsubscribe anytime.</div>
  </div>
</div>'''

RC_W = '''<div class="widget navy">
  <div class="wh"><h3>🙋 Roll Call Chatter</h3><p>Meet your shipmates before you sail.</p></div>
  <div class="wb"><ul class="side-list" id="rcSide"><li style="opacity:.6">Loading…</li></ul>
  <a href="/rollcalls" class="btn btn-navy btn-sm" style="width:100%;margin-top:10px">All Roll Calls</a></div>
</div>'''

def sidebar(rc=True):
    return '<aside class="side">' + QUOTE + GUIDES_W + (RC_W if rc else '') + '</aside>'

AUTH = '''<div class="modal" id="authModal" role="dialog" aria-modal="true" aria-label="Sign in" data-mode="in">
  <div class="box">
    <button class="x" aria-label="Close">×</button>
    <h2>⛱️ Join the Crew</h2>
    <p style="margin:4px 0 0;color:var(--ink-soft)">A free account lets you post on Roll Calls and meet your shipmates.</p>
    <div class="seg"><button type="button" data-m="in">Sign in</button><button type="button" data-m="up">Create account</button></div>
    <div id="authMsg"></div>
    <form id="authForm">
      <div class="field only-up" style="display:none"><label for="aName">Screen name</label><input id="aName" maxlength="40" placeholder="e.g. ParrotheadPam"></div>
      <div class="field only-up" style="display:none"><label for="aTown">Hometown (optional)</label><input id="aTown" maxlength="60" placeholder="e.g. Tampa, FL"></div>
      <div class="field"><label for="aEmail">Email</label><input id="aEmail" type="email" required autocomplete="email"></div>
      <div class="field"><label for="aPass">Password</label><input id="aPass" type="password" required minlength="8" autocomplete="current-password"></div>
      <button class="btn btn-coral" id="authGo" type="submit" style="width:100%">Sign In</button>
      <p class="err" id="authErr"></p>
      <p class="fine" style="text-align:center"><button type="button" class="link" id="authForget">Forgot password?</button></p>
      <p class="fine only-up" style="display:none">By joining you agree to be kind. Posts are public. No spam, selling or personal info, please; we may remove posts or accounts that break the rules.</p>
    </form>
  </div>
</div>'''

FOOTER = '''<footer class="site">
  <div class="wrap">
    <div class="fgrid">
      <div>
        <h3>The Chill Compass</h3>
        <p style="margin:0;font-size:15px">Pointing you toward sun, ocean, cruise, relax &amp; good vibes. Cruise tips, staterooms and roll calls from travel advisors who keep going back for more. 🍹</p>
      </div>
      <div><h3>Explore</h3><ul>
        <li><a href="/staterooms">Staterooms</a></li>
        <li><a href="/rollcalls">Roll Calls</a></li>
        <li><a href="/blog">All Posts</a></li>
        <li><a href="/blog?cat=port-guides">Port Guides</a></li>
        <li><a href="/blog?cat=deals">Deals</a></li></ul></div>
      <div><h3>Connect</h3><ul>
        <li><a href="#quote" data-quote>Free Quote</a></li>
        <li><a href="#signup">Free Port Guides</a></li>
        <li><a href="/contact">Contact Us</a></li>
        <li><a href="/write-for-us">Write for Us</a></li></ul></div>
      <div><h3>About</h3><ul>
        <li><a href="/about">About Us</a></li>
        <li><a href="/account">My Account</a></li>
        <li><a href="/privacy">Privacy Policy</a></li>
        <li><a href="https://www.cruisestoursandtravel.com" target="_blank" rel="noopener">Cruises Tours and Travel</a></li></ul></div>
    </div>
    <div class="disclaimer">
      © <span id="yr">2026</span> The Chill Compass · Presented by Cruises Tours and Travel, LLC · FL Seller of Travel Reg. No. ST150140<br>
      Independent blog, not affiliated with, endorsed by or sponsored by Margaritaville at Sea or Margaritaville Enterprises. Stateroom details are summarized from public cruise line information and may change.
    </div>
  </div>
</footer>
<a href="#quote" class="btn btn-coral fab" data-quote>🛳️ Free Quote</a>
<div class="pop" id="pop" role="dialog" aria-modal="true" aria-label="Free guides">
  <div class="box">
    <button class="x" aria-label="Close">×</button>
    <div style="font-size:46px">🗺️🧳</div>
    <h2>Free Port Guides!</h2>
    <p style="margin:6px 0 18px">Palm Beach, Tampa, Miami &amp; Galveston, plus our packing list, straight to your inbox.</p>
    <form class="form js-signup" data-source="popup">
      <input type="text" name="first_name" placeholder="First name" aria-label="First name" maxlength="80">
      <input type="email" name="email" placeholder="Email address" aria-label="Email address" required maxlength="250">
      <button class="btn btn-sun" type="submit" style="width:100%">Send Them!</button>
    </form>
    <div class="err"></div>
    <div class="thanks">🎉 You're in! Watch your inbox.</div>
    <div class="fine">No spam, ever. Unsubscribe anytime.</div>
  </div>
</div>
''' + AUTH + '''
<script>document.getElementById('yr').textContent=new Date().getFullYear()</script>
'''

SCRIPTS = f'''<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="/assets/app.js?v={V}"></script>
<script>
document.addEventListener('cc:ready', async () => {{
  const el = document.getElementById('rcSide'); if (!el) return;
  const {{ data }} = await sb.from('roll_calls').select('id,ship,sail_date,post_count,last_post_at').gte('sail_date', new Date().toISOString().slice(0,10)).order('last_post_at', {{ ascending: false, nullsFirst: false }}).limit(5);
  el.innerHTML = (data && data.length) ? data.map(r => `<li><a href="/rollcall/${{r.id}}"><span class="dot d-${{SHIPS[r.ship].slug}}"></span>${{esc(r.ship)}} · ${{dateOnly(r.sail_date).toLocaleDateString('en-US',{{month:'short',day:'numeric',year:'numeric'}})}}</a><small>${{r.post_count}} posts${{r.last_post_at ? ' · ' + timeAgo(r.last_post_at) : ''}}</small></li>`).join('')
    : '<li>No roll calls yet. <a href="/rollcalls">Start the first one!</a></li>';
}});
</script>
'''

def page(name, title, main, desc=DESC, path='/', extra_head='', extra_js='', side=True, rc=True, tall=False):
    body = f'<div class="wrap"><div class="shell{"" if side else " wide"}"><main>{main}</main>{sidebar(rc) if side else ""}</div></div>'
    html = head(title, desc, path, extra_head) + header(tall) + body + '\n' + FOOTER + SCRIPTS + extra_js + '</body>\n</html>\n'
    os.makedirs(os.path.dirname(os.path.join(SITE, name)), exist_ok=True)
    open(os.path.join(SITE, name), 'w').write(html)

def title_block(eyebrow, h1, p=''):
    return f'<div class="page-title"><div class="eyebrow">{eyebrow}</div><h1>{h1}</h1>{f"<p>{p}</p>" if p else ""}</div>'

# ======================= HOME =======================
home = '''
<section class="sec"><div id="lead"><div class="loading">Loading the latest post…</div></div></section>

<section class="sec">
  <div class="sec-h"><h2>🛏️ Pick your stateroom</h2><a href="/staterooms">See every room →</a></div>
  <div class="ships">
    <a class="ship ship-paradise" href="/staterooms#paradise"><span class="wm">🌺</span><span class="big">Paradise</span><small>Palm Beach · 4 room types</small></a>
    <a class="ship ship-islander" href="/staterooms#islander"><span class="wm">🏝️</span><span class="big">Islander</span><small>Tampa · 12 room types</small></a>
    <a class="ship ship-beachcomber" href="/staterooms#beachcomber"><span class="wm">🐚</span><span class="big">Beachcomber</span><small>Miami · Galveston · 12 room types</small></a>
  </div>
</section>

<section class="sec">
  <div class="sec-h"><h2>📰 Fresh from the deck</h2><a href="/blog">All posts →</a></div>
  <div class="rows" id="latest"><div class="loading">Loading posts…</div></div>
</section>

<div class="ad-slot" data-slot="home-mid"></div>

<section class="sec">
  <div class="sec-h"><h2>🙋 Upcoming Roll Calls</h2><a href="/rollcalls">Find your sailing →</a></div>
  <div class="rc-list" id="rcHome"><div class="loading">Loading roll calls…</div></div>
</section>

<section class="sec">
  <div class="band"><div class="e">📝</div><div><h3>Got a Margaritaville at Sea story?</h3>
  <p>Send your trip report, tips or photos to <a href="mailto:admin@margaritavilleatseablog.com?subject=Blog%20Submission">admin@margaritavilleatseablog.com</a> and you could be featured.</p></div>
  <a href="/write-for-us" class="btn btn-sun">How to Submit</a></div>
</section>

<section class="sec">
  <div class="sec-h"><h2>🩴 Who we are</h2><a href="/about">Meet the crew →</a></div>
  <div class="card"><p style="margin:0">We're a crew of travel advisors who've enjoyed Margaritaville at Sea so much that we couldn't stop talking about it, so we started a blog. Think of us as your cruise buddies who've already tested the pool deck, tried the cocktails and found the best spot to watch the sunset. <b>100+ cruises sailed, 15+ years of advising, and more sunsets than we can count.</b></p></div>
</section>'''
home_js = '''<script>
document.addEventListener('cc:ready', async () => {
  const [posts, rc] = await Promise.all([
    fetchPosts({ limit: 6 }),
    sb.from('roll_calls').select('*').gte('sail_date', new Date().toISOString().slice(0, 10)).order('sail_date').limit(4)
  ]);
  const L = document.getElementById('lead'), el = document.getElementById('latest');
  if (!posts.length) {
    L.innerHTML = `<div class="lead"><div class="img" style="background:${CATS['Ship Scoop'].grad}">🛳️</div><div class="txt"><div class="eyebrow">Welcome aboard</div><h2>Where the cruise is chill &amp; the drinks come with umbrellas</h2><p>Our first post is setting sail soon! Browse the staterooms, find your Roll Call or grab our free port guides.</p><a href="/staterooms" class="btn btn-coral">Explore Staterooms</a></div></div>`;
    el.innerHTML = emptyBox('Our first posts are setting sail soon!');
  } else {
    L.innerHTML = leadCard(posts[0]);
    el.innerHTML = posts.length > 1 ? posts.slice(1).map(postRow).join('') : emptyBox('More posts are on the way!');
  }
  const r = rc.data || [];
  document.getElementById('rcHome').innerHTML = r.length ? r.map(rcRow).join('')
    : emptyBox('No roll calls yet', 'Sailing soon? <a href="/rollcalls">Start the roll call for your cruise</a> and meet your shipmates.');
});
</script>'''
page('index.html', 'The Chill Compass', home, path='/', extra_js=home_js, tall=True,
     extra_head='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Blog","name":"The Chill Compass","url":"https://margaritavilleatseablog.com","description":"' + DESC + '","publisher":{"@type":"Organization","name":"Cruises Tours and Travel, LLC"}}</script>')

# ======================= STATEROOMS =======================
rooms = title_block('🛏️ Staterooms', 'Find your perfect stateroom',
    'Pick a ship, then click through every room type one at a time. Found the one? Hit <b>Quote this room</b> and we\'ll price it for you.') + '''
<div class="ships" id="shipPick">
  <button class="ship ship-paradise" data-ship="Paradise"><span class="wm">🌺</span><span class="big">Paradise</span><small>Palm Beach, FL</small></button>
  <button class="ship ship-islander" data-ship="Islander"><span class="wm">🏝️</span><span class="big">Islander</span><small>Tampa, FL</small></button>
  <button class="ship ship-beachcomber" data-ship="Beachcomber"><span class="wm">🐚</span><span class="big">Beachcomber</span><small>Miami, FL · Galveston, TX</small></button>
</div>
<div class="viewer" id="viewer">
  <div class="room-nav" id="roomNav" role="tablist" aria-label="Stateroom types"></div>
  <div class="room" id="room"><div class="loading">Loading staterooms…</div></div>
</div>
<p class="room-fine">Room details are summarized from Margaritaville at Sea's public ship information and can change. Exact size, beds and layout vary by stateroom, so ask us before you book. Illustrations are for fun, not exact layouts.</p>'''
rooms_js = '''<script>
let ROOMS = [], SHIP = 'Paradise', IDX = 0;
const TIER_ORDER = ['Interior', 'Ocean View', 'Balcony', 'Suite'];
function shipRooms() { return ROOMS.filter(r => r.ship === SHIP); }
function renderNav() {
  const list = shipRooms(); let html = '', last = '';
  list.forEach((r, i) => {
    if (r.tier !== last) { html += `<h4>${esc(r.tier)}</h4>`; last = r.tier; }
    html += `<button role="tab" aria-selected="${i === IDX}" class="${i === IDX ? 'on' : ''}" data-i="${i}"><span class="n">${i + 1}</span>${esc(r.name.replace(/ Stateroom$/, ''))}</button>`;
  });
  const nav = document.getElementById('roomNav'); nav.innerHTML = html;
  nav.querySelectorAll('button').forEach(b => b.onclick = () => show(+b.dataset.i, true));
  const on = nav.querySelector('.on');
  if (on) { const nr = nav.getBoundingClientRect(), r = on.getBoundingClientRect();
    if (r.top < nr.top || r.bottom > nr.bottom) nav.scrollTop += r.top - nr.top - 40;
    if (r.left < nr.left || r.right > nr.right) nav.scrollLeft += r.left - nr.left - 20; }
}
function show(i, user) {
  const list = shipRooms();
  if (!list.length) { document.getElementById('room').innerHTML = emptyBox('Rooms coming soon', 'We\\'re still adding this ship\\'s staterooms.'); document.getElementById('roomNav').innerHTML = ''; return; }
  IDX = Math.max(0, Math.min(i, list.length - 1));
  const r = list[IDX], s = SHIPS[r.ship];
  const pic = r.image_url ? `<img src="${esc(r.image_url)}" alt="${esc(r.name)} on ${esc(r.ship)}">` : roomArt(r.tier, s.accent);
  const facts = [['Ship', r.ship], ['Category', r.tier], r.decks && ['Where', r.decks], r.occupancy && ['Sleeps', r.occupancy]].filter(Boolean);
  document.getElementById('room').innerHTML = `
    <div class="pic">${pic}<span class="tag tier tier-${r.tier.split(' ')[0]}">${esc(r.tier)}</span><span class="count">${IDX + 1} of ${list.length}</span>
      <div class="arrows"><button id="prv" aria-label="Previous room" ${IDX === 0 ? 'disabled' : ''}>‹</button><button id="nxt" aria-label="Next room" ${IDX === list.length - 1 ? 'disabled' : ''}>›</button></div></div>
    <div class="info">
      <h2>${esc(r.name)}</h2>
      <div class="ship-line"><span class="dot d-${s.slug}"></span>Margaritaville at Sea ${esc(r.ship)} · sails from ${esc(s.port)}</div>
      <div class="facts-row">${facts.map(f => `<div><b>${f[0]}</b>${esc(f[1])}</div>`).join('')}</div>
      <p style="margin:0">${esc(r.blurb || '')}</p>
      ${r.features && r.features.length ? `<ul class="feat">${r.features.map(f => `<li>${esc(f)}</li>`).join('')}</ul>` : '<div style="height:16px"></div>'}
      <div class="acts"><button class="btn btn-coral" id="qThis">🛳️ Quote this room</button>
        ${IDX < list.length - 1 ? `<button class="btn btn-ghost" id="nxt2">Next: ${esc(list[IDX + 1].name.replace(/ Stateroom$/, ''))} →</button>` : ''}</div>
    </div>`;
  document.getElementById('prv').onclick = () => show(IDX - 1, true);
  document.getElementById('nxt').onclick = () => show(IDX + 1, true);
  const n2 = document.getElementById('nxt2'); if (n2) n2.onclick = () => show(IDX + 1, true);
  document.getElementById('qThis').onclick = () => prefillQuote(r.ship, r.tier === 'Suite' ? 'Suite' : r.tier);
  renderNav();
  if (user) history.replaceState(null, '', '#' + s.slug + '/' + slugify(r.name));
}
function pickShip(name, roomSlug) {
  SHIP = name; IDX = 0;
  document.querySelectorAll('#shipPick .ship').forEach(b => { b.classList.toggle('on', b.dataset.ship === name); b.setAttribute('aria-pressed', b.dataset.ship === name); });
  if (roomSlug) { const k = shipRooms().findIndex(r => slugify(r.name) === roomSlug); if (k >= 0) IDX = k; }
  show(IDX, false);
}
document.querySelectorAll('#shipPick .ship').forEach(b => b.onclick = () => { pickShip(b.dataset.ship); history.replaceState(null, '', '#' + SHIPS[b.dataset.ship].slug); document.getElementById('viewer').scrollIntoView({ behavior: 'smooth', block: 'start' }); });
document.addEventListener('keydown', e => { if (e.target.closest('input,textarea,select')) return; if (e.key === 'ArrowRight') show(IDX + 1, true); if (e.key === 'ArrowLeft') show(IDX - 1, true); });
document.addEventListener('cc:ready', async () => {
  const { data, error } = await sb.from('staterooms').select('*').eq('active', true).order('sort');
  if (error || !data) { document.getElementById('room').innerHTML = '<div class="loading">Sorry, we couldn\\'t load the staterooms. Please refresh.</div>'; return; }
  ROOMS = data.sort((a, b) => TIER_ORDER.indexOf(a.tier) - TIER_ORDER.indexOf(b.tier) || a.sort - b.sort);
  const [sh, rm] = location.hash.slice(1).split('/');
  pickShip(shipBySlug(sh) || 'Paradise', rm);
});
</script>'''
page('staterooms.html', 'Staterooms', rooms, desc='Explore every Margaritaville at Sea stateroom and suite on Paradise, Islander and Beachcomber, one room at a time, and get a free quote.', path='/staterooms', extra_js=rooms_js, rc=False)

# ======================= ROLL CALLS (list) =======================
rcl = title_block('🙋 Roll Calls', 'Meet your shipmates before you sail',
    'Find your sailing, say hello, plan meet-ups and share tips with fellow cruisers on the same ship and date. Don\'t see your cruise? Start the roll call!') + '''
<div class="card" style="padding:16px 18px;margin-bottom:16px;display:flex;gap:12px;flex-wrap:wrap;align-items:center;justify-content:space-between">
  <div class="chips" id="rcChips" style="margin:0"></div>
  <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">
    <label class="fine" style="margin:0"><input type="checkbox" id="rcPast"> Show past sailings</label>
    <button class="btn btn-coral btn-sm" id="rcNew">+ Start a Roll Call</button>
  </div>
</div>
<div class="rc-list" id="rcAll"><div class="loading">Loading roll calls…</div></div>
<div class="modal" id="newRc" role="dialog" aria-modal="true" aria-label="Start a roll call">
  <div class="box">
    <button class="x" aria-label="Close">×</button>
    <h2>🙋 Start a Roll Call</h2>
    <p style="margin:6px 0 16px;color:var(--ink-soft)">One roll call per ship and sail date. We'll take you there if it already exists.</p>
    <form id="newRcForm">
      <div class="field"><label for="nShip">Ship</label><select id="nShip" required><option>Paradise</option><option>Islander</option><option>Beachcomber</option></select></div>
      <div class="field"><label for="nDate">Sail date</label><input id="nDate" type="date" required></div>
      <div class="field"><label for="nIt">Itinerary (optional)</label><input id="nIt" maxlength="150" placeholder="e.g. 4-night Cozumel from Tampa"></div>
      <button class="btn btn-coral" type="submit" style="width:100%">Create Roll Call</button>
      <p class="err" id="nErr"></p>
    </form>
  </div>
</div>'''
rcl_js = '''<script>
let RCS = [], F = 'All';
function drawRc() {
  const past = document.getElementById('rcPast').checked, today = new Date().toISOString().slice(0, 10);
  const list = RCS.filter(r => (F === 'All' || r.ship === F) && (past ? r.sail_date < today : r.sail_date >= today));
  if (past) list.reverse();
  document.getElementById('rcAll').innerHTML = list.length ? list.map(rcRow).join('')
    : emptyBox(past ? 'No past roll calls here' : 'No upcoming roll calls yet', past ? '' : 'Be the captain! Click <b>Start a Roll Call</b> for your sailing.');
}
document.getElementById('rcChips').innerHTML = ['All', 'Paradise', 'Islander', 'Beachcomber'].map(s => `<button class="chip ${s === 'All' ? 'on' : ''}" data-s="${s}">${s === 'All' ? 'All ships' : '<span class="dot d-' + SHIPS[s].slug + '"></span>' + s}</button>`).join('');
document.querySelectorAll('#rcChips .chip').forEach(c => c.onclick = () => { F = c.dataset.s; document.querySelectorAll('#rcChips .chip').forEach(x => x.classList.toggle('on', x === c)); drawRc(); });
document.getElementById('rcPast').onchange = drawRc;
const NM = document.getElementById('newRc');
NM.querySelector('.x').onclick = () => NM.classList.remove('show');
document.getElementById('rcNew').onclick = () => {
  if (!ME) return openAuth('up', 'Create a free account (or sign in) to start a roll call.');
  if (F !== 'All') document.getElementById('nShip').value = F;
  document.getElementById('nDate').min = new Date().toISOString().slice(0, 10);
  NM.classList.add('show');
};
document.getElementById('newRcForm').addEventListener('submit', async e => {
  e.preventDefault();
  const ship = document.getElementById('nShip').value, sail_date = document.getElementById('nDate').value, itinerary = document.getElementById('nIt').value.trim() || null;
  const ex = RCS.find(r => r.ship === ship && r.sail_date === sail_date);
  if (ex) return location.href = '/rollcall/' + ex.id;
  const { data, error } = await sb.from('roll_calls').insert({ ship, sail_date, itinerary, created_by: ME.id }).select().single();
  if (error) {
    if (error.code === '23505') { const { data: d } = await sb.from('roll_calls').select('id').eq('ship', ship).eq('sail_date', sail_date).single(); if (d) return location.href = '/rollcall/' + d.id; }
    const n = document.getElementById('nErr'); n.textContent = 'Sorry, we couldn\\'t create that roll call. ' + error.message; n.style.display = 'block'; return;
  }
  await sb.from('roll_call_members').insert({ roll_call_id: data.id, user_id: ME.id });
  location.href = '/rollcall/' + data.id;
});
document.addEventListener('cc:ready', async () => {
  const { data } = await sb.from('roll_calls').select('*').order('sail_date').limit(1000);
  RCS = data || []; const s = new URLSearchParams(location.search).get('ship');
  if (s && SHIPS[s]) document.querySelector(`#rcChips [data-s="${s}"]`).click(); else drawRc();
});
</script>'''
page('rollcalls.html', 'Roll Calls', rcl, desc='Margaritaville at Sea Roll Calls: find your sailing on Paradise, Islander or Beachcomber and meet your shipmates before you cruise.', path='/rollcalls', extra_js=rcl_js, rc=False)

# ======================= ROLL CALL (thread) =======================
rct = '''<p style="margin:0 0 12px"><a href="/rollcalls" style="font-weight:700;text-decoration:none">← All Roll Calls</a></p>
<div id="rcWrap"><div class="loading">Loading roll call…</div></div>'''
rct_js = '''<script>
const RID = decodeURIComponent(location.pathname.replace(/^\\/rollcall\\//, '').replace(/\\/$/, '')) || new URLSearchParams(location.search).get('id');
let RC = null, SAILORS = [];
async function loadRc() {
  const { data: r } = await sb.from('roll_calls').select('*').eq('id', RID).maybeSingle();
  if (!r) { document.getElementById('rcWrap').innerHTML = emptyBox('Roll call not found', 'It may have been removed. <a href="/rollcalls">See all roll calls</a>.'); return; }
  RC = r; const d = dateOnly(r.sail_date), s = SHIPS[r.ship];
  const days = Math.ceil((d - new Date(new Date().toDateString())) / 864e5);
  document.title = `${r.ship} Roll Call · ${d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })} | The Chill Compass`;
  document.getElementById('rcWrap').innerHTML = `
    <div class="rc-head">
      <div class="date-badge"><span>${d.toLocaleDateString('en-US', { month: 'short' })}</span><b>${d.getDate()}</b><span>${d.getFullYear()}</span></div>
      <div><div class="eyebrow"><span class="dot d-${s.slug}"></span>${esc(r.ship)} Roll Call</div>
        <h1>${d.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' })}</h1>
        <div style="color:var(--ink-soft);font-weight:700">${esc(r.itinerary || 'Sails from ' + s.port)}</div></div>
      <div class="countdown">${days > 0 ? `<b>${days}</b>day${days === 1 ? '' : 's'} to go!` : days === 0 ? '<b>🎉</b>Sail day!' : '<b>⛱️</b>Sailed'}</div>
    </div>
    <div class="card" style="margin-top:16px;padding:18px 20px">
      <div style="display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;align-items:center;margin-bottom:10px">
        <h3 style="font-size:20px">🧳 Who's sailing <span id="sCount" style="color:var(--ink-soft)"></span></h3>
        <div id="joinBox"></div>
      </div>
      <div class="sailors" id="sailors"></div>
    </div>
    <div class="thread" id="thread"><div class="loading">Loading posts…</div></div>
    <div id="composer"></div>`;
  await Promise.all([loadSailors(), loadPosts()]); drawComposer();
}
async function loadSailors() {
  const { data } = await sb.from('roll_call_members').select('user_id,cabin,created_at,profiles(display_name,hometown)').eq('roll_call_id', RID).order('created_at');
  SAILORS = data || [];
  document.getElementById('sCount').textContent = `(${SAILORS.length})`;
  document.getElementById('sailors').innerHTML = SAILORS.length ? SAILORS.map(m => `<span class="sailor" title="${esc(m.profiles?.hometown || '')}">${avatar(m.profiles?.display_name, 28)}${esc(m.profiles?.display_name || 'Cruiser')}${m.cabin ? ` <small style="color:var(--ink-soft)">· ${esc(m.cabin)}</small>` : ''}</span>`).join('')
    : '<span style="color:var(--ink-soft)">No one has checked in yet. Be the first!</span>';
  const mine = ME && SAILORS.some(m => m.user_id === ME.id);
  document.getElementById('joinBox').innerHTML = mine ? `<button class="link red" id="leave">Not sailing anymore? Leave</button>`
    : `<form id="joinF" style="display:flex;gap:8px;flex-wrap:wrap"><select id="cabin" style="font:inherit;padding:8px;border-radius:10px;border:2px solid #eadfca"><option value="">Cabin type (optional)</option><option>Interior</option><option>Ocean View</option><option>Balcony</option><option>Suite</option></select><button class="btn btn-teal btn-sm">🙋 I'm sailing!</button></form>`;
  const lv = document.getElementById('leave');
  if (lv) lv.onclick = async () => { await sb.from('roll_call_members').delete().eq('roll_call_id', RID).eq('user_id', ME.id); loadSailors(); };
  const jf = document.getElementById('joinF');
  if (jf) jf.onsubmit = async e => {
    e.preventDefault();
    if (!ME) return openAuth('up', 'Create a free account (or sign in) to check in on this roll call.');
    const { error } = await sb.from('roll_call_members').insert({ roll_call_id: RID, user_id: ME.id, cabin: document.getElementById('cabin').value || null });
    if (error) alert('Sorry, that didn\\'t work. ' + error.message); else loadSailors();
  };
}
async function loadPosts() {
  const { data } = await sb.from('roll_call_posts').select('id,body,created_at,user_id,profiles(display_name,hometown)').eq('roll_call_id', RID).order('created_at');
  const list = data || [];
  document.getElementById('thread').innerHTML = list.length ? list.map(p => `<div class="msg" id="p-${p.id}">${avatar(p.profiles?.display_name)}<div>
      <div class="who">${esc(p.profiles?.display_name || 'Cruiser')}<small>${p.profiles?.hometown ? esc(p.profiles.hometown) + ' · ' : ''}${timeAgo(p.created_at)}</small>
      ${ME && ME.id === p.user_id ? `<button class="link red" style="float:right" onclick="delPost('${p.id}')">Delete</button>` : ''}</div>
      <div class="txt">${esc(p.body)}</div></div></div>`).join('')
    : emptyBox('No posts yet', 'Say hi to your shipmates! Where are you from? Is this your first Margaritaville at Sea cruise?');
}
async function delPost(id) { if (!confirm('Delete your post?')) return; await sb.from('roll_call_posts').delete().eq('id', id); loadPosts(); }
function drawComposer() {
  const c = document.getElementById('composer');
  if (!ME) { c.innerHTML = `<div class="composer" style="text-align:center"><p style="margin:0 0 10px"><b>Want to join the conversation?</b> A free account lets you post and check in.</p><button class="btn btn-coral" onclick="openAuth('up')">Join the Crew</button> <button class="btn btn-ghost" onclick="openAuth('in')">Sign in</button></div>`; return; }
  if (ME.banned) { c.innerHTML = '<div class="notice">Your account can\\'t post right now. Questions? Email admin@margaritavilleatseablog.com.</div>'; return; }
  c.innerHTML = `<form class="composer" id="cmp"><label for="body" style="font-weight:800">Post as ${esc(ME.display_name)}</label>
    <textarea id="body" maxlength="4000" required placeholder="Say hi, share plans, ask questions… 🍹"></textarea>
    <div style="display:flex;justify-content:space-between;align-items:center;gap:10px;margin-top:8px;flex-wrap:wrap"><span class="fine" style="margin:0">Be kind · no personal info like cabin numbers or phone numbers</span><button class="btn btn-coral">Post Reply</button></div></form>`;
  document.getElementById('cmp').onsubmit = async e => {
    e.preventDefault(); const b = e.target.querySelector('button'); b.disabled = true;
    const { error } = await sb.from('roll_call_posts').insert({ roll_call_id: RID, user_id: ME.id, body: document.getElementById('body').value.trim() });
    b.disabled = false;
    if (error) return alert('Sorry, your post didn\\'t go through. ' + error.message);
    if (!SAILORS.some(m => m.user_id === ME.id)) await sb.from('roll_call_members').insert({ roll_call_id: RID, user_id: ME.id });
    document.getElementById('body').value = ''; await Promise.all([loadPosts(), loadSailors()]);
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
  };
}
document.addEventListener('cc:ready', loadRc);
document.addEventListener('cc:auth', () => { if (RC) { loadSailors(); loadPosts(); drawComposer(); } });
</script>'''
page('rollcall.html', 'Roll Call', rct, path='/rollcalls', extra_js=rct_js)

# ======================= BLOG =======================
blog = title_block('📰 The Blog', '<span id="bh">All the Chill Cruise Intel</span>', 'Ship scoop, port guides, packing hacks and deals, fresh from our deck chairs.') + '''
<div class="chips" id="chips"></div>
<div class="rows" id="list"><div class="loading">Loading posts…</div></div>
<div class="ad-slot" data-slot="blog-bottom"></div>'''
blog_js = '''<script>
document.addEventListener('cc:ready', async () => {
  const slug = new URLSearchParams(location.search).get('cat');
  const cat = catBySlug(slug);
  document.getElementById('chips').innerHTML = `<a class="chip ${cat ? '' : 'on'}" href="/blog">All</a>` +
    Object.keys(CATS).map(k => `<a class="chip ${k === cat ? 'on' : ''}" href="/blog?cat=${CATS[k].slug}">${CATS[k].emoji} ${k}</a>`).join('');
  if (cat) { document.getElementById('bh').textContent = cat; document.title = cat + ' | The Chill Compass'; }
  const posts = await fetchPosts({ limit: 60, category: cat });
  document.getElementById('list').innerHTML = posts.length ? posts.map(postRow).join('') : emptyBox(cat ? 'No ' + cat + ' posts yet. Stay tuned!' : 'Our first posts are setting sail soon!');
});
</script>'''
page('blog.html', 'Blog', blog, path='/blog', extra_js=blog_js)

# ======================= POST =======================
post = '''<div id="post"><div class="loading" style="padding:120px 20px">Loading…</div></div>
<div class="ad-slot" data-slot="post-bottom"></div>
<section class="sec" id="related-wrap" style="display:none"><div class="sec-h"><h2>You might also like</h2></div><div class="rows" id="related"></div></section>'''
post_js = '''<script src="https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js"></script>
<script>
function setMeta(sel, attr, val) { let m = document.querySelector(sel); if (m) m.setAttribute(attr, val); }
document.addEventListener('cc:ready', async () => {
  const el = document.getElementById('post');
  const slug = decodeURIComponent(location.pathname.replace(/^\\/post\\//, '').replace(/\\/$/, '')) || new URLSearchParams(location.search).get('slug');
  const { data: p } = await sb.from('posts').select('*').eq('slug', slug).maybeSingle();
  if (!p) { el.innerHTML = emptyBox('Oops, we drifted off course!', 'That post isn\\'t here. Try the <a href="/blog">blog</a> instead.'); return; }
  const c = CATS[p.category] || CATS['Ship Scoop'];
  document.title = p.title + ' | The Chill Compass';
  const d = p.excerpt || p.title;
  setMeta('meta[name=description]', 'content', d); setMeta('meta[property="og:title"]', 'content', p.title);
  setMeta('meta[property="og:description"]', 'content', d); setMeta('meta[property="og:url"]', 'content', location.origin + '/post/' + p.slug);
  setMeta('link[rel=canonical]', 'href', location.origin + '/post/' + p.slug);
  if (p.cover_url) setMeta('meta[property="og:image"]', 'content', p.cover_url);
  const heroBg = p.cover_url ? `background-image:url('${esc(p.cover_url)}')` : `background:${c.grad}`;
  const url = encodeURIComponent(location.href), t = encodeURIComponent(p.title);
  el.innerHTML = `
    <section class="article-hero" style="${heroBg}">
      <a class="tag" href="/blog?cat=${c.slug}">${c.emoji} ${esc(p.category)}</a>
      <h1>${esc(p.title)}</h1>
      <div>${p.published ? fmtDate(p.published_at) : '<b>DRAFT (only you can see this)</b>'}</div>
    </section>
    <article class="article">
      ${DOMPurify.sanitize(p.content || '', { ADD_TAGS: ['iframe'], ADD_ATTR: ['allow', 'allowfullscreen', 'frameborder', 'target'] })}
      <div class="share"><b>Share the chill:</b>
        <a href="https://www.facebook.com/sharer/sharer.php?u=${url}" target="_blank" rel="noopener">Facebook</a>
        <a href="https://pinterest.com/pin/create/button/?url=${url}&description=${t}" target="_blank" rel="noopener">Pinterest</a>
        <a href="mailto:?subject=${t}&body=${url}">Email</a>
        <button onclick="navigator.clipboard.writeText(location.href);this.textContent='Copied! ✓'">Copy link</button>
      </div>
    </article>`;
  const ld = document.createElement('script'); ld.type = 'application/ld+json';
  ld.textContent = JSON.stringify({ '@context': 'https://schema.org', '@type': 'BlogPosting', headline: p.title, description: d, image: p.cover_url || undefined, datePublished: p.published_at, dateModified: p.updated_at, publisher: { '@type': 'Organization', name: 'The Chill Compass' } });
  document.head.appendChild(ld);
  const rel = await fetchPosts({ limit: 3, category: p.category, excludeId: p.id });
  if (rel.length) { document.getElementById('related').innerHTML = rel.map(postRow).join(''); document.getElementById('related-wrap').style.display = 'block'; }
});
</script>'''
page('post.html', 'Post', post, path='/blog', extra_js=post_js)

# ======================= ABOUT =======================
about = title_block('🧭 About Us', 'Hey there, fellow beach bum! 🍹', 'Meet the crew behind The Chill Compass.') + '''
<div class="article" style="margin-top:0">
  <p>Grab a frozen drink and kick off your flip-flops, because you've found your new favorite cruise hangout!</p>
  <p>We're a crew of travel advisors who've enjoyed Margaritaville at Sea so much that we couldn't stop talking about it, so we started a blog. Between us we've sailed more than 100 cruises and spent over 15 years helping travelers plan everything from quick weekend getaways to big family reunions at sea.</p>
  <h2>What you'll find here</h2>
  <ul>
    <li><b>🛏️ Staterooms:</b> click through every room type on Paradise, Islander and Beachcomber</li>
    <li><b>🙋 Roll Calls:</b> meet the people sailing on your ship and date</li>
    <li><b>🚢 Ship Scoop:</b> the real deal on dining, pools, drinks and entertainment</li>
    <li><b>🏝️ Port Guides:</b> what to do, eat and skip in every port</li>
    <li><b>🧳 Packing Hacks</b> and <b>💸 Deals</b> worth celebrating</li>
  </ul>
  <h2>Want us to plan it for you?</h2>
  <p>The Chill Compass is presented by <a href="https://www.cruisestoursandtravel.com" target="_blank" rel="noopener">Cruises Tours and Travel, LLC</a>. Our advisors can find the best cabin, perks and pricing for your next sailing, at no extra cost to you. Just fill out the <a href="#quote" data-quote>free quote form</a>.</p>
  <p style="font-size:14px;opacity:.7;margin-top:30px"><i>The Chill Compass is an independent blog and is not affiliated with, endorsed by or sponsored by Margaritaville at Sea or Margaritaville Enterprises. All trademarks belong to their respective owners.</i></p>
</div>'''
page('about.html', 'About Us', about, desc='Meet the travel advisors behind The Chill Compass, an independent cruise blog for Margaritaville at Sea fans.', path='/about')

# ======================= CONTACT =======================
contact = title_block('🐚 Contact', 'Drop us a line!', 'Questions, post ideas or advertising? We\'d love to hear from you. Ready to book? Use the <a href="#quote" data-quote>free quote form</a>.') + '''
<div class="card">
  <form id="contact">
    <div class="field"><label for="cn">Your name</label><input id="cn" name="name" required maxlength="150"></div>
    <div class="field"><label for="ce">Email</label><input id="ce" name="email" type="email" required maxlength="250"></div>
    <div class="field"><label for="cm">Message</label><textarea id="cm" name="message" rows="6" required maxlength="5000"></textarea></div>
    <button class="btn btn-coral" type="submit">Send Message</button>
    <p id="cerr" class="err"></p>
  </form>
  <div id="cthx" style="display:none;text-align:center"><div style="font-size:54px">🎉</div><h2>Message received!</h2><p>Thanks for reaching out. We'll get back to you soon.</p></div>
</div>
<p style="margin-top:16px">Want to submit your own blog post? Email <a href="mailto:admin@margaritavilleatseablog.com?subject=Blog%20Submission"><b>admin@margaritavilleatseablog.com</b></a>.</p>'''
contact_js = '''<script>
document.getElementById('contact').addEventListener('submit', async e => {
  e.preventDefault();
  const f = e.target, b = f.querySelector('button'), err = document.getElementById('cerr');
  b.disabled = true; err.style.display = 'none';
  const { error } = await sb.from('messages').insert({ name: f.name.value.trim(), email: f.email.value.trim(), message: f.message.value.trim() });
  b.disabled = false;
  if (error) { err.textContent = 'Sorry, that didn\\'t go through. Please try again.'; err.style.display = 'block'; return; }
  f.style.display = 'none'; document.getElementById('cthx').style.display = 'block';
});
</script>'''
page('contact.html', 'Contact Us', contact, desc='Get in touch with The Chill Compass crew.', path='/contact', extra_js=contact_js)

# ======================= WRITE FOR US =======================
wfu = title_block('📝 Write for Us', 'Share your Margaritaville at Sea story!', 'Fellow cruisers make the best tour guides. We\'d love to feature your trip on The Chill Compass.') + '''
<div class="article" style="margin-top:0">
  <h2 style="margin-top:0">What we're looking for</h2>
  <ul>
    <li><b>Trip reports:</b> your sailing, day by day, with the highs (and the "next time we'll…")</li>
    <li><b>Port tips:</b> favorite beaches, bites, shops and excursions</li>
    <li><b>Stateroom reviews:</b> your cabin, with photos!</li>
    <li><b>Packing and money-saving hacks</b> that made your cruise better</li>
    <li><b>Photos!</b> Sunsets, pool deck, cocktails, cabins: the more the merrier</li>
  </ul>
  <h2>How to submit</h2>
  <ol>
    <li>Write your story (about 500–1,500 words is perfect, but we're flexible).</li>
    <li>Attach 3–10 of your own photos (please only send photos you took).</li>
    <li>Include your first name (or nickname) and the month/year you sailed.</li>
    <li>Email it all to <a href="mailto:admin@margaritavilleatseablog.com?subject=Blog%20Submission">admin@margaritavilleatseablog.com</a> with the subject line <b>"Blog Submission"</b>.</li>
  </ol>
  <h2>The fine print</h2>
  <p>We read every submission and will reach out if your story is a fit. We may lightly edit for length and clarity, and we'll credit you by the name you provide. By submitting, you confirm the words and photos are your own and give us permission to publish them on The Chill Compass and our social pages.</p>
  <p style="text-align:center;margin-top:28px"><a href="mailto:admin@margaritavilleatseablog.com?subject=Blog%20Submission" class="btn btn-coral">📧 Email Your Story</a></p>
</div>'''
page('write-for-us.html', 'Write for Us', wfu, desc='Submit your own Margaritaville at Sea trip report, tips or photos to be featured on The Chill Compass.', path='/write-for-us')

# ======================= ACCOUNT =======================
acct = title_block('⛱️ My Account', 'Your crew profile', 'Update your screen name and hometown, or set a new password.') + '''
<div id="acct"><div class="loading">Loading…</div></div>'''
acct_js = '''<script>
async function drawAcct() {
  const el = document.getElementById('acct');
  if (!ME) { el.innerHTML = `<div class="card" style="text-align:center"><p>Sign in to manage your account.</p><button class="btn btn-coral" onclick="openAuth('in')">Sign In</button> <button class="btn btn-ghost" onclick="openAuth('up')">Create Account</button></div>`; return; }
  el.innerHTML = `<div class="card" style="margin-bottom:16px"><h2 style="margin-bottom:12px">Profile</h2><form id="pf">
    <div class="field"><label for="pn">Screen name</label><input id="pn" minlength="2" maxlength="40" required value="${esc(ME.display_name)}"></div>
    <div class="field"><label for="ph">Hometown</label><input id="ph" maxlength="60" value="${esc(ME.hometown || '')}"></div>
    <button class="btn btn-coral">Save Profile</button> <span id="pmsg"></span></form>
    <p class="fine">Signed in as ${esc(ME.email)}</p></div>
    <div class="card"><h2 style="margin-bottom:12px">New password</h2><form id="pw">
    <div class="field"><label for="p1">New password</label><input id="p1" type="password" minlength="8" required autocomplete="new-password"></div>
    <button class="btn btn-teal">Update Password</button> <span id="pwmsg"></span></form></div>`;
  document.getElementById('pf').onsubmit = async e => { e.preventDefault();
    const { error } = await sb.from('profiles').update({ display_name: document.getElementById('pn').value.trim(), hometown: document.getElementById('ph').value.trim() || null }).eq('id', ME.id);
    document.getElementById('pmsg').textContent = error ? '⚠️ ' + error.message : '✅ Saved!'; if (!error) { await loadMe(); renderTopbarUser(); } };
  document.getElementById('pw').onsubmit = async e => { e.preventDefault();
    const { error } = await sb.auth.updateUser({ password: document.getElementById('p1').value });
    document.getElementById('pwmsg').textContent = error ? '⚠️ ' + error.message : '✅ Password updated!'; if (!error) e.target.reset(); };
}
document.addEventListener('cc:ready', drawAcct);
document.addEventListener('cc:auth', drawAcct);
sb.auth.onAuthStateChange(async (ev) => { if (ev === 'PASSWORD_RECOVERY' || ev === 'SIGNED_IN') { await loadMe(); renderTopbarUser(); drawAcct(); } });
</script>'''
page('account.html', 'My Account', acct, path='/account', extra_js=acct_js, rc=False)

# ======================= PRIVACY =======================
privacy = title_block('Privacy', 'Privacy Policy', 'Last updated: October 2026') + '''
<div class="article" style="margin-top:0;font-size:16px">
  <p>The Chill Compass ("we," "us") is presented by Cruises Tours and Travel, LLC. This policy explains what information we collect on margaritavilleatseablog.com and how we use it.</p>
  <h3>Information you give us</h3>
  <p>When you sign up for our email list we collect your first name (optional) and email address. When you request a free quote we collect your name, email, and any phone number, state and trip details you provide, and our travel advisors use them to prepare and send your quote. When you use our contact form we collect your name, email address and message. You can unsubscribe from our emails at any time using the link in any email, or by contacting us.</p>
  <h3>Roll Call accounts</h3>
  <p>If you create a Roll Call account we store your email, password (securely, by our database provider), screen name and optional hometown. Your screen name, hometown, roll call check-ins and posts are public. Please don't post personal details like phone numbers or cabin numbers. You can edit your profile on the My Account page or ask us to delete your account.</p>
  <h3>Cookies, analytics and advertising</h3>
  <p>Like most websites, we and our partners may use cookies and similar technologies to understand how visitors use the site, keep you signed in and show advertising. Third-party vendors, including Google, may use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this site and/or other sites on the Internet. You may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>.</p>
  <h3>Affiliate links</h3>
  <p>Some links on this site may be affiliate links, which means we may earn a small commission if you make a purchase, at no extra cost to you. We only recommend things we'd use ourselves.</p>
  <h3>Sharing</h3>
  <p>We do not sell your personal information. We share it only with service providers who help us run the site and send email (for example, our database and email providers), and when required by law.</p>
  <h3>Children</h3>
  <p>This site is not directed to children under 13, and we do not knowingly collect their information. Roll Call accounts are for adults 18+.</p>
  <h3>Contact</h3>
  <p>Questions? Email <a href="mailto:admin@margaritavilleatseablog.com">admin@margaritavilleatseablog.com</a> or write to Cruises Tours and Travel, LLC, 5006 Sanderling Ridge Dr, Lithia, FL 33547.</p>
</div>'''
page('privacy.html', 'Privacy Policy', privacy, desc='Privacy policy for The Chill Compass.', path='/privacy', rc=False)

# ======================= 404 =======================
nf = '''<div class="empty" style="padding:60px 20px"><div class="e">🧭</div><h3 style="font-size:30px">Oops, we drifted off course!</h3><p>That page washed out to sea. Let's get you back to the beach.</p>
<p style="margin-top:20px"><a href="/" class="btn btn-coral">Back to Home</a></p></div>'''
page('404.html', 'Page Not Found', nf, path='/404')

# ======================= Netlify config =======================
open(os.path.join(SITE, '_redirects'), 'w').write('''/post/*      /post.html        200
/rollcall/*  /rollcall.html    200
/blog        /blog.html        200
/staterooms  /staterooms.html  200
/rollcalls   /rollcalls.html   200
/account     /account.html     200
/about       /about.html       200
/contact     /contact.html     200
/write-for-us /write-for-us.html 200
/privacy     /privacy.html     200
/admin       /admin/index.html 200
''')
open(os.path.join(SITE, '_headers'), 'w').write('''/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
/admin/*
  X-Robots-Tag: noindex, nofollow
  Cache-Control: no-store
/account*
  X-Robots-Tag: noindex
/assets/img/*
  Cache-Control: public, max-age=2592000
''')
open(os.path.join(SITE, 'robots.txt'), 'w').write(f'User-agent: *\nDisallow: /admin\nDisallow: /account\nSitemap: {DOMAIN}/sitemap.xml\n')
open(os.path.join(SITE, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join(f'  <url><loc>{DOMAIN}{p}</loc></url>\n' for p in ['/', '/staterooms', '/rollcalls', '/blog', '/about', '/contact', '/write-for-us']) + '</urlset>\n')
print('built')
