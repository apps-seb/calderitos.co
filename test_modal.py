import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={'width': 375, 'height': 812},
            device_scale_factor=2,
            is_mobile=True,
            has_touch=True
        )
        page = await context.new_page()
        file_path = f"file://{os.path.abspath('index.html')}"
        await page.goto(file_path)

        # Click the first dish card to open modal
        await page.click('.card')

        # Wait for the modal and ingredients to be visible and animations to complete
        await page.wait_for_selector('#dishModal.active')
        await page.wait_for_selector('.ingredient-item')
        await asyncio.sleep(1) # wait for animations

        await page.screenshot(path="/home/jules/verification/mobile_modal.png", full_page=True)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
