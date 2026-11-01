"""Namaste Tarot: a Manhattan tarot house. Angle: sit for a tarot reading, then take home a deck and the reading-table things, from our own on-site shop."""
import json, os
import engine as G
E = G.E
BUSINESS_TYPE = 'Store'
THEME_COLOR = '#2a1640'
FONTS = 'https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap'
ORG_DESC = 'Namaste Tarot is a tarot house in Manhattan: tarot readings on West 14th Street, and a shelf of decks and reading-table goods you can order online.'
LLMS_NOTE = ('Namaste Tarot is a tarot reading and tarot goods brand operated by Wealth Edge Ventures Inc. Readings take place inside Namaste Bookshop, 2 West 14th Street, New York. '
             'Each reader has a profile on this site and is reserved on their Square scheduling page. Products have pages and a cart on this site; checkout and shipping are handled by Namaste Bookshop\'s Shopify store, and prices refresh daily.')
R = json.load(open(os.path.join(os.path.dirname(__file__), 'readers.json')))
NAV = [('/readings/', 'Readings'), ('/readers/', 'Readers'), ('/decks/', 'Decks'), ('/reading-table/', 'Reading table'), ('/about/', 'About')]
CART = True
SHOP_PATH = '/decks/'
PAIR_TITLE = 'For the reading table'

def shell(pg):
    nav = ''.join(f'<a href="{h}"' + (' aria-current="page"' if pg['path'] == h else '') + f'>{t}</a>' for h, t in NAV)
    return (f'<body><a class="skip" href="#main">Skip to content</a><header class="mast"><a class="seal" href="/" aria-label="Namaste Tarot home">'
            f'<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="12" y="4" width="24" height="40" rx="3" fill="none" stroke="currentColor" stroke-width="2"/>'
            f'<path d="M24 14l2.6 6.4 6.9.5-5.3 4.4 1.7 6.7L24 28.4l-5.9 3.6 1.7-6.7-5.3-4.4 6.9-.5z" fill="#d9a441"/></svg><span>Namaste <b>Tarot</b></span></a>'
            f'{G.cart_button()}<nav class="menu" aria-label="Main">{nav}</nav></header><main id="main">{pg["body"]}</main>'
            f'<footer class="foot"><div class="fcol"><b>Namaste Tarot</b><p>Tarot readings and tarot goods on West 14th Street, Manhattan.</p>'
            f'<p><a href="tel:{G.TEL}">{G.PHONE}</a><br><a href="mailto:{G.EMAIL}">{G.EMAIL}</a></p></div>'
            f'<div class="fcol"><b>Hours</b><p>' + '<br>'.join(f'{d}: {h}' for d, h in G.HOURS) + '</p></div>'
            f'<div class="fcol"><b>Where</b><p>Inside Namaste Bookshop, {G.ADDR}. Operated by Wealth Edge Ventures Inc.</p><p><a href="/about/">About</a> &middot; <a href="/privacy/">Privacy</a></p></div></footer>'
            f'<div class="dock"><a href="/readers/">Book a reading</a><a href="tel:{G.TEL}">Call</a></div></body></html>')

def reader_card(k, line):
    r = R[k]
    return (f'<li class="rc"><img src="{E(G.img(r["img"], 240))}" alt="{E(r["name"])}" width="96" height="96" loading="lazy">'
            f'<div><h3>{E(r["name"])}</h3><p>{line}</p><p class="from">From ${r["from"]}</p>'
            f'<a class="pill" href="/readers/{k}/">Meet {E(r["name"].split()[0])}</a></div></li>')

def card(x, cat):
    return (f'<li class="pc"><img src="{E(G.img(x["img"], 400))}" alt="{E(x["t"])}" width="200" height="200" loading="lazy">'
            f'<h3>{E(x["t"])}</h3><p class="price">{G.money(x["p"])}</p><a class="ghost sm" {G.buy_attrs(x, cat)}>Details</a>{G.atc(x, cat, "Add to cart", "buy")}</li>')

