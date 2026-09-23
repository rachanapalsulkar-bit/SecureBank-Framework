from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.products_menu = page.locator(".shop-menu a[href='/products']")
        
        # Categories
        self.women_category = page.locator("a[href='#Women']")
        self.men_category = page.locator("a[href='#Men']")
        self.kids_category = page.locator("a[href='#Kids']")
        
        # Search elements
        self.search_input = page.locator("#search_product")
        self.search_btn = page.locator("#submit_search")
        self.product_items = page.locator(".product-image-wrapper")
        
        # Cart & Checkout actions
        self.add_to_cart_btn = page.locator(".productinfo .add-to-cart").first
        self.continue_shopping_btn = page.locator("button.btn-success:text('Continue Shopping')")
        self.cart_menu = page.locator(".shop-menu a[href='/view_cart']")
        self.checkout_btn = page.locator(".check_out")
        self.checkout_modal = page.locator("#checkoutModal") # Appears if user is not logged in

    def search_and_verify_product(self, product_name: str, expected_count: int = 1):
        self.products_menu.click()
        expect(self.page).to_have_url("https://automationexercise.com/products")
        
        self.search_input.fill(product_name)
        self.search_btn.click()
        expect(self.product_items).to_have_count(expected_count)
        self.page.screenshot(path=screenshot_path, full_page=True)

    def add_product_from_category(self, category: str, subcategory_locator: str):
        self.products_menu.click()
        expect(self.page).to_have_url("https://automationexercise.com/products")
        
        if category.lower() == "women":
            self.women_category.click()
        elif category.lower() == "men":
            self.men_category.click()
        elif category.lower() == "kids":
            self.kids_category.click()
        else:
            raise ValueError(f"Invalid category: {category}")
            
        self.page.locator(subcategory_locator).click()
        
        product_card = self.product_items.first
        product_card.hover()
        self.add_to_cart_btn.click()
        
        expect(self.continue_shopping_btn).to_be_visible()
        self.continue_shopping_btn.click()

    def view_cart(self, screenshot_path: str = "screenshots/final_cart.png"):
        self.cart_menu.click()
        expect(self.page).to_have_url("https://automationexercise.com/view_cart")
        self.page.screenshot(path=screenshot_path, full_page=True)

    def proceed_to_checkout(self):

        self.checkout_btn.click()