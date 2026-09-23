from playwright.sync_api import Page, expect

def test_product_search_fat_flow(page: Page, products_page):
    products_page.search_and_verify_product("Blue Top", expected_count=1)

def test_add_products_from_all_categories_and_checkout(page: Page, products_page):
    # 1. Women Category (Dress)
    products_page.add_product_from_category(
        category="women", 
        subcategory_locator="#Women a[href='/category_products/1']"
    )
    
    # 2. Men Category (Tshirts)
    products_page.add_product_from_category(
        category="men", 
        subcategory_locator="#Men a[href='/category_products/3']"
    )
    
    # 3. Kids Category (Tops & Shirts)
    products_page.add_product_from_category(
        category="kids", 
        subcategory_locator="#Kids a[href='/category_products/4']"
    )
    
    # 4. View Cart, Verify count, and take screenshot
    products_page.view_cart(screenshot_path="screenshots/final_cart_summary.png")
    expect(page.locator("#cart_info_table tbody tr")).to_have_count(3)
    
    # 5. Proceed to Checkout
    products_page.proceed_to_checkout()
    
    # Note: On Automation Exercise, clicking checkout while logged out triggers a modal 
    # prompting you to register/login. You can assert that modal or heading appears:
    expect(page.locator("u:text('Register / Login')")).to_be_visible()