READERS_BY_DECK = [
 ('Classic and Thoth decks', [
   ('casey-deamoira', 'Reads the Thoth deck and pairs it with Hellenistic astrology, so a session can look at your birth chart, your current transits, or both.'),
   ('anthony-fusco', 'Has worked with the Voyager Tarot for a quarter century and is known for business, love and timing questions.'),
   ('damon-stang', 'A master tarot reader steeped in folk magic, with a long professional career and press coverage behind him.'),
   ('mychal-a-bryan', 'Reads Qabalistic tarot in one-hour sessions, alongside traditional astrology.')]),
 ('Cards with a second system', [
   ('mallika', 'Lays Lenormand for the plain facts and tarot for the reasons behind them.'),
   ('lizanne', 'Works with Everyday Art Cards and mediumship, and asks for your question first.'),
   ('lu-camy', 'Her own illustrated oracle deck, Soul Synergy, sits on the table next to the tarot.'),
   ('dainichi-lazuli', 'Mixes tarot with Vedic astrology, numerology, crystals and Norse runes.'),
   ('alexander-d-santiago', 'Offers tarot on its own or combined with Western or Vedic chart work.'),
   ('priya', 'A third-generation astrologer who also reads tarot.')]),
 ('Readers who lead with intuition', [
   ('rebecca-martinez', 'Bilingual sessions, English or Spanish, guided by what she hears as she reads.'),
   ('catherine-marks', 'Psychic tarot from a clairvoyant who also works as a medium.'),
   ('andrea-dopewitchkira', 'Eleven years of tarot, with a longer "Witch Talk" session if you want to keep talking.'),
   ('brinly-erin', 'Clairvoyant and clairaudient, with a focus on self-worth and inner strength.'),
   ('high-priestess-judith', 'Known as La Gitana; love questions are her specialty.'),
   ('sophia-strange', 'Writes you a short poem from what comes up in the spread.'),
   ('tyler-t-mann-tarot', 'Reads like a motivational coach and keeps the advice practical.')]),
]

GROUP_OF = {k: h for h, items in READERS_BY_DECK for k, _ in items}
LINE_OF = {k: l for h, items in READERS_BY_DECK for k, l in items}
def reader_pages():
    for k, h in GROUP_OF.items():
        r = R[k]; first = r['name'].split()[0]
        where = {'bookshop': f'at the tables inside Namaste Bookshop, {G.ADDR}', 'upstairs': f'in a private room at {G.HC_STREET}', 'both': 'at the 14th Street tables or upstairs in Suite 1104, depending on the day', 'remote': 'remotely for now'}[r['home']]
        body = (f'<section class="page"><div class="rhead"><img src="{E(G.img(r["img"], 400))}" alt="{E(r["name"])}" width="150" height="150"><div><p class="eyebrow">{E(h)}</p><h1>{E(r["name"])}</h1></div></div>'
                f'<p class="lede">{E(LINE_OF[k])}</p><p>{E(first)} reads {where}.' + (' Phone sessions are available too.' if r['phone'] else '') + '</p>'
                f'<h2>Sessions</h2>{G.services_list(k, "inline")}'
                f'<p><a class="pill big" href="{E(r["book"])}" rel="nofollow noopener">Book {E(first)}</a></p>'
                f'<p class="small">Booking opens {E(first)}\'s Square appointment page with live times; payment there confirms the seat. Want a deck for afterward? <a href="/decks/">See the decks</a>.</p>'
                f'<p><a href="/readers/">Back to the readers</a></p></section>')
        G.add(f'/readers/{k}/', f'{r["name"]}: Tarot Readings | Namaste Tarot', f'{r["name"]} reads tarot with Namaste Tarot in Manhattan. {LINE_OF[k]} From ${r["from"]}.', body,
              ld=[G.person_ld(k, f'/readers/{k}/')], crumbs=[('Home', '/'), ('Readers', '/readers/'), (r['name'], f'/readers/{k}/')])

