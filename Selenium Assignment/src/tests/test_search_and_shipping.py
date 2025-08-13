# src/tests/test_search_and_shipping.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage
from src.pages.product_page import ProductPage


@pytest.mark.usefixtures("driver")
class TestDarazSearchAndShipping:

    def test_search_filter_count_and_free_shipping(self, driver):
        wait = WebDriverWait(driver, 15)

        home = HomePage(driver)
        results = SearchResultsPage(driver)

        # 1) Go to homepage and search
        home.go_to_homepage()
        home.search_item("electronics")

        # Wait until results are visible
        wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".info--ifj7U .title--wFj93")
        ))

        # 2) Select brand filter
        brand = "philips"  # lowercase (case-insensitive handled in page object)
        results.filter_by_brand(brand)

        # Wait for brand filter results to refresh
        wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".info--ifj7U .title--wFj93")
        ))

        # 3) Set price filter 500 - 5000
        results.set_price_filter(500, 5000)

        # Wait for price filter results to refresh
        wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".info--ifj7U .title--wFj93")
        ))

        # 4) Count products
        count = results.get_products_count()
        assert count > 0, f"Expected > 0 products after filters, got {count}"

        # 5) Click first product
        results.click_first_product()

        # Handle possible new tab
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])

        # 6) Check free shipping
        product = ProductPage(driver)
        has_free = product.is_free_shipping_available()
        assert has_free, "Free shipping not available for this product."
