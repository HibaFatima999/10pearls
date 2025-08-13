# src/pages/home_page.py
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "q")  # typical Daraz search input id
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit'], a.search-box__button--1oH7")

    COOKIE_CLOSE_SELECTORS = [
        (By.CSS_SELECTOR, "button[data-cy='close-button']"),
        (By.CSS_SELECTOR, "button.cookie__close"),
        (By.CSS_SELECTOR, "button[aria-label='close']"),
    ]

    def go_to_homepage(self):
        self.driver.get("https://www.daraz.pk/")
        self.close_cookie_popup()

    def close_cookie_popup(self):
        for locator in self.COOKIE_CLOSE_SELECTORS:
            try:
                self.click(locator)
                return
            except TimeoutException:
                continue
        # no popup or couldn't find it; ignore

    def search_item(self, item_name):
        self.send_keys(self.SEARCH_INPUT, item_name)
        # click search button; fallback if not clickable
        try:
            self.click(self.SEARCH_BUTTON)
        except Exception:
            # press Enter as fallback
            self.find_element(self.SEARCH_INPUT).submit()