def product_desc(x, shelf):
    if shelf == 'Decks': return f"{x['t']}: a tarot deck from the Namaste Tarot shelf, {G.money(x['p'])}. Add it to your cart and it ships from New York."
    return f"{x['t']}: a reading-table piece from Namaste Tarot, {G.money(x['p'])}. Add it to your cart and it ships from New York."

def product_body(x, cat, shelf, path):
    t = x['t']; v = x.get('vendor') or ''
    if cat == 'decks':
        why = ('A good first deck if you are learning, since most guidebooks are written around this imagery.' if 'rider' in t.lower() or 'waite' in t.lower()
               else 'Pick the deck whose pictures you want to keep looking at; that matters more than which one is "right".')
        notes = f'<p>{why}</p>'
    else:
        notes = '<p>None of this is needed to read tarot. It just keeps cards clean, carried well, or standing up where you can see them while you think.</p>'
    facts = ''.join(f'<li><b>{a}</b> {E(b)}</li>' for a, b in [('Maker', v), ('SKU', x.get('sku') or ''), ('Barcode', x.get('gtin') or '')] if b)
    return (f'<section class="page prod"><div class="pimg"><img src="{E(G.img(x["img"], 800))}" alt="{E(t)}" width="400" height="400"></div><div>'
            f'<p class="eyebrow">{shelf}</p><h1>{E(t)}</h1><p class="price big">{G.money(x["p"])}</p>{G.atc(x, cat, "Add to cart", "pill big", True)}'
            f'{notes}<ul class="facts">{facts}</ul><p class="small">Ships from New York. Price checked daily; if it sells out it leaves the shelf. <a href="{path}">Back to {shelf.lower()}</a></p></div></section>')

