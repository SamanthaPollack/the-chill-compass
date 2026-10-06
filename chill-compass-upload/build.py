#!/usr/bin/env python3
"""Builds the static pages of The Chill Compass (v5 "Boardwalk" layout) from shared partials.
Run:  python3 build.py   then drag the site/ folder onto Netlify."""
import os
SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
DOMAIN = 'https://margaritavilleatseablog.com'
DESC = "Margaritaville at Sea cruise reviews, deck plans, packages, port guides and deals from travel advisors who love Margaritaville at Sea so much, we keep going back for more!"
V = '15'

def head(title, desc=DESC, path='/', extra=''):
    full = 'The Chill Compass | A Margaritaville at Sea Blog' if title == 'The Chill Compass' else f'{title} | The Chill Compass'
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
  <div class="l"><a href="/rollcalls">🙋 Roll Calls</a><a href="/port-guides#guides" class="hide-s">🗺️ Free Port Guides</a><a href="/about" class="hide-s">About Us</a><span>FL Seller of Travel ST150140</span></div>
  <div class="r" id="tbUser"></div>
</div></div>
<header class="masthead{' tall' if tall else ''}"><a class="home" href="/" aria-label="The Chill Compass home"></a><h1 class="sr">The Chill Compass: A Margaritaville at Sea Blog</h1></header>
<div class="tagbar">A Margaritaville at Sea Blog</div>
<div class="dock"><div class="wrap">
  <a href="/" class="mini" aria-label="Home"><img src="/assets/img/logo.jpg" alt="The Chill Compass" width="66" height="44"></a>
  <nav aria-label="Main"><ul>
    <li><a href="/">Home</a></li>
    <li><a href="/cruise-reviews">Cruise Reviews</a></li>
    <li><a href="/extra-packages">Extra Packages</a></li>
    <li><a href="/fleet">Fleet</a></li>
    <li><a href="/port-guides">Port Guides</a></li>
    <li><a href="/deals">Deals</a></li>
    <li><a href="/newsletter">Newsletter</a></li>
    <li><a href="/weddings">Weddings</a></li>
    <li><a href="/events">Events</a></li>
    <li><a href="/rollcalls">Roll Calls</a></li>
    <li><a href="/faq">FAQ</a></li>
  </ul></nav>
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
    <div class="thanks">🎉 You're on the list! <a href="/port-guides#guides">Open your free port guides →</a></div>
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
        <p style="margin:0;font-size:15px">Pointing you toward sun, ocean, cruise, relax &amp; good vibes. Cruise reviews, deck plans and roll calls from travel advisors who keep going back for more. 🍹</p>
      </div>
      <div><h3>Explore</h3><ul>
        <li><a href="/cruise-reviews">Cruise Reviews</a></li>
        <li><a href="/fleet">The Fleet: Ships, Deck Plans &amp; Rooms</a></li>
        <li><a href="/extra-packages">Extra Packages</a></li>
        <li><a href="/events">Events</a></li>
        <li><a href="/rollcalls">Roll Calls</a></li>
        <li><a href="/faq">FAQ</a></li></ul></div>
      <div><h3>Connect</h3><ul>
        <li><a href="/port-guides#guides">Free Port Guides</a></li>
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

# ======================= HOME = THE BLOG =======================
CAT_INTRO = {
    '': ('📰 Fresh from the deck', 'The latest Margaritaville at Sea reviews, port guides, deals and tips from our deck chairs.'),
    'Cruise Reviews': ('⭐ Cruise Reviews', 'Honest, sail-by-sail reviews of Paradise, Islander and Beachcomber: cabins, food, drinks, shows and the real vibe onboard.'),
    'Port Guides': ('🏝️ Port Guides', 'What to do, eat and skip in every Margaritaville at Sea port, plus tips for the homeports.'),
    'Deals': ('💸 Deals', 'Sales, promos and offers worth celebrating.'),
    'Tips & News': ('🧭 Tips & News', 'Packing hacks, planning tips and the latest Margaritaville at Sea news.'),
}

