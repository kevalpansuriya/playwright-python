import re
from playwright.sync_api import Page, expect

from test_flipkart_login.locators import FlipKart

url = "https://www.flipkart.com/"


def test_has_title(page: Page):
    page.goto(url)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile(FlipKart.TITLE))


def test_get_started_link(page: Page):
    page.goto(url)

    # Click the get started link.
    # page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    page.locator(FlipKart.SEARCH_BUTTON).fill("toys")
    print(FlipKart.LOGO)


    #expect(page.locator(FlipKart.LOGO)).to_be_visible()
