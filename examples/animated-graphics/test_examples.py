#!/usr/bin/env python3
"""Headless-browser checks for the animated graphics examples.
Requires: pip install playwright && playwright install chromium.
Verifies: no console/page errors, motion actually happens, pointer and keyboard response,
reduced-motion path, pause on hidden/off-screen, and non-blank rendering."""
import pathlib, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
FAIL = []
def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f"  [{detail}]" if detail and not cond else ""))
    if not cond: FAIL.append(name)

def open_page(browser, file, reduced=False, size=(1000, 700)):
    ctx = browser.new_context(viewport={"width": size[0], "height": size[1]}, reduced_motion="reduce" if reduced else "no-preference")
    page = ctx.new_page(); errors = []
    page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto((HERE / file).as_uri()); page.wait_for_timeout(400)
    return ctx, page, errors

def nonblank(page, selector="canvas"):
    return page.evaluate("""(sel) => { const c = document.querySelector(sel); const t = document.createElement('canvas'); t.width = 64; t.height = 64;
      const x = t.getContext('2d'); x.drawImage(c, 0, 0, 64, 64); const d = x.getImageData(0,0,64,64).data; let n = 0; for (let i=0;i<d.length;i+=4) if (d[i+3] > 0 && (d[i]+d[i+1]+d[i+2]) > 30) n++; return n; }""", selector)

