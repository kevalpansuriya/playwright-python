import logging
import re

from playwright.sync_api import Page, expect

from test_flipkart_login.locators import FlipKartLocator

log = logging.getLogger(__name__)
url = "https://www.flipkart.com/"


def test_has_title(page: Page) -> None:
    """
    Tests if the page has the title.
    :param page:
    :return:
    """
    page.goto(url)
    page.wait_for_url(url=url)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile(FlipKartLocator.TITLE))


def test_get_started_link(page: Page) -> None:
    """
    Tests if the page has the started link.
    :param page:
    :return:
    """
    page.goto(url)
    page.wait_for_url(url=url)

    # click the get started link.
    # page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.locator(FlipKartLocator.LOGO)).to_be_visible()
    page.locator(FlipKartLocator.SEARCH_BUTTON).fill("toys")
