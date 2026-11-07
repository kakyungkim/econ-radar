# -*- coding: utf-8 -*-
"""collect_news.py 검사. 네트워크를 쓰지 않는다. 참값은 아래 고정 입력에 적어 둔다."""
import os, sys, datetime as dt

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))
import collect_news as cn

KST = dt.timezone(dt.timedelta(hours=9))

RSS = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0"><channel><title>t</title>
<item><title>  Fed holds   rates </title><link>https://ex.com/a?utm_source=x&amp;id=1</link>
<pubDate>Thu, 06 Nov 2026 03:00:00 GMT</pubDate><description>&lt;p&gt;Rates &lt;b&gt;steady&lt;/b&gt;.&lt;/p&gt;</description></item>
<item><title>Old story</title><link>https://ex.com/old</link><pubDate>Mon, 02 Nov 2026 03:00:00 GMT</pubDate></item>
<item><title>No date</title><link>https://ex.com/nodate</link></item>
<item><title>KST stamp</title><link>https://ex.com/k</link><pubDate>Thu, 06 Nov 2026 17:30:00 +0900</pubDate></item>
</channel></rss>"""

ATOM = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"><title>AI</title>
<entry><title>Model launch</title><link rel="alternate" href="https://ex.com/m1"/>
<updated>2026-11-06T05:00:00+00:00</updated><summary>New &amp;amp; shiny</summary></entry>
<entry><title>Too late</title><link href="https://ex.com/m2"/><published>2026-11-06T10:00:00Z</published></entry>
</feed>"""

END = dt.datetime(2026, 11, 6, 18, 0, tzinfo=KST)


def test_parse_rss_normalizes():
    items = cn.parse_feed(RSS.encode(), "Fed", "en", "macro")
    assert len(items) == 4
    a = items[0]
    assert a["title"] == "Fed holds rates"
    assert a["source"] == "Fed" and a["lang"] == "en" and a["section"] == "macro"
    assert a["summary"] == "Rates steady."
    assert a["published"].utcoffset() == dt.timedelta(0) or a["published"].tzinfo is not None
    assert a["published"].astimezone(KST).hour == 12  # 03:00Z = 12:00 KST
    assert items[2]["published"] is None


def test_parse_atom():
    items = cn.parse_feed(ATOM.encode(), "AI", "en", "ai")
    assert [i["url"] for i in items] == ["https://ex.com/m1", "https://ex.com/m2"]
    assert items[0]["summary"] == "New & shiny"
    assert items[0]["published"].astimezone(KST).hour == 14


def test_window_filter_handles_timezones():
    items = cn.parse_feed(RSS.encode(), "Fed", "en", "macro") + cn.parse_feed(ATOM.encode(), "AI", "en", "ai")
    kept = cn.filter_window(items, END, 30)
    titles = sorted(i["title"] for i in kept)
    # 창: 11-05 12:00 ~ 11-06 18:00 KST. Old story, No date, Too late(19:00 KST) 제외
    assert titles == ["Fed holds rates", "KST stamp", "Model launch"]


def test_canonical_url_strips_tracking():
    assert cn.canonical_url("https://ex.com/a?utm_source=x&id=1#frag") == "https://ex.com/a?id=1"
    assert cn.canonical_url("HTTP://Ex.com/a/") == "http://ex.com/a"


def test_dedupe_by_url_and_title():
    def it(t, u, s="macro"):
        return {"title": t, "url": u, "section": s, "published": END}
    items = [it("Same Story", "https://a.com/1?utm_medium=z"), it("Other", "https://a.com/1"),
             it("same   story", "https://b.com/2"), it("Different", "https://b.com/3")]
    out = cn.dedupe(items)
    assert [i["title"] for i in out] == ["Same Story", "Different"]


def test_fetch_priority_bio_ai_korea_first_then_recency():
    def it(s, h):
        return {"title": f"{s}{h}", "url": f"https://x/{s}{h}", "section": s,
                "published": END - dt.timedelta(hours=h)}
    items = [it("markets", 1), it("macro", 2), it("bio", 20), it("ai", 10), it("korea", 5), it("bio", 3)]
    order = [i["title"] for i in cn.pick_for_fetch(items, 4)]
    assert order == ["bio3", "korea5", "ai10", "bio20"]


FIXTURE_HTML = """<html><head><script>var x=1;</script><style>p{}</style></head><body>
<nav><p>Home menu</p></nav>
<article><h1>Title</h1>
<p>Short.</p>
<p>The central bank left its benchmark rate unchanged on Thursday, citing resilient hiring data.</p>
<p>Analysts had expected a hold, and markets barely moved after the statement was released today.</p>
</article><footer><p>Copyright boilerplate that is long enough to pass the forty char filter easily.</p></footer>
</body></html>"""


def test_html_to_text_prefers_article_and_drops_short():
    t = cn.html_to_text(FIXTURE_HTML)
    assert "central bank left its benchmark rate" in t
    assert "Short." not in t and "Home menu" not in t and "Copyright" not in t and "var x" not in t


def test_html_to_text_without_article_and_limit():
    html = "<html><body><p>" + "가나다라마바사 " * 40 + "</p></body></html>"
    assert len(cn.html_to_text(html, limit=100)) <= 100


def test_text_status():
    assert cn.text_status("") == "blocked"
    assert cn.text_status("x" * 100) == "short"
    assert cn.text_status("x" * 500) == "ok"


def test_render_md_contains_source_kst_url():
    item = {"title": "Fed holds rates", "source": "Fed", "lang": "en", "section": "macro",
            "published": dt.datetime(2026, 11, 6, 3, 0, tzinfo=dt.timezone.utc),
            "url": "https://ex.com/a", "summary": "Rates steady.", "text": "본문" * 400, "text_status": "ok"}
    stats = {"Fed": {"fetched": 4, "kept": 1, "error": ""}, "Dead": {"fetched": 0, "kept": 0, "error": "curl 22"}}
    md = cn.render_md("2026-11-06", END - dt.timedelta(hours=30), END, stats, [item])
    assert "Fed" in md and "2026-11-06 12:00" in md and "https://ex.com/a" in md
    assert "Dead" in md and "curl 22" in md
    assert "Rates steady." in md
    assert "본문" * 300 in md and "본문" * 301 not in md  # 발췌 600자 제한


def test_interleave_keeps_every_feed_under_cap():
    def it(src, h):
        return {"title": f"{src}{h}", "url": f"https://x/{src}{h}", "source": src, "section": "macro",
                "published": END - dt.timedelta(hours=h)}
    items = [it("A", h) for h in range(1, 8)] + [it("B", 20)]
    top = cn.interleave(items)[:3]
    assert {i["source"] for i in top} == {"A", "B"}


def test_double_escaped_cdata_title_survives():
    x = ("<rss version='2.0'><channel><item><title>&lt;![CDATA[Drug works]]&gt;</title>"
         "<link>https://ex.com/c</link><pubDate>Thu, 06 Nov 2026 03:00:00 GMT</pubDate></item></channel></rss>")
    assert cn.parse_feed(x.encode(), "O", "en", "bio")[0]["title"] == "Drug works"