def blog_page(fname, cat, path, desc):
    eyebrow, sub = CAT_INTRO[cat]
    is_home = cat == ''
    guides_band = ('''<section class="sec" id="guides"><div class="sec-h"><h2>🗺️ Free printable port guides</h2></div>
  <p style="margin:-4px 0 12px;color:var(--ink-soft)">Terminal addresses, parking, check-in times, airports, where to stay and play, plus a cheat sheet for every port of call.</p>
  <div class="guide-grid">''' + ''.join(f'''<a class="guide g-lock" data-href="/assets/guides/chill-compass-port-guide-{f}.pdf" href="#guides"><span class="e">{e}</span><div><b>{t}</b><small>{s}</small></div></a>''' for f, e, t, s in [
        ('paradise-palm-beach', '🌺', 'Paradise · Palm Beach', 'Port of Palm Beach, Riviera Beach'),
        ('islander-tampa', '🏝️', 'Islander · Tampa', 'Port Tampa Bay, Terminal 6'),
        ('beachcomber-miami', '🐚', 'Beachcomber · Miami', 'PortMiami, Terminal C (from Jan 2027)'),
        ('beachcomber-galveston', '🤠', 'Beachcomber · Galveston', 'Galveston Terminal 28 (from Oct 2027)')]) + '''</div>
  <div class="card g-gate" style="margin-top:14px"><b>📬 Unlock all four guides free.</b> Pop in your email and they'll open right here (and we'll send you cruise tips and deals, no spam).
    <form class="form js-signup" data-source="port-guides-page" style="margin-top:10px"><input type="text" name="first_name" placeholder="First name" aria-label="First name" maxlength="80"><input type="email" name="email" placeholder="Email address" aria-label="Email address" required maxlength="250"><button class="btn btn-coral" type="submit">Unlock the Guides</button></form>
    <div class="err"></div><div class="thanks">🎉 Unlocked! Click any guide above to open it.</div></div>
</section>''') if cat == 'Port Guides' else ''
    body = (title_block(eyebrow, 'Where the cruise is chill &amp; the drinks come with umbrellas' if is_home else cat, sub) +
        guides_band +
        ('<p class="submit-cta"><a href="/write-for-us" class="btn btn-coral">✍️ Submit Your Cruise Review</a></p>' if cat == 'Cruise Reviews' else '') +
        ('<section class="sec"><div id="lead"></div></section>' if is_home else '') +
        '<div class="chips" id="chips"></div><div class="rows" id="list"><div class="loading">Loading posts…</div></div>' +
        f'<div class="ad-slot" data-slot="{"home-mid" if is_home else "blog-bottom"}"></div>' +
        ('''<section class="sec"><div class="band"><div class="e">📝</div><div><h3>Got a Margaritaville at Sea story?</h3>
  <p>Send your trip report, tips or photos to <a href="mailto:admin@margaritavilleatseablog.com?subject=Blog%20Submission">admin@margaritavilleatseablog.com</a> and you could be featured.</p></div>
  <a href="/write-for-us" class="btn btn-sun">How to Submit</a></div></section>''' if is_home else ''))
    js = '''<script>
const PAGE_CAT = %s;
function unlockGuides() {
  if (!store('cc_subscribed')) return;
  document.querySelectorAll('.g-lock').forEach(a => { a.href = a.dataset.href; a.target = '_blank'; a.rel = 'noopener'; a.classList.add('open'); });
  const g = document.querySelector('.g-gate'); if (g && !g.querySelector('.thanks').style.display) g.innerHTML = '<b>✅ Your free guides are unlocked.</b> Click any guide above to open or download it.';
}
document.addEventListener('submit', e => { if (e.target.matches('.g-gate form')) setTimeout(function chk(){ store('cc_subscribed') ? unlockGuides() : setTimeout(chk, 300); }, 300); }, true);
document.querySelectorAll('.g-lock').forEach(a => a.addEventListener('click', e => { if (!store('cc_subscribed')) { e.preventDefault(); const f = document.querySelector('.g-gate input[type=email]'); f.scrollIntoView({behavior:'smooth', block:'center'}); f.focus({preventScroll:true}); } }));
unlockGuides();
document.addEventListener('cc:ready', async () => {
  const qcat = catBySlug(new URLSearchParams(location.search).get('cat'));
  const cat = PAGE_CAT || qcat || null;
  document.getElementById('chips').innerHTML = `<a class="chip ${cat ? '' : 'on'}" href="/">All</a>` +
    Object.keys(CATS).map(k => `<a class="chip ${k === cat ? 'on' : ''}" href="/${CATS[k].slug}">${CATS[k].emoji} ${k}</a>`).join('');
  const posts = await fetchPosts({ limit: 60, category: cat });
  const lead = document.getElementById('lead');
  let rest = posts;
  if (lead && !cat) {
    if (posts.length) { lead.innerHTML = leadCard(posts[0]); rest = posts.slice(1); }
    else lead.innerHTML = '';
  }
  document.getElementById('list').innerHTML = rest.length ? rest.map(postRow).join('')
    : (posts.length ? '' : emptyBox(cat ? 'No ' + cat + ' posts yet. Stay tuned!' : 'Our first posts are setting sail soon!'));
});
</script>''' % ('null' if is_home else repr(cat))
    page(fname, 'The Chill Compass' if is_home else cat, body, desc=desc, path=path, extra_js=js, tall=is_home,
         extra_head=('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Blog","name":"The Chill Compass","url":"https://margaritavilleatseablog.com","description":"' + DESC + '","publisher":{"@type":"Organization","name":"Cruises Tours and Travel, LLC"}}</script>') if is_home else '')

blog_page('index.html', '', '/', DESC)
blog_page('cruise-reviews.html', 'Cruise Reviews', '/cruise-reviews', 'Margaritaville at Sea cruise reviews: Paradise, Islander and Beachcomber, from travel advisors who sail them.')
blog_page('port-guides.html', 'Port Guides', '/port-guides', 'Margaritaville at Sea port guides for Palm Beach, Tampa, Miami, Galveston and every port of call.')
blog_page('deals.html', 'Deals', '/deals', 'The best Margaritaville at Sea deals and promotions, found by travel advisors.')
blog_page('blog.html', 'Tips & News', '/tips', 'Margaritaville at Sea packing hacks, planning tips and news.')

# ======================= FLEET (landing) =======================
fl = title_block('🚢 The Fleet', 'Meet the Margaritaville at Sea ships', 'Pick a ship to explore it: ship details and highlights, photos, deck plans, and every stateroom and suite type on one page.') + '''
<div class="ship-cards" id="shipCards"><div class="loading">Loading ships…</div></div>'''
fl_js = '''<script>
document.addEventListener('cc:ready', async () => {
  const [{ data: ships }, { data: rooms }] = await Promise.all([
    sb.from('ships').select('*').order('sort'), sb.from('staterooms').select('ship').eq('active', true)]);
  const count = s => (rooms || []).filter(r => r.ship === s).length;
  document.getElementById('shipCards').innerHTML = (ships || []).map(s => {
    const facts = [s.guests && '👥 ' + s.guests, s.tonnage && '⚓ ' + s.tonnage].filter(Boolean).map(f => `<span>${esc(f)}</span>`).join('');
    return `<a class="ship-card" href="/fleet/${SHIPS[s.name].slug}">
      <div class="sc-img ship-${SHIPS[s.name].slug}" style="${s.hero_url ? `background-image:url('${esc(s.hero_url)}')` : ''}">${s.hero_url ? '' : `<span class="wm">${SHIPS[s.name].emoji}</span>`}</div>
      <div class="sc-body"><div class="eyebrow">${esc(s.tagline || '')}</div><h2>${esc(s.name)}</h2>
        <p>📍 ${esc(s.homeport || '')}</p>${facts ? `<div class="rc-chips">${facts}</div>` : ''}
        <p class="sc-what">Ship details · photos · deck plans · ${count(s.name)} room types</p>
        <span class="btn btn-coral btn-sm">Explore ${esc(s.name)} →</span></div>
    </a>`;
  }).join('');
});
</script>'''
page('fleet.html', 'The Fleet', fl, desc='Meet the Margaritaville at Sea fleet: Paradise, Islander and Beachcomber ship details, photos, deck plans and every stateroom type.', path='/fleet', extra_js=fl_js, rc=False)