def pages():
    decks = G.cached('decks', lambda: G.from_collection('tarot-cards-decks', 36, skip=r'keychain|display|wholesale'))
    table = G.cached('table', lambda: G.by_handles([
        'cosmic-bloom-flower-of-life-velvet-tarot-card-drawstring-bag-6x8', 'the-fool-tarot-pouch', 'purple-flower-of-life-mandala-with-tassels-6-x-8-printed-bag',
        'crown-chakra-embroidered-velvet-pouch-black-5-x-7', 'blue-evil-eye-mandala-with-tassels-6-x-8-printed-bag', '4x4-chrysalis-velvet-pouch-bag',
        'tarot-talisman-the-star', 'tarot-talisman-the-empress-by-lo-scarabeo', '0-the-fool-tarot-talisman', 'xviii-the-moon-tarot-talisman',
        'sun-tarot-card-holder', 'celestial-filigree-rosewood-color-wood-box-4x-2', 'antique-wooden-chest-storage-box-green', 'acacia-wooden-cylinder-storage-box-2-75h-x-3-80d']))
    reader_pages()
    G.product_pages(decks, 'decks', 'Decks', '/decks/', [('Home', '/')])
    G.product_pages(table, 'table', 'Reading table', '/reading-table/', [('Home', '/')])
    G.add('/cart/', 'Your Cart | Namaste Tarot', 'Your Namaste Tarot cart.', '<section class="page"><h1>Your cart</h1><p class="cmsg" role="status" aria-live="polite"></p><div data-cart-page><div class="cbody" data-cart-body><p>Loading your cart&hellip;</p></div></div><noscript><p>The cart needs JavaScript. Call <a href="tel:+12126450141">212-645-0141</a> to order by phone.</p></noscript><p><a href="/decks/">Keep browsing decks</a></p></section>', robots='noindex', sitemap=False)
    home = (f'<section class="hero"><div class="arch"><p class="eyebrow">Namaste Tarot &middot; 14th Street, Manhattan</p>'
            f'<h1>Have your cards read. Then take a deck home.</h1>'
            f'<p class="lede">Namaste Tarot pairs a tarot reading with the tools of the craft. Sit with one of our readers for fifteen minutes or a full hour, '
            f'then choose a deck, pouch or talisman from our shelf and order it right here.</p>'
            f'<p><a class="pill big" href="/readers/">Book a tarot reading</a> <a class="ghost" href="/decks/">See the decks</a></p></div></section>'
            f'<section class="trio"><article><h2>A reading</h2><p>Sessions come in 15-minute steps, up to a full hour. Most readers start at about $35 for 15 minutes, and you confirm the figure before paying.</p><a href="/readings/">How readings work here</a></article>'
            f'<article><h2>A reader</h2><p>Some readers use the Thoth deck, some add Lenormand or astrology, and some read mostly by intuition. Pick by style.</p><a href="/readers/">Readers by deck and style</a></article>'
            f'<article><h2>A deck</h2><p>{len(decks)} tarot decks in stock, with prices checked every day. Add one to your cart from any page.</p><a href="/decks/">Browse decks</a></article></section>'
            f'<section class="band"><h2>On the shelf this week</h2><ul class="grid">' + ''.join(card(x, 'decks') for x in decks[:8]) + '</ul>'
            f'<p class="more"><a href="/decks/">All {len(decks)} decks</a> &middot; <a href="/reading-table/">Pouches, talismans and boxes</a></p></section>'
            f'<section class="note"><h2>Where to find us</h2><p>Namaste Tarot readings happen at tables inside Namaste Bookshop on West 14th Street, '
            f'and in private rooms upstairs at 80 Fifth Avenue, Suite 1104. Orders placed here ship from New York.</p>'
            f'<p><a href="{G.DIRECTIONS}">Directions</a> &middot; <a href="tel:{G.TEL}">{G.PHONE}</a></p></section>')
    G.add('/', 'Namaste Tarot | Tarot Readings & Tarot Decks, 14th Street NYC',
          'Book a tarot reading with Namaste Tarot on West 14th Street in Manhattan, or order a tarot deck, pouch or talisman from our shelf.', home,
          ld=[G.shop_ld(), G.product_ld(decks[:8], 'Tarot decks on the shelf this week')])
    faq = [
        ('Do I have to book ahead?', 'Booking ahead holds a time. Same-day readings are possible when a reader has an open slot; each reader\'s profile links to their live openings, or call ' + G.PHONE + ' to ask.'),
        ('Can I pay at the shop instead of online?', 'If online booking gives you trouble, you can come in and pay cash. Call first so a reader can be held for you.'),
        ('Will the reader tell me my future?', 'A tarot reading is a way to look at a situation from new angles. Our readers differ in style, but none of them can promise an outcome, and nobody should use a reading in place of a doctor, a lawyer or an accountant.'),
        ('Can I get a reading if I live outside New York?', 'Yes. Several readers take phone sessions at the same prices as in person. Phone readers are marked on their profiles.'),
    ]
    readings = (f'<section class="page"><h1>Tarot readings at Namaste Tarot</h1><p class="lede">A Namaste Tarot reading is a seat at a small table on 14th Street with one reader, one deck and your question.</p>'
                f'<h2>Choosing a length</h2><table class="len"><tr><th>Length</th><th>Good for</th></tr>'
                f'<tr><td>15 minutes</td><td>One clear question and a short spread</td></tr><tr><td>30 minutes</td><td>A few related questions, or one bigger spread</td></tr>'
                f'<tr><td>45 minutes</td><td>Two or three areas of life, with time to talk</td></tr><tr><td>60 minutes</td><td>A full look at where things stand, or a reading combined with astrology</td></tr></table>'
                f'<p>Each reader chooses their own rates. Many charge about $35 for 15 minutes and $130 to $140 for an hour; a few specialists charge more. You always see the cost on the booking screen first.</p>'
                f'<h2>Booking</h2><ol class="steps"><li>Pick a reader on the <a href="/readers/">readers page</a> and open their profile.</li>'
                f'<li>Pick in-person or phone, then a length and a time.</li><li>Pay online, then come in a few minutes early, or keep your phone nearby for a phone session.</li></ol>'
                f'<h2>Where you sit</h2><p>In-person readings take place either at the tables inside Namaste Bookshop, {G.ADDR}, or in the private rooms upstairs at {G.HC_STREET}. '
                f'Your booking confirmation tells you where to go.</p>'
                f'<h2>Questions people ask before booking</h2><dl class="faq">' + ''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in faq) + '</dl>'
                f'<p><a class="pill big" href="/readers/">Choose a reader</a></p></section>')
    G.add('/readings/', 'Tarot Reading Lengths, Prices & Booking | Namaste Tarot',
          'How tarot readings work at Namaste Tarot in Manhattan: 15 to 60 minute sessions, typical prices, in person or by phone, and how to book.', readings,
          ld=[G.faq_ld(faq)], crumbs=[('Home', '/'), ('Readings', '/readings/')])
    rd = ''.join(f'<h2>{E(h)}</h2><ul class="rlist">' + ''.join(reader_card(k, E(l)) for k, l in items) + '</ul>' for h, items in READERS_BY_DECK)
    G.add('/readers/', 'Tarot Readers by Deck & Style | Namaste Tarot',
          'Namaste Tarot\'s readers grouped by how they read: Thoth and classic decks, tarot with Lenormand or astrology, and intuitive readers.',
          f'<section class="page"><h1>Readers, grouped by how they read</h1><p class="lede">Schedules change week to week, so each profile\'s booking button shows the real open times.</p>{rd}'
          f'<p class="small">If a reader is not listed, they are not taking bookings right now.</p></section>',
          crumbs=[('Home', '/'), ('Readers', '/readers/')])
    G.add('/decks/', f'Tarot Decks in Stock ({len(decks)}) | Namaste Tarot',
          'Tarot decks in stock at Namaste Tarot, with prices checked daily. Add to cart here; orders ship from New York City.',
          f'<section class="page"><h1>Tarot decks in stock</h1><p class="lede">Our tarot shelf. The list and prices update every morning; anything that sells out drops off.</p>'
          f'<ul class="grid">' + ''.join(card(x, 'decks') for x in decks) + '</ul>'
          f'<p class="small">Add decks to your cart and check out when you are ready. Shipping and tax are shown at checkout.</p></section>',
          ld=[G.product_ld(decks, 'Tarot decks in stock')], crumbs=[('Home', '/'), ('Decks', '/decks/')])
    G.add('/reading-table/', 'Tarot Pouches, Talismans & Card Boxes | Namaste Tarot',
          'Velvet tarot pouches, Lo Scarabeo tarot talismans, a card holder and small wooden boxes for keeping a deck, from Namaste Tarot.',
          f'<section class="page"><h1>For the reading table</h1><p class="lede">Small things that sit around a deck: a pouch to carry it, a box to keep it, a holder to stand a card up while you think about it.</p>'
          f'<ul class="grid">' + ''.join(card(x, 'table') for x in table) + '</ul>'
          f'<p class="small">Sizes are in each product name. None of these is needed to read tarot; they just keep the cards in good shape.</p></section>',
          ld=[G.product_ld(table, 'Tarot reading-table accessories')], crumbs=[('Home', '/'), ('Reading table', '/reading-table/')])
    G.add('/about/', 'About Namaste Tarot',
          'Namaste Tarot is a tarot reading and tarot goods brand on West 14th Street, Manhattan, operated by Wealth Edge Ventures Inc.',
          f'<section class="page"><h1>About Namaste Tarot</h1><p>Namaste Tarot gives tarot readings and sells tarot decks and reading-table goods. Readings happen at tables inside Namaste Bookshop, {G.ADDR}, near Union Square, '
          f'and in private rooms at 80 Fifth Avenue, Suite 1104.</p><p>Wealth Edge Ventures Inc. runs Namaste Tarot; Namaste Bookshop, the same company\'s shop, packs and ships our orders. '
          f'Our reader pages draw on what each reader publishes about themselves, and product prices are checked every day.</p>'
          f'<h2>Contact</h2><p><a href="tel:{G.TEL}">{G.PHONE}</a> &middot; <a href="mailto:{G.EMAIL}">{G.EMAIL}</a></p></section>',
          crumbs=[('Home', '/'), ('About', '/about/')])
    G.add('/privacy/', 'Privacy | Namaste Tarot', 'How namastetarot.com handles analytics, your cart, bookings and orders.',
          '<section class="page">' + G.privacy('namastetarot.com is a small information and shopping site. It has no accounts and no forms of its own.', products=True) + '</section>',
          crumbs=[('Home', '/'), ('Privacy', '/privacy/')])