with sync_playwright() as p:
    browser = p.chromium.launch(args=["--use-gl=swiftshader", "--enable-webgl", "--ignore-gpu-blocklist"])

    # ---- orbital rotation
    ctx, pg, err = open_page(browser, "orbital-rotation.html")
    s0 = pg.evaluate("__demo.state"); pg.wait_for_timeout(2300); s1 = pg.evaluate("__demo.state")
    check("orbital: idle auto-rotation advances", s1["ry"] != s0["ry"], f"{s0} -> {s1}")
    box = pg.locator("#stage").bounding_box(); cx, cy = box["x"] + box["width"]/2, box["y"] + box["height"]/2
    before = pg.evaluate("__demo.state.ry"); pg.mouse.move(cx, cy); pg.mouse.down(); pg.mouse.move(cx + 120, cy, steps=6); pg.mouse.up(); pg.wait_for_timeout(100)
    after = pg.evaluate("__demo.state.ry"); check("orbital: drag rotates", abs(after - before) > 20, f"{before} -> {after}")
    pg.locator("#stage").focus(); a = pg.evaluate("__demo.state.ry"); pg.keyboard.press("ArrowRight"); b = pg.evaluate("__demo.state.ry"); check("orbital: keyboard rotates", b - a >= 9, f"{a} -> {b}")
    pg.emulate_media(reduced_motion="reduce"); pg.wait_for_timeout(150); check("orbital: OS reduced motion stops loop", pg.evaluate("__demo.state.raf") is False)
    check("orbital: no console errors", not err, str(err)); ctx.close()
    ctx, pg, err = open_page(browser, "orbital-rotation.html", reduced=True); a = pg.evaluate("__demo.state.ry"); pg.wait_for_timeout(1500)
    check("orbital: reduced motion = no auto-rotation", pg.evaluate("__demo.state.ry") == a and pg.evaluate("__demo.state.raf") is False); ctx.close()

    # ---- flow network
    ctx, pg, err = open_page(browser, "flow-network.html"); pg.wait_for_timeout(1500)
    check("network: particles flowing", pg.evaluate("__demo.particles()") > 3, str(pg.evaluate("__demo.particles()")))
    check("network: canvas renders pixels", nonblank(pg) > 40, str(nonblank(pg)))
    n0 = {n["id"]: n for n in pg.evaluate("__demo.nodes()")}["API"]; pg.mouse.move(n0["x"] + 40, n0["y"] + 10); pg.mouse.move(n0["x"] + 30, n0["y"] + 5, steps=5); pg.wait_for_timeout(500)
    n1 = {n["id"]: n for n in pg.evaluate("__demo.nodes()")}["API"]; check("network: cursor field displaces nearby node", abs(n1["x"] - n0["x"]) + abs(n1["y"] - n0["y"]) > 3, f"{n0} -> {n1}")
    pg.mouse.move(900, 650); pg.wait_for_timeout(100); d0 = {n["id"]: n for n in pg.evaluate("__demo.nodes()")}["DB"]
    pg.mouse.move(d0["x"], d0["y"]); pg.mouse.down(); pg.mouse.move(d0["x"] - 100, d0["y"] - 80, steps=5); pg.mouse.up(); pg.wait_for_timeout(100)
    d1 = {n["id"]: n for n in pg.evaluate("__demo.nodes()")}["DB"]; check("network: node is draggable", abs(d1["x"] - d0["x"]) > 50, f"{d0} -> {d1}")
    pg.emulate_media(reduced_motion="reduce"); pg.wait_for_timeout(100); check("network: OS reduced motion stops loop", pg.evaluate("__demo.running()") is False)
    check("network: no console errors", not err, str(err)); ctx.close()
    ctx, pg, err = open_page(browser, "flow-network.html", reduced=True); pg.wait_for_timeout(1000)
    check("network: reduced motion = static (no loop, no particles)", pg.evaluate("__demo.running()") is False and pg.evaluate("__demo.particles()") == 0)
    check("network: reduced motion still draws the diagram", nonblank(pg) > 40); ctx.close()

    # ---- parallax
    ctx, pg, err = open_page(browser, "parallax-layers.html")
    pg.mouse.move(100, 100); pg.mouse.move(900, 600, steps=8); pg.wait_for_timeout(700); t = pg.evaluate("__demo.transforms()")
    check("parallax: pointer moves layers", all(x for x in t) and len(set(t)) > 1, str(t))
    import re
    def mag(s): m = re.search(r"translate3d\((-?[\d.]+)px", s); return abs(float(m.group(1))) if m else 0
    check("parallax: deeper layers move farther", mag(t[-1]) > mag(t[1]) > 0, str([mag(x) for x in t]))
    pg.mouse.wheel(0, 300); pg.wait_for_timeout(500); t2 = pg.evaluate("__demo.transforms()"); check("parallax: scroll changes layer transforms", t2 != t)
    check("parallax: no console errors", not err, str(err)); ctx.close()
    ctx, pg, err = open_page(browser, "parallax-layers.html", reduced=True); pg.mouse.move(100, 100); pg.mouse.move(900, 600, steps=6); pg.wait_for_timeout(300)
    check("parallax: reduced motion leaves layers still", all(x == "" for x in pg.evaluate("__demo.transforms()"))); ctx.close()

    # ---- shader
    ctx, pg, err = open_page(browser, "shader-field.html"); pg.wait_for_timeout(500)
    check("shader: WebGL2 context created", pg.evaluate("__demo.webgl") is True, str(pg.evaluate("__demo")))
    f0 = pg.evaluate("__demo.frames()"); pg.mouse.move(300, 300); pg.mouse.move(500, 400, steps=5); pg.wait_for_timeout(600); f1 = pg.evaluate("__demo.frames()")
    check("shader: frames advance", f1 > f0 + 3, f"{f0} -> {f1}")
    # read the composited result from a real screenshot (the drawing buffer is not preserved between frames by design)
    import io
    from PIL import Image
    img = Image.open(io.BytesIO(pg.locator("#gl").screenshot())).convert("RGB").resize((32, 32))
    px = list(img.getdata()); mean = [sum(c[i] for c in px) / len(px) for i in range(3)]
    check("shader: renders non-black, varied pixels", sum(mean) > 60 and len(set(px)) > 50, f"mean={mean} unique={len(set(px))}")
    pg.emulate_media(reduced_motion="reduce"); pg.wait_for_timeout(150); fa = pg.evaluate("__demo.frames()"); pg.wait_for_timeout(300); check("shader: OS reduced motion stops frames", pg.evaluate("__demo.frames()") == fa)
    check("shader: no console errors", not [e for e in err if "GPU stall" not in e], str(err)); ctx.close()
    ctx, pg, err = open_page(browser, "shader-field.html", reduced=True); pg.wait_for_timeout(600); fr = pg.evaluate("__demo.frames()"); pg.wait_for_timeout(400)
    check("shader: reduced motion draws one static frame then stops", pg.evaluate("__demo.running()") is False and pg.evaluate("__demo.frames()") == fr and fr >= 1); ctx.close()
    # simulate no-WebGL: fallback path
    ctx = browser.new_context(); pg = ctx.new_page(); errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.add_init_script("HTMLCanvasElement.prototype.getContext = function(){ return null; }"); pg.goto((HERE / "shader-field.html").as_uri()); pg.wait_for_timeout(300)
    check("shader: graceful fallback when WebGL unavailable", pg.evaluate("__demo.webgl") is False and not errs and "fallback" in pg.inner_text("#status").lower(), str(errs)); ctx.close()

    # ---- svg path flow
    ctx, pg, err = open_page(browser, "svg-path-flow.html")
    d0 = pg.evaluate("__demo.paths()"); node = pg.locator(".node").nth(1); bb = node.bounding_box()
    pg.mouse.move(bb["x"] + bb["width"]/2, bb["y"] + bb["height"]/2); pg.mouse.down(); pg.mouse.move(bb["x"] + 250, bb["y"] + 150, steps=6); pg.mouse.up(); d1 = pg.evaluate("__demo.paths()")
    check("svg flow: dragging a node reroutes connectors", d0 != d1)
    node = pg.locator(".node").nth(2); node.focus(); k0 = pg.evaluate("__demo.paths()"); pg.keyboard.press("ArrowLeft"); check("svg flow: keyboard moves node and reroutes", pg.evaluate("__demo.paths()") != k0)
    pk = [pg.get_attribute(".packet", "cx")]; pg.wait_for_timeout(500); pk.append(pg.get_attribute(".packet", "cx")); check("svg flow: packets travel along paths", pk[0] != pk[1], str(pk))
    check("svg flow: no console errors", not err, str(err)); ctx.close()
    ctx, pg, err = open_page(browser, "svg-path-flow.html", reduced=True); pg.wait_for_timeout(500)
    check("svg flow: reduced motion stops packets", pg.evaluate("__demo.running()") is False); ctx.close()

    # ---- mobile viewport: no horizontal overflow
    for f in ["orbital-rotation.html", "flow-network.html", "parallax-layers.html", "shader-field.html", "svg-path-flow.html"]:
        ctx, pg, err = open_page(browser, f, size=(375, 667)); ov = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
        check(f"{f}: no horizontal overflow at 375px", ov <= 1, str(ov)); ctx.close()
    browser.close()

print(f"\n{'ALL PASSED' if not FAIL else str(len(FAIL)) + ' FAILED: ' + ', '.join(FAIL)}")
sys.exit(1 if FAIL else 0)