# ======================= FLEET (one ship: details, photos, deck plans, rooms) =======================
ship = '''<div class="chips" id="shipChips" style="margin-top:4px"></div>
<div id="shipHead"><div class="loading">Loading…</div></div>
<div id="roomsAll"></div>
<p class="room-fine">Ship and stateroom details are summarized from Margaritaville at Sea's public ship information and can change. Exact size, beds and layout vary by stateroom, so ask us before you book. Photos and renderings are representative.</p>
<div class="lb" id="lb" hidden><button type="button" class="lb-x" aria-label="Close">×</button><button type="button" class="lb-p" aria-label="Previous photo">‹</button><img alt=""><button type="button" class="lb-n" aria-label="Next photo">›</button></div>'''
ship_js = '''<script>
const TIER_ORDER = ['Interior', 'Ocean View', 'Balcony', 'Suite'];
const TIER_EMOJI = { 'Interior': '🛏️', 'Ocean View': '🌊', 'Balcony': '🌅', 'Suite': '👑' };
let LB = [], LBi = 0;
function openLb(list, i) { LB = list; LBi = i; const lb = document.getElementById('lb'); lb.querySelector('img').src = LB[LBi]; lb.hidden = false; lb.classList.toggle('one', LB.length < 2); document.body.style.overflow = 'hidden'; }
function stepLb(d) { LBi = (LBi + d + LB.length) % LB.length; document.querySelector('#lb img').src = LB[LBi]; }
function closeLb() { document.getElementById('lb').hidden = true; document.body.style.overflow = ''; }
function roomPics(r) { const p = (r.photos || []).filter(Boolean); if (!p.length && r.image_url) p.push(r.image_url); return p; }
function roomCard(r) {
  const pics = roomPics(r), id = 'r-' + slugify(r.name);
  const main = pics.length ? `<img src="${esc(pics[0])}" alt="${esc(r.name)} on Margaritaville at Sea ${esc(r.ship)}" loading="lazy" data-zoom>`
    : `<div class="ph"><span>📸</span>Photo coming soon</div>`;
  const thumbs = pics.length > 1 ? `<div class="thumbs">${pics.map((p, i) => `<button type="button" class="${i ? '' : 'on'}" data-src="${esc(p)}" aria-label="Photo ${i + 1}"><img src="${esc(p)}" alt="" loading="lazy"></button>`).join('')}</div>` : '';
  const chips = [r.decks && '📍 ' + r.decks, r.occupancy && '👥 ' + r.occupancy].filter(Boolean).map(c => `<span>${esc(c)}</span>`).join('');
  return `<article class="room-card" id="${id}" data-pics='${esc(JSON.stringify(pics))}'>
    <div class="rc-pic">${main}<span class="tag tier-${r.tier.split(' ')[0]}">${esc(r.tier)}</span></div>${thumbs}
    <div class="rc-body"><h3>${esc(r.name)}</h3>${chips ? `<div class="rc-chips">${chips}</div>` : ''}
      <p>${esc(r.blurb || '')}</p>
      ${r.features && r.features.length ? `<ul class="feat">${r.features.map(f => `<li>${esc(f)}</li>`).join('')}</ul>` : ''}</div>
  </article>`;
}
document.addEventListener('cc:ready', async () => {
  const slug = location.pathname.replace(/^\\/(fleet|deck-plans)\\/?/, '').replace(/\\/$/, '') || new URLSearchParams(location.search).get('ship') || 'paradise';
  const name = shipBySlug(slug) || 'Paradise';
  document.getElementById('shipChips').innerHTML = Object.keys(SHIPS).map(k => `<a class="chip ${k === name ? 'on' : ''}" href="/fleet/${SHIPS[k].slug}"><span class="dot d-${SHIPS[k].slug}"></span>${k}</a>`).join('') + `<a class="chip" href="/fleet">All ships</a>`;
  const [{ data: s }, { data: rooms }] = await Promise.all([
    sb.from('ships').select('*').eq('name', name).maybeSingle(),
    sb.from('staterooms').select('*').eq('ship', name).eq('active', true).order('sort')]);
  document.title = `${name}: Ship Details, Deck Plans & Staterooms | The Chill Compass`;
  const sh = s || { name };
  const list = (rooms || []).sort((a, b) => TIER_ORDER.indexOf(a.tier) - TIER_ORDER.indexOf(b.tier) || a.sort - b.sort);
  const gal = (sh.photos || []).filter(Boolean), hi = (sh.highlights || []).filter(Boolean);
  const facts = [['Homeport', sh.homeport], ['Guests', sh.guests], ['Size', sh.tonnage], ['Built', sh.built && (sh.built + (sh.former_name ? ' (as ' + sh.former_name + ')' : ''))]].filter(f => f[1]);
  const nav = [['about', '⭐ About the ship'], gal.length && ['photos', '📸 Photos'], ['deck-plans', '🗺️ Deck plans'], ['rooms', '🛏️ Staterooms & suites']].filter(Boolean);
  document.getElementById('shipHead').innerHTML = `
    <div class="ship-hero ship-${SHIPS[name].slug}" style="${sh.hero_url ? `background-image:linear-gradient(180deg,rgba(11,57,84,.05),rgba(11,57,84,.8)),url('${esc(sh.hero_url)}')` : ''}">
      <div class="eyebrow" style="color:var(--sun)">${esc(sh.tagline || 'Margaritaville at Sea')}</div>
      <h1>Margaritaville at Sea ${esc(name)}</h1></div>
    <nav class="ship-nav" aria-label="${esc(name)} sections">${nav.map(n => `<a href="#${n[0]}">${n[1]}</a>`).join('')}</nav>
    <section class="card ship-sec" id="about"><h2>⭐ About ${esc(name)}</h2>
      ${sh.intro ? `<p class="ship-intro">${esc(sh.intro)}</p>` : ''}
      ${facts.length ? `<div class="facts-row">${facts.map(f => `<div><b>${f[0]}</b>${esc(f[1])}</div>`).join('')}</div>` : ''}
      ${hi.length ? `<h3>Onboard highlights</h3><ul class="feat">${hi.map(h => `<li>${esc(h)}</li>`).join('')}</ul>` : ''}</section>
    ${gal.length ? `<section class="ship-sec" id="photos"><div class="sec-h"><h2>📸 ${esc(name)} photos</h2><span class="fine" style="margin:0">Tap to enlarge</span></div>
      <div class="ship-gal">${gal.map((p, i) => `<button type="button" data-g="${i}"><img src="${esc(p)}" alt="Margaritaville at Sea ${esc(name)} photo ${i + 1}" loading="lazy"></button>`).join('')}</div></section>` : ''}
    <section class="card deck-box ship-sec" id="deck-plans"><div><h2>🗺️ ${esc(name)} deck plans</h2>
      <p>See where every stateroom, pool, bar and restaurant sits, deck by deck.</p></div>
      <div class="deck-acts">${sh.deck_plan_url ? `<a class="btn btn-navy" href="${esc(sh.deck_plan_url)}" target="_blank" rel="noopener">View deck plan</a>` : ''}
      ${sh.official_deck_plan_link ? `<a class="btn btn-ghost" href="${esc(sh.official_deck_plan_link)}" target="_blank" rel="noopener">Official deck plans ↗</a>` : ''}</div>
      ${sh.deck_plan_url && !/\\.pdf(\\?|$)/i.test(sh.deck_plan_url) ? `<a href="${esc(sh.deck_plan_url)}" target="_blank" rel="noopener" class="deck-img"><img src="${esc(sh.deck_plan_url)}" alt="${esc(name)} deck plan" loading="lazy"></a>` : ''}</section>`;
  const jump = TIER_ORDER.filter(t => list.some(r => r.tier === t));
  let html = `<div class="sec-h ship-sec" id="rooms" style="margin-top:28px"><h2>🛏️ Staterooms &amp; suites on ${esc(name)}</h2><span class="fine" style="margin:0">${list.length} room types</span></div>
    <div class="chips tier-jump">${jump.map(t => `<a class="chip" href="#tier-${slugify(t)}">${TIER_EMOJI[t]} ${t}</a>`).join('')}</div>`;
  jump.forEach(t => {
    html += `<h3 class="tier-h" id="tier-${slugify(t)}">${TIER_EMOJI[t]} ${t === "Suite" ? "Suites" : t + " Staterooms"}</h3><div class="room-grid">${list.filter(r => r.tier === t).map(roomCard).join('')}</div>`;
  });
  document.getElementById('roomsAll').innerHTML = list.length ? html : `<div id="rooms">${emptyBox('Room details coming soon')}</div>`;
  document.querySelectorAll('.ship-gal [data-g]').forEach(b => b.onclick = () => openLb(gal, +b.dataset.g));
  document.querySelectorAll('.room-card').forEach(card => {
    const pics = JSON.parse(card.dataset.pics || '[]'), img = card.querySelector('[data-zoom]');
    if (img) img.onclick = () => openLb(pics, Math.max(0, pics.indexOf(img.getAttribute('src'))));
  });
  document.querySelectorAll('.thumbs button').forEach(b => b.onclick = () => {
    const card = b.closest('.room-card'); card.querySelector('.rc-pic img').src = b.dataset.src;
    card.querySelectorAll('.thumbs button').forEach(x => x.classList.toggle('on', x === b));
  });
  const lb = document.getElementById('lb');
  lb.querySelector('.lb-x').onclick = closeLb; lb.querySelector('.lb-p').onclick = () => stepLb(-1); lb.querySelector('.lb-n').onclick = () => stepLb(1);
  lb.onclick = e => { if (e.target === lb) closeLb(); };
  document.addEventListener('keydown', e => { if (lb.hidden) return; if (e.key === 'Escape') closeLb(); if (e.key === 'ArrowLeft') stepLb(-1); if (e.key === 'ArrowRight') stepLb(1); });
  if (location.hash) { const el = document.querySelector(location.hash); if (el) el.scrollIntoView(); }
});
</script>'''
page('ship.html', 'The Fleet', ship, desc='Margaritaville at Sea ship details, photos, deck plans and every stateroom and suite type.', path='/fleet', extra_js=ship_js, rc=False)


