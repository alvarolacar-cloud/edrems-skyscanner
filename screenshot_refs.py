from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1440, 'height': 900},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        )
        page = context.new_page()

        try:
            page.goto('https://www.booking.com', timeout=30000)
            page.wait_for_timeout(2000)
            page.screenshot(path='booking_desk.png')
        except Exception as e:
            print("Booking error:", e)

        try:
            page.goto('https://www.edreams.es', timeout=30000)
            page.wait_for_timeout(2000)
            page.screenshot(path='edreams_desk.png')
        except Exception as e:
            print("eDreams error:", e)

        browser.close()

if __name__ == "__main__":
    run()
