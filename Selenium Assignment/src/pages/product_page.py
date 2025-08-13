# src/pages/product_page.py
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    # Some possible texts or labels for free shipping on product pages
    FREE_SHIPPING_XPATHS = [
        "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), 'free delivery')]",
        "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), 'free shipping')]",
        "//span[contains(., 'Free Delivery') or contains(., 'Free Shipping')]",
    ]

    def is_free_shipping_available(self):
        # Wait for product page to load key element (title)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//title|//h1|//h2"))
            )
        except Exception:
            pass

        for xp in self.FREE_SHIPPING_XPATHS:
            try:
                el = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xp)))
                if el and el.is_displayed():
                    return True
            except TimeoutException:
                continue
            except Exception:
                continue
        # Not found
        return False