# ======================= WEDDINGS =======================
WED_MAIL = 'mailto:admin@margaritavilleatseablog.com?subject=Wedding%20Inquiry&body=Names%3A%0AWedding%20date%20or%20sailing%20you%27re%20eyeing%3A%0AApprox.%20number%20of%20guests%3A%0APackage%20you%27re%20interested%20in%3A%0AAnything%20else%3A'
WED_BTN = f'<a class="btn btn-coral" href="{WED_MAIL}">💌 Inquire About a Wedding</a>'
wed_pk = [
  ('Bliss', '$999', '🌺', 'Everything you need to say "I do" at sea.', [
    'Personal wedding coordinator', 'Room rental', 'Officiant', 'Keepsake wedding certificate',
    'Bridal bouquet (single-color roses) and matching boutonniere', 'Margarita toast for the couple',
    'Priority check-in for the couple', 'Special in-room amenity', 'Dinner for the newlyweds at JWB Steakhouse',
    'Sound system and basic room lighting', 'Wedding cake']),
  ('Elation', '$1,699', '🥂', 'Everything in Bliss, plus:', [
    'Upgraded venue with panoramic views', 'Upgraded ceremony decorations',
    'Semi-private reception dinner in the Main Dining Room', 'In-house DJ (1 hour)',
    'Photographer (ceremony only, 1 hour)', 'Breakfast for the couple at JWB Steakhouse']),
  ('Paradise', '$2,699', '💍', 'Everything in Elation, plus:', [
    '3-tier wedding cake', 'Premium ceremony decorations and room lighting',
    'Live music reception (1 hour)', 'Photographer for the ceremony and reception']),
]
wed = title_block('💍 Weddings at Sea', 'Say "I do" in Margaritaville',
  'Barefoot vows, a margarita toast and your favorite people on a ship that feels like a beach party. Here\'s how weddings work on Margaritaville at Sea.') + \
  f'<p class="submit-cta">{WED_BTN}</p>' + '''
<div class="notice">Wedding packages are currently available on <b>Paradise</b> (sailing from Palm Beach). Your group needs at least <b>8 staterooms (16 guests)</b>, including the couple.</div>
<div class="sec-h" style="margin-top:22px"><h2>💒 Wedding packages</h2></div>
<div class="wed-grid">''' + ''.join(f'''
  <div class="card wed-card{' hot' if i == 1 else ''}"><div class="wed-e">{e}</div><h3>{n}</h3><div class="wed-price">{p}</div>
    <p class="wed-sub">{sub}</p><ul class="feat">{''.join(f'<li>{x}</li>' for x in inc)}</ul></div>''' for i, (n, p, e, sub, inc) in enumerate(wed_pk)) + '''
</div>
<div class="sec-h" style="margin-top:28px"><h2>📝 Good to know</h2></div>
<div class="card"><ul class="feat">
  <li><b>Officiant included:</b> every package comes with a professional officiant and a wedding coordinator.</li>
  <li><b>Minimum group:</b> 8 staterooms (16 guests), including the couple. More guests can be added for an extra fee.</li>
  <li><b>Guests who aren't sailing</b> can still attend the ceremony on board. Additional fees may apply.</li>
  <li><b>Make it a weekend:</b> welcome parties, cocktail celebrations, rehearsal dinners and other group events can be added.</li>
  <li><b>Make it yours:</b> upgrades like custom cakes and décor requests are available.</li>
</ul></div>
<div class="band" style="margin-top:26px"><div class="e">💌</div><div><h3>Dreaming of a cruise wedding?</h3>
  <p>Tell us your names, the sailing or month you have in mind and roughly how many guests, and we'll get back to you.</p></div>''' + WED_BTN + '''</div>
<p class="room-fine">Package prices and inclusions are from Margaritaville at Sea's published wedding packages as of October 2026 and can change.</p>'''
page('weddings.html', 'Weddings', wed, desc='Margaritaville at Sea wedding packages on Paradise: Bliss, Elation and Paradise packages, what\'s included and how to get married at sea.', path='/weddings')

