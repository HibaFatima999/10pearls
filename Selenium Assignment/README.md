# Selenium Assignment – Daraz Search & Shipping Test

##Overview
This project is an automated **Selenium Python test** that:
1. Opens the Daraz website.
2. Searches for "electronics".
3. Filters products by a specific brand (case-insensitive).
4. Applies a price range filter (500 – 5000).
5. Counts the number of matching products.
6. Opens the first product in the results.
7. Checks if **free shipping** is available for that product.

The framework uses the **Page Object Model (POM)** for clean separation between test steps and page interactions.
---
## 📂 Project Structure
Selenium Assignment/
├── venv/                              # Virtual environment folder
├── src/
│   ├── pages/
│   │   ├── base_page.py               # Base page class with common Selenium actions
│   │   ├── home_page.py               # Methods for interacting with Daraz homepage
│   │   ├── search_results_page.py     # Methods for filtering & interacting with search results
│   │   └── product_page.py            # Methods for product details page
│   └── tests/
│       └── test_search_and_shipping.py # Main test script
├── conftest.py                        # Pytest fixtures (driver setup & teardown)
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Files and folders to ignore in Git
└── README.md                          # Project documentation


## NOTE TO READ BEFORE RUNNING THE PROJECT
All project files eg. (venv) etc. are not uploaded on github because it contains further folders and files in it like site packages that are large in number and causing difficulty while uploading.
So before running the project some dependencies/site-packages needs to be regeneraed or installed explicitely to align it with the given project.

This test relies on HTML structure, CSS selectors, and element attributes from the Daraz website.
If Daraz updates its:
HTML element structure
Class names or IDs
XPaths or CSS selectors
Page flow or navigation
then the locators in our POM classes may break, causing:
-Element not found errors (NoSuchElementException)
-Failing steps in filtering, price setting, or product opening
-Incorrect product counts or failure to detect free shipping

Solution if this happens:
-Reinspect the Daraz page using browser DevTools (F12).
-Update the element locators in:
  home_page.py
  search_results_page.py
  product_page.py
Keep locators as flexible as possible (avoid overly strict XPaths that may break easily).

## Prepared by:
**Hiba Fatima**  
QA Batch-05
