import asyncio, sys, json
from playwright.async_api import async_playwright
BASE="http://127.0.0.1:8765"
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
        ctx = await b.new_context(viewport={"width":1400,"height":900}, device_scale_factor=1)
        await ctx.route("**/tiles.openfreemap.org/**", lambda r: r.abort())
        page = await ctx.new_page()
        logs=[]
        page.on("console", lambda m: logs.append(f"[{m.type}] {m.text}"))
        page.on("pageerror", lambda e: logs.append(f"[pageerror] {e}"))
        # 1. home map
        await page.goto(BASE+"/", wait_until="load")
        await page.wait_for_timeout(3500)
        await page.screenshot(path="shots/01_home.png")
        # 2. search + select
        await page.fill("input[type=search]", "ping an")
        await page.wait_for_timeout(500)
        await page.screenshot(path="shots/02_search.png")
        await page.keyboard.press("Enter")
        await page.wait_for_timeout(2500)
        await page.screenshot(path="shots/03_selected.png")
        url = page.url
        # 3. filters
        await page.click("text=Filters")
        await page.wait_for_timeout(400)
        await page.screenshot(path="shots/04_filters.png")
        # 4. tower page direct
        await page.goto(BASE+"/tower/burj-khalifa-3/", wait_until="load")
        await page.wait_for_timeout(3000)
        await page.screenshot(path="shots/05_tower_page.png")
        # 5. shared-point chooser: Wanda East Port Dalian
        await page.goto(BASE+"/tower/wanda-east-port-tower-1-9531/", wait_until="load")
        await page.wait_for_timeout(2500)
        html = await page.content()
        # 6. rankings + city page
        await page.goto(BASE+"/rankings/", wait_until="load"); await page.screenshot(path="shots/06_rankings.png", full_page=False)
        await page.goto(BASE+"/city/shenzhen/nanshan-district/", wait_until="load"); await page.screenshot(path="shots/07_district.png")
        # mobile
        m = await b.new_context(viewport={"width":390,"height":844}, device_scale_factor=2, is_mobile=True, has_touch=True)
        await m.route("**/tiles.openfreemap.org/**", lambda r: r.abort())
        mp = await m.new_page()
        await mp.goto(BASE+"/tower/burj-khalifa-3/", wait_until="load"); await mp.wait_for_timeout(3000)
        await mp.screenshot(path="shots/08_mobile_tower.png")
        print("selected url:", url)
        print("\n".join(l for l in logs if "tiles.openfreemap" not in l)[:3000])
        await b.close()
asyncio.run(main())