# ======================= EXTRA PACKAGES =======================
def tbl(rows, head=('Package', 'Price (from)', "What you get")):
    return '<div class="tbl-wrap"><table class="tbl"><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr></thead><tbody>' + \
        ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table></div>'

pk = title_block('🍹 Extra Packages', 'Drink, dining &amp; Wi-Fi packages, decoded',
    'Here\'s what you can add to your Margaritaville at Sea cruise, what it costs and when it\'s worth it.') + '''
<div class="notice">Prices below are the cruise line's published "from" prices as of October 2026 and change often, especially with pre-cruise sales. Many packages are cheaper if you buy before you sail.</div>

<div class="toc chips"><a class="chip" href="#drinks">🍹 Drinks</a><a class="chip" href="#dining">🍤 Dining</a><a class="chip" href="#wifi">📶 Wi-Fi</a><a class="chip" href="#bundles">🎟️ Bundles</a><a class="chip" href="#more">🌴 More add-ons</a><a class="chip" href="#worth">🤔 Worth it?</a></div>

<div class="article" style="margin-top:14px">
<h2 id="drinks">🍹 Beverage packages</h2>
''' + tbl([
    ['<b>Ultimate Beverage Chill</b>', 'About $50–$70 per person, per night (varies by ship and sailing)', 'Beer, wine by the glass, cocktails and frozen "boat drinks," plus soda, juices, mocktails and bottled water. Up to 15 alcoholic or specialty drinks a day.'],
    ['<b>Unlimited Soda Package</b>', '$12 per person, per night', 'Souvenir cup with unlimited fountain soda refills.'],
    ['<b>Beers &amp; Cheers</b> (Paradise)', '$59.99 per package', 'Five chilled beers delivered with a souvenir cooler.'],
    ['<b>Berries &amp; Bubbly</b> (Paradise)', '$39.99 per package', 'Chilled sparkling wine with fresh berries, a sweet in-cabin treat.'],
]) + '''
<div class="tip"><b>Good to know:</b> If one adult (21+) in a stateroom buys the alcoholic package, every other adult in that stateroom has to buy it too. An automatic service charge is added to beverage packages, and specialty coffee, room-service drinks and full bottles aren't included.</div>

<h2 id="dining">🍤 Specialty dining</h2>
''' + tbl([
    ['<b>JWB Prime Steakhouse dinner</b>', '$55 per person', 'The splurge-worthy steakhouse night.'],
    ['<b>Sparkling Brunch</b>', '$19.90 per person', 'Chef-made brunch with a mimosa, bellini or sparkling wine.'],
    ['<b>Far Side Sampler</b> (Islander)', '$67.50 to $75 per person', 'A $25 dining credit to use at Far Side Sushi, Tiki Grill and Island Eats.'],
    ['<b>Prime Dining Package</b>', '$89 per person', 'JWB dinner, Sparkling Brunch and Far Side sushi, bundled for savings.'],
    ['<b>Ultimate Dining Chill</b> (Islander)', '$159 per person', 'The full specialty-dining lineup for big foodies.'],
]) + '''

<h2 id="wifi">📶 Wi-Fi ("Coconut Telegraph")</h2>
''' + tbl([
    ['<b>Connect</b>', '$19.99 per night, per device', 'Messaging on select apps (iMessage, WhatsApp and similar).'],
    ['<b>Basic</b>', '$26.99 per night, per device', 'Web browsing, email and Wi-Fi calling.'],
    ['<b>Premium</b>', '$30.99 per night, per device', 'Streaming, social media and general surfing.'],
    ['<b>Business</b>', '$39.99 per night, per device', 'The fastest tier, for working at sea.'],
]) + '''
<p>Buying before you sail usually gets you a pre-cruise discount, and hourly or daily plans are also sold onboard.</p>

<h2 id="bundles">🎟️ All-in-one bundles</h2>
''' + tbl([
    ['<b>Paradise License to Chill</b>', 'From $399 per person', 'Cocktails, dining, spa credit, Wi-Fi and VIP perks rolled into one.'],
    ['<b>Paradise Ultimate License to Chill</b>', 'From $499 per person', 'Upgrades to fine dining plus spa credit, Wi-Fi and VIP perks.'],
    ['<b>Islander Signature Chill</b>', 'From $599 per person', 'Islander-only bundle of drinks, dining and perks.'],
    ['<b>Ultimate Islander Escape</b>', 'From $799 per person', 'Express check-in, unlimited beverages, specialty dining, spa and more.'],
    ['<b>Faster Chill</b>', 'From $129 per stateroom', 'Express check-in, priority luggage delivery and Wi-Fi for two devices.'],
    ['<b>Express Pass</b>', 'From $49 per stateroom', 'Express check-in and disembarkation.'],
]) + '''

<h2 id="more">🌴 More fun add-ons</h2>
''' + tbl([
    ['<b>Pool-deck cabana</b>', 'From $499 (Paradise) / $799 (Islander) per cruise', 'Your own shady cabana for the whole cruise. Limited and non-refundable.'],
    ['<b>Changes in Latitude wine tasting</b>', '$29.99 per person', 'Curated wines paired with cheese.'],
    ['<b>Mixology class</b>', '$34.99 per person', 'Learn to make four cocktails (sea days, limited spots).'],
    ['<b>St. Somewhere Spa</b>', 'Massage from $179; couples $299', 'Massages, facials and the Ultimate Bliss package ($499).'],
    ['<b>Photo packages</b>', 'From $35.99', 'Professional cruise photos, or private sessions from $199.99.'],
]) + '''

<h2 id="worth">🤔 Are they worth it?</h2>
<ul>
<li><b>Drink package:</b> worth it if you'll have about 5 or more drinks a day. Do the math with the bar menu before you buy.</li>
<li><b>Soda package:</b> a no-brainer for kids and soda lovers on longer sailings.</li>
<li><b>Wi-Fi:</b> one Connect plan for messaging is plenty for most people. Save Premium for streaming or work.</li>
<li><b>Bundles:</b> great value if you'd buy the drinks <i>and</i> the specialty dining anyway.</li>
</ul>

</div>'''
page('extra-packages.html', 'Extra Packages', pk, desc='Margaritaville at Sea drink packages, specialty dining, Wi-Fi and add-ons explained, with prices and tips.', path='/extra-packages')

