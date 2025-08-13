# src/pages/search_results_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class SearchResultsPage(BasePage):
    # Price inputs (placeholders can vary)
    MIN_PRICE_INPUTS = [
        (By.CSS_SELECTOR, "input[placeholder='Min']"),
        (By.CSS_SELECTOR, "input[aria-label*='Min']"),
        (By.XPATH, "//input[contains(@placeholder,'Min')]")
    ]
    MAX_PRICE_INPUTS = [
        (By.CSS_SELECTOR, "input[placeholder='Max']"),
        (By.CSS_SELECTOR, "input[aria-label*='Max']"),
        (By.XPATH, "//input[contains(@placeholder,'Max')]")
    ]
    PRICE_APPLY_BUTTONS = [
        (By.CSS_SELECTOR, "button[class*='price-go']"),
        (By.XPATH, "//button[contains(., 'Go') or contains(., 'Apply')]")
    ]

    # Brand search input & brand checkbox fallback
    BRAND_SEARCH_INPUTS = [
        (By.CSS_SELECTOR, "input[placeholder*='Search brand']"),
        (By.CSS_SELECTOR, "input[placeholder*='Search']"),
        (By.XPATH, "//input[contains(@placeholder, 'Search')]")
    ]
    # Updated: case-insensitive checkbox match
    BRAND_CHECKBOX_TEMPLATE = lambda brand: (
        By.XPATH,
        f"//label[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), '{brand.lower()}')]//input[@type='checkbox']"
    )

    # Product item locators (several fallbacks)
    PRODUCT_ITEMS_LOCATORS = [
        (By.CSS_SELECTOR, "div[data-qa-locator='product-item']"),
        (By.CSS_SELECTOR, "div.box--ujueT"),  # older daraz class
        (By.CSS_SELECTOR, "div.sku")  # fallback
    ]

    def _find_first_visible(self, locators):
        for loc in locators:
            try:
                elems = self.driver.find_elements(*loc)
                if elems and len(elems) > 0:
                    return loc
            except Exception:
                continue
        raise TimeoutException("No locator matched from provided list")

    def set_price_filter(self, min_price, max_price):
        min_loc = self._find_first_visible(self.MIN_PRICE_INPUTS)
        max_loc = self._find_first_visible(self.MAX_PRICE_INPUTS)

        min_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(min_loc))
        min_input.clear()
        min_input.send_keys(str(min_price))

        max_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(max_loc))
        max_input.clear()
        max_input.send_keys(str(max_price))

        for loc in self.PRICE_APPLY_BUTTONS:
            try:
                self.click(loc)
                return
            except Exception:
                continue
        max_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def filter_by_brand(self, brand_name):
        """
        Filters search results by brand, case-insensitively.
        """
        for loc in self.BRAND_SEARCH_INPUTS:
            try:
                inp = WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(loc))
                try:
                    inp.clear()
                    inp.send_keys(brand_name)
                    time.sleep(1)
                except Exception:
                    pass

                # Updated: case-insensitive checkbox matching
                checkbox = (
                    By.XPATH,
                    f"//label[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), '{brand_name.lower()}')]//input[@type='checkbox']"
                )
                try:
                    el = WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable(checkbox))
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
                    el.click()
                    return
                except Exception:
                    # Try label click fallback
                    try:
                        label = WebDriverWait(self.driver, 4).until(
                            EC.element_to_be_clickable((
                                By.XPATH,
                                f"//label[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), '{brand_name.lower()}')]"
                            ))
                        )
                        label.click()
                        return
                    except Exception:
                        continue
            except Exception:
                continue

        # Last fallback
        try:
            fallback = (
                By.XPATH,
                f"//label[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), '{brand_name.lower()}')]"
            )
            self.click(fallback)
        except Exception:
            pass  # Continue without brand filter if it fails

    def get_products_count(self):
        for loc in self.PRODUCT_ITEMS_LOCATORS:
            try:
                elems = self.driver.find_elements(*loc)
                if elems and len(elems) > 0:
                    return len(elems)
            except Exception:
                continue
        elems = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/product/'], a[title]")
        return len(elems)

    def click_first_product(self):
        for loc in self.PRODUCT_ITEMS_LOCATORS:
            try:
                elems = self.driver.find_elements(*loc)
                if elems and len(elems) > 0:
                    first = elems[0]
                    try:
                        link = first.find_element(By.TAG_NAME, "a")
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
                        link.click()
                        return
                    except Exception:
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", first)
                        first.click()
                        return
            except Exception:
                continue
        links = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/product/'], a[data-tracking]")
        if links:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", links[0])
            links[0].click()
            return
        raise Exception("No product found to click")