NOTFOUND_DESC = 'That page is not on namastetarot.com.'
NOTFOUND = f'<section class="page"><h1>That card is not in this deck</h1><p>The page you wanted is not here. Try <a href="/readings/">readings</a>, <a href="/decks/">decks</a> or the <a href="/">home page</a>.</p></section>'

CSS = """:root{--ink:#2a1640;--gold:#d9a441;--paper:#fbf7ef;--soft:#efe6f5;--text:#2b2433;--accent:#2a1640;--onaccent:#fff;--onink:#fff;--body:Lora,Georgia,serif;--display:Cinzel,Georgia,serif;--btnr:99px;--r:10px;--line:#ddd3e8;--muted:#5d5566;--focus:#d9a441}
.mast{position:relative}.cartbtn{position:absolute;right:14px;top:14px;color:#fff;width:30px;height:30px;display:block}.cartbtn svg{width:28px;height:28px}.cartn{position:absolute;top:-6px;right:-8px;background:var(--gold);color:var(--ink);border-radius:99px;font:700 .7rem sans-serif;padding:2px 6px}
button.buy{border:0;cursor:pointer;font:inherit;font-weight:700;margin-top:6px}.ghost.sm{padding:2px 0;font-size:.85rem}
.rhead{display:flex;gap:16px;align-items:center}.rhead img{width:150px;height:150px;border-radius:50%;object-fit:cover;border:3px solid var(--gold);flex:none}.rhead h1{margin:0}p.svc{background:#fff;padding:12px 14px;border-radius:8px;border-left:4px solid var(--gold)}
.btn{display:inline-block;background:var(--ink);color:#fff;padding:13px 22px;border-radius:99px;text-decoration:none;font-weight:600;text-align:center}.ccheck{display:block}
.prod{display:grid;gap:22px}@media(min-width:760px){.prod{grid-template-columns:1fr 1fr;align-items:start}}.pimg img{width:100%;height:auto;background:#fff;border-radius:12px;object-fit:contain}.price.big{font-size:1.4rem}button.pill{border:0;cursor:pointer;font:inherit;font-weight:600}.facts{padding-left:1.1em}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--text);font:17px/1.65 Lora,Georgia,serif;padding-bottom:64px}
a{color:#6a3c96}h1,h2,h3{font-family:Cinzel,Georgia,serif;color:var(--ink);line-height:1.2}h1{font-size:clamp(1.8rem,6vw,2.8rem);margin:.3em 0}
.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:#fff;padding:8px}
.mast{background:var(--ink);color:#fff;text-align:center;padding:14px 12px 0}.seal{display:inline-flex;align-items:center;gap:10px;color:#fff;text-decoration:none;font:700 1.3rem Cinzel,serif;letter-spacing:.06em}
.seal svg{width:34px;height:34px;color:var(--gold)}.seal b{color:var(--gold)}
.menu{display:flex;gap:4px;overflow-x:auto;justify-content:flex-start;padding:10px 0 12px;scrollbar-width:none}.menu a{color:#eadff5;text-decoration:none;padding:6px 12px;border-radius:99px;font-size:.92rem;white-space:nowrap}
.menu a[aria-current]{background:var(--gold);color:var(--ink)}
main{max-width:1060px;margin:0 auto;padding:0 16px}
.hero{padding:28px 0 8px}.arch{background:linear-gradient(180deg,var(--soft),#fff);border:2px solid var(--gold);border-radius:200px 200px 18px 18px;padding:56px 22px 30px;text-align:center}
.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:.75rem;color:#7d5c18}.lede{font-size:1.08rem;max-width:620px;margin:0 auto 1em}
.page .lede{margin:0 0 1em}
.pill{display:inline-block;background:var(--ink);color:#fff;padding:9px 16px;border-radius:99px;text-decoration:none;font-weight:600;font-size:.92rem}.pill.big{padding:13px 22px;font-size:1rem}
.ghost{display:inline-block;padding:9px 14px;color:var(--ink);font-weight:600}
.trio{display:grid;gap:14px;margin:26px 0}.trio article{background:#fff;border-top:4px solid var(--gold);padding:16px 18px;border-radius:8px;box-shadow:0 1px 3px #0001}
@media(min-width:760px){.trio{grid-template-columns:repeat(3,1fr)}}
.band h2,.note h2{text-align:center}.grid{list-style:none;padding:0;display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
@media(min-width:700px){.grid{grid-template-columns:repeat(4,1fr)}}
.pc{background:#fff;border-radius:10px;padding:10px;display:flex;flex-direction:column;box-shadow:0 1px 3px #0001}.pc img{width:100%;height:auto;aspect-ratio:1;object-fit:contain}
.pc h3{font:600 .88rem/1.35 Lora,serif;margin:.5em 0;flex:1}.price{margin:0 0 .5em;font-weight:600}.buy{background:var(--gold);color:var(--ink);text-align:center;padding:8px;border-radius:8px;text-decoration:none;font-weight:700}
.more{text-align:center}.note{background:var(--ink);color:#efe6f5;border-radius:14px;padding:20px;margin:28px 0}.note h2{color:var(--gold)}.note a{color:var(--gold)}
.rlist{list-style:none;padding:0;display:grid;gap:12px}@media(min-width:760px){.rlist{grid-template-columns:1fr 1fr}}
.rc{display:flex;gap:14px;background:#fff;border-radius:12px;padding:14px;border-left:4px solid var(--gold)}.rc img{border-radius:50%;object-fit:cover;flex:none}.rc h3{margin:0 0 .2em;font-size:1.05rem}.rc p{margin:.2em 0}.from{font-weight:600;color:#7d5c18}
.len{border-collapse:collapse;width:100%}.len td,.len th{border-bottom:1px solid #ddd3e8;padding:8px;text-align:left}.steps li{margin:.4em 0}
.faq dt{font-weight:600;margin-top:1em;color:var(--ink)}.faq dd{margin:.2em 0 0}.small{font-size:.88rem;color:#5d5566}
.foot{background:#1d0f2e;color:#d9cfe6;display:grid;gap:18px;padding:28px 18px;margin-top:36px}.foot a{color:var(--gold)}@media(min-width:760px){.foot{grid-template-columns:repeat(3,1fr);padding:32px 6vw}}
.dock{position:fixed;bottom:0;left:0;right:0;display:flex;background:var(--ink);z-index:9}.dock a{flex:1;text-align:center;color:#fff;padding:14px;text-decoration:none;font-weight:600}.dock a:first-child{background:var(--gold);color:var(--ink)}
@media(min-width:900px){.dock{display:none}body{padding-bottom:0}.menu{justify-content:center}}
"""