# ======================= NEWSLETTER =======================
nl = title_block('💌 Newsletter', 'Join the crew!', 'Our free email newsletter is the best way to keep up with The Chill Compass.') + '''
<div class="nl-card">
  <div class="nl-perks">
    <div><span>🗺️</span><b>Free port guides</b><small>Palm Beach, Tampa, Miami &amp; Galveston, printable PDFs</small></div>
    <div><span>💸</span><b>Deal alerts</b><small>Sales and promos as soon as we spot them</small></div>
    <div><span>⭐</span><b>New reviews &amp; tips</b><small>Fresh posts, straight to your inbox</small></div>
    <div><span>🎉</span><b>Event news</b><small>Themed cruises, group sailings and meet-ups</small></div>
  </div>
  <form class="form js-signup nl-form" data-source="newsletter-page">
    <input type="text" name="first_name" placeholder="First name" aria-label="First name" maxlength="80">
    <input type="email" name="email" placeholder="Email address" aria-label="Email address" required maxlength="250">
    <button class="btn btn-coral" type="submit">Sign Me Up!</button>
  </form>
  <div class="err"></div>
  <div class="thanks" style="font-size:18px;margin-top:10px">🎉 You're on the list! Watch your inbox for your free guides.</div>
  <p class="fine">No spam, ever. Unsubscribe anytime.</p>
</div>'''
page('newsletter.html', 'Newsletter', nl, desc='Join The Chill Compass newsletter for free Margaritaville at Sea port guides, deals and tips.', path='/newsletter')

