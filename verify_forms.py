
import time
from playwright.sync_api import sync_playwright, expect

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        try:
            time.sleep(10)  # Give the server a moment to start
            page.goto("http://localhost:8501")

            # --- 1. Verify Registration Page ---
            page.get_by_text("Register", exact=True).click()
            expect(page.get_by_text("Create New Account")).to_be_visible()

            # Check for required field indicators
            expect(page.get_by_text("Username *")).to_be_visible()
            expect(page.get_by_text("Email *")).to_be_visible()
            expect(page.get_by_text("Password *", exact=True)).to_be_visible()
            expect(page.get_by_text("Confirm Password *")).to_be_visible()
            expect(page.locator(".caption-text")).to_be_visible()

            # Test validation by submitting empty form
            page.get_by_role("button", name="Register").click()
            expect(page.get_by_text("Please fill in all required fields.")).to_be_visible()
            print("✅ Registration form verification successful.")

            # --- 2. Verify Login Page ---
            page.get_by_text("Login", exact=True).click()
            expect(page.get_by_text("Login to Your Account")).to_be_visible()

            # Check for required field indicators
            expect(page.get_by_text("Username *")).to_be_visible()
            expect(page.get_by_text("Password *")).to_be_visible()
            expect(page.locator(".caption-text")).to_be_visible()

            # Test validation
            page.get_by_role("button", name="Login").click()
            expect(page.get_by_text("Please fill in all required fields.")).to_be_visible()
            print("✅ Login form verification successful.")

            # --- 3. Log in and Verify Add Mood Page ---
            page.get_by_label("Username *").fill("testuser")
            page.get_by_label("Password *").fill("password")
            page.get_by_role("button", name="Login").click()

            # Wait for navigation to Dashboard
            expect(page.get_by_text("Your Mood Dashboard")).to_be_visible()

            page.get_by_text("Add Mood", exact=True).click()
            expect(page.get_by_text("Record Your Current Mood")).to_be_visible()

            # Check for required field indicator
            expect(page.get_by_text("Location (e.g., Library, Cafeteria) *")).to_be_visible()
            expect(page.locator(".caption-text")).to_be_visible()

            # Test validation
            page.get_by_role("button", name="Submit Mood Entry").click()
            expect(page.get_by_text("Please fill in all required fields.")).to_be_visible()
            print("✅ Add Mood form verification successful.")

            # --- 4. Take Screenshot ---
            page.screenshot(path="form_verification.png")
            print("📸 Screenshot captured: form_verification.png")

        finally:
            browser.close()

if __name__ == "__main__":
    run_verification()
