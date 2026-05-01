from playwright.sync_api import sync_playwright
import time

USERNAME = "testuser12345"
EMAIL = "lejobin488@kynninc.com"
PASSWORD = "Nanu@2005"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # ------------------------
        # SIGNUP
        # ------------------------
        page.goto("https://www.city-data.com/forum/register.php")

        if page.locator("text=I agree").count() > 0:
            page.click("text=I agree")

        page.fill("input[name='username']", USERNAME)
        page.fill("input[name='email']", EMAIL)
        page.fill("input[name='password']", PASSWORD)
        page.fill("input[name='passwordconfirm']", PASSWORD)

        page.click("input[type='submit']")

        print("Signup submitted")

        # ⚠️ MANUAL STEP REQUIRED
        input("👉 Verify email manually, then press ENTER...")

        # ------------------------
        # LOGIN
        # ------------------------
        page.goto("https://www.city-data.com/forum/login.php")

        page.fill("input[name='vb_login_username']", USERNAME)
        page.fill("input[name='vb_login_password']", PASSWORD)
        page.click("input[type='submit']")

        print("Logged in")

        # ------------------------
        # POSTING
        # ------------------------
        page.goto("https://www.city-data.com/forum/general-u-s/")

        page.click("text=Post New Thread")

        page.fill("input[name='subject']", "Automation Test Post")
        page.fill("textarea", "This post is created using Playwright.")

        page.click("input[type='submit']")

        print("Post submitted")

        time.sleep(5)
        browser.close()

run()