# ======================= EVENTS =======================
ev = title_block('🎉 Events', 'Themed cruises, group sailings &amp; big dates',
    'Holiday cruises, festival sailings, ship debuts and group trips worth planning around.') + '''
<div class="ev-list" id="evList"><div class="loading">Loading events…</div></div>
<div class="band" style="margin-top:24px"><div class="e">🙋</div><div><h3>Meet your shipmates</h3><p>Sailing one of these? Find or start the Roll Call for your date and say hi before you sail.</p></div><a href="/rollcalls" class="btn btn-sun">Roll Calls</a></div>'''
ev_js = '''<script>
function fmtRange(a, b) {
  const A = dateOnly(a), o = { month: 'long', day: 'numeric', year: 'numeric' };
  if (!b) return A.toLocaleDateString('en-US', o);
  const B = dateOnly(b);
  return A.getMonth() === B.getMonth() && A.getFullYear() === B.getFullYear()
    ? `${A.toLocaleDateString('en-US', { month: 'long' })} ${A.getDate()}–${B.getDate()}, ${A.getFullYear()}`
    : `${A.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })} – ${B.toLocaleDateString('en-US', o)}`;
}
document.addEventListener('cc:ready', async () => {
  const today = new Date().toISOString().slice(0, 10);
  const { data } = await sb.from('events').select('*').eq('active', true).order('start_date');
  const list = (data || []).filter(e => (e.end_date || e.start_date) >= today);
  document.getElementById('evList').innerHTML = list.length ? list.map(e => {
    const d = dateOnly(e.start_date);
    return `<article class="ev">
      <div class="date-badge"><span>${d.toLocaleDateString('en-US', { month: 'short' })}</span><b>${d.getDate()}</b><span>${d.getFullYear()}</span></div>
      <div class="ev-body">${e.image_url ? `<img src="${esc(e.image_url)}" alt="" loading="lazy" class="ev-img">` : ''}
        <h3>${esc(e.title)}</h3>
        <div class="ev-meta">${[e.ship && '🚢 ' + esc(e.ship), '📅 ' + fmtRange(e.start_date, e.end_date), e.location && '📍 ' + esc(e.location)].filter(Boolean).join(' &nbsp;·&nbsp; ')}</div>
        <p>${esc(e.description || '')}</p>
        <div class="acts">${e.link ? `<a class="btn btn-navy btn-sm" href="${esc(e.link)}" target="_blank" rel="noopener">${esc(e.link_label || 'Learn more')} ↗</a>` : ''}</div>
      </div></article>`;
  }).join('') : emptyBox('New events coming soon', 'Join the newsletter and we\\'ll let you know.');
});
</script>'''
page('events.html', 'Events', ev, desc='Margaritaville at Sea themed cruises, holiday sailings, group cruises and ship debuts.', path='/events', extra_js=ev_js)

# ======================= FAQ =======================
FAQS = [
 ('Booking & money', [
  ("What's included in my cruise fare?", "Your stateroom, meals in the main dining room and buffet, most casual eateries, entertainment, pools and the kids' clubs. Not included: alcohol and soda (unless you buy a package), specialty dining, Wi-Fi, gratuities, spa treatments and shore excursions."),
  ("How much are gratuities?", "They're added to your onboard account automatically: $22 per person, per night in staterooms and $25 per person, per night in suites. Many people prepay them so there are no surprises at the end."),
  ("Does it cost more to book with a travel advisor?", "Nope! We're paid by the cruise line, so our help is free. We compare sailings and cabins, watch for price drops and promos, and help if anything goes sideways."),
  ("Should I buy travel insurance?", "We strongly recommend it, especially for hurricane-season sailings (June to November). It can cover cancellations, missed departures, medical care at sea and lost luggage. Ask us for options."),
 ]),
 ('Who can sail', [
  ("How old do I have to be?", "The person booking must be 18 or older at the time of sailing. You must be 21 to drink alcohol and 18 to enter the casino."),
  ("Can I bring my baby?", "Yes. On Paradise, infants must be at least 6 months old on the day you sail."),
  ("Are there kids' programs?", "Yes! There are three supervised kids' programs for ages 3 to 17, grouped by age, with games, crafts and parties."),
  ("What documents do I need?", "U.S. citizens on round-trip cruises from a U.S. port can usually sail with an original birth certificate plus government photo ID, but we always recommend a valid passport. If you have to fly home from a foreign port in an emergency, you'll need one. No photocopies or phone photos of IDs, and the name on your ID must match your reservation."),
 ]),
 ('Embarkation day', [
  ("When should I arrive at the port?", "About three weeks before sailing you'll get an arrival window based on your stateroom location. The terminal closes at 3:00 PM in Palm Beach and 2:30 PM in Tampa, and late guests are denied boarding. Grab our free port guides for parking and terminal tips."),
  ("How much luggage can I bring?", "Each guest can bring two standard-sized bags up to 50 pounds each. Extra bags are $55 each."),
  ("Can I bring my own alcohol?", "No outside alcohol is allowed. Bottles you buy in port are held at the gangway and returned at the end of the cruise."),
 ]),
 ('Onboard', [
  ("Is there Wi-Fi?", "Yes. The \"Coconut Telegraph\" plans start around $19.99 per night, per device for messaging. See our <a href='/extra-packages#wifi'>Extra Packages</a> page."),
  ("Is the drink package worth it?", "If you'll have about five or more drinks a day, usually yes. Remember that every adult in the stateroom has to buy it if one does. Our <a href='/extra-packages#drinks'>Extra Packages</a> page has the details."),
  ("Where can I smoke?", "Only in designated outdoor areas: Deck 9 next to the License to Chill pool on Paradise, and Deck 10 overlooking the LandShark pool on Islander. Smoking anywhere else can mean fines of up to $500."),
  ("Which ship is right for me?", "Paradise is perfect for quick 2- to 5-night Bahamas and Key West getaways. Islander does 4- to 7-night Western Caribbean trips from Tampa. Beachcomber is the new, biggest ship, sailing longer Caribbean itineraries from Miami in 2027 and then Galveston. Compare them on our <a href='/fleet'>Fleet</a> page."),
 ]),
]
faq_html = title_block('❓ FAQ', 'Frequently asked questions', 'Quick answers about sailing Margaritaville at Sea. Don\'t see your question? <a href="/contact">Ask us</a>!')
for sec, items in FAQS:
    faq_html += f'<h2 class="faq-h">{sec}</h2><div class="faq">' + ''.join(f'<details><summary>{q}</summary><div>{a}</div></details>' for q, a in items) + '</div>'
faq_html += '<p class="room-fine">Policies summarized from Margaritaville at Sea\'s published FAQ as of October 2026 and can change. Always check your booking documents.</p>'
import json as _json
faq_ld = '<script type="application/ld+json">' + _json.dumps({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
    {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for _, items in FAQS for q, a in items]}) + '</script>'
page('faq.html', 'FAQ', faq_html, desc='Margaritaville at Sea FAQ: gratuities, drink packages, documents, age rules, luggage and more.', path='/faq', extra_head=faq_ld)

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
  if (!p) { el.innerHTML = emptyBox('Oops, we drifted off course!', 'That post isn\\'t here. Try the <a href="/">home page</a> instead.'); return; }
  const c = CATS[p.category] || CATS['Cruise Reviews'];
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
      <a class="tag" href="/${c.slug}">${c.emoji} ${esc(p.category)}</a>
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
page('post.html', 'Post', post, path='/', extra_js=post_js)

# ======================= ABOUT =======================
about = title_block('🧭 About Us', 'Hey there, fellow beach bum! 🍹', 'Meet the crew behind The Chill Compass.') + '''
<div class="article" style="margin-top:0">
  <p>Grab a frozen drink and kick off your flip-flops, because you've found your new favorite cruise hangout!</p>
  <p>We're a crew of travel advisors who've enjoyed Margaritaville at Sea so much that we couldn't stop talking about it, so we started a blog. Between us we've sailed more than 100 cruises and spent over 15 years helping travelers plan everything from quick weekend getaways to big family reunions at sea.</p>
  <h2>What you'll find here</h2>
  <ul>
    <li><b>⭐ Cruise Reviews:</b> the real deal on Paradise, Islander and Beachcomber</li>
    <li><b>🚢 Fleet:</b> each ship's details, photos, deck plans and every stateroom and suite type</li>
    <li><b>🍹 Extra Packages:</b> drink, dining and Wi-Fi packages decoded</li>
    <li><b>🏝️ Port Guides</b>, <b>💸 Deals</b> and <b>🎉 Events</b> worth planning around</li>
    <li><b>🙋 Roll Calls:</b> meet the people sailing on your ship and date</li>
  </ul>
  <h2>Want us to plan it for you?</h2>
  <p>The Chill Compass is presented by <a href="https://www.cruisestoursandtravel.com" target="_blank" rel="noopener">Cruises Tours and Travel, LLC</a>. Our advisors can find the best cabin, perks and pricing for your next sailing, at no extra cost to you.</p>
  <p style="font-size:14px;opacity:.7;margin-top:30px"><i>The Chill Compass is an independent blog and is not affiliated with, endorsed by or sponsored by Margaritaville at Sea or Margaritaville Enterprises. All trademarks belong to their respective owners.</i></p>
</div>'''
page('about.html', 'About Us', about, desc='Meet the travel advisors behind The Chill Compass, an independent cruise blog for Margaritaville at Sea fans.', path='/about')

# ======================= CONTACT =======================
contact = title_block('🐚 Contact', 'Drop us a line!', 'Questions, post ideas or advertising? We\'d love to hear from you.') + '''
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
open(os.path.join(SITE, '_redirects'), 'w').write('''/staterooms      /fleet               301!
/staterooms/*    /fleet               301!
/deck-plans      /fleet               301!
/deck-plans/*    /fleet/:splat        301!
/blog            /                    301!
/post/*          /post.html           200
/rollcall/*      /rollcall.html       200
/fleet           /fleet.html          200
/fleet/*         /ship.html           200
/cruise-reviews  /cruise-reviews.html 200
/extra-packages  /extra-packages.html 200
/port-guides     /port-guides.html    200
/deals           /deals.html          200
/tips            /blog.html           200
/newsletter      /newsletter.html     200
/events          /events.html         200
/weddings        /weddings.html       200
/faq             /faq.html            200
/rollcalls       /rollcalls.html      200
/account         /account.html        200
/about           /about.html          200
/contact         /contact.html        200
/write-for-us    /write-for-us.html   200
/privacy         /privacy.html        200
/admin           /admin/index.html    200
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
    ''.join(f'  <url><loc>{DOMAIN}{p}</loc></url>\n' for p in ['/', '/cruise-reviews', '/extra-packages', '/fleet', '/fleet/paradise', '/fleet/islander', '/fleet/beachcomber', '/port-guides', '/deals', '/newsletter', '/events', '/weddings', '/faq', '/rollcalls', '/about', '/contact', '/write-for-us']) + '</urlset>\n')
print('built')
