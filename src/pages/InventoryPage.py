from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    BTN_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BTN_BIKELIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    BTN_CHECKOUT = (By.ID, "checkout")
    BTN_CONTINUE = (By.ID, "continue")
    BTN_FINISH = (By.ID, "finish")

    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_NUMBER = (By.CLASS_NAME, "shopping_cart_badge")
    
    INPUT_NAME = (By.ID, "first-name")
    INPUT_LAST = (By.ID, "last-name")
    INPUT_CODE = (By.ID, "postal-code")

    THANKS_MSG = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)

    def validateTitle(self):
        assert self.get_title() == "Swag Labs"
        self.wait_page()

    def addItemsToCart(self):
        self.click_element(self.BTN_BACKPACK)
        self.click_element(self.BTN_BIKELIGHT)
        self.wait_page()

    def goToCart(self):
        self.click_element(self.SHOPPING_CART_LINK)
        self.wait_page()

    def validateCartQuantity(self):
        number = self.get_element_text(self.SHOPPING_CART_NUMBER)
        return '2' in number

    def checkoutCart(self):
        self.click_element(self.BTN_CHECKOUT)
        self.wait_page()

    def validateCartUrl(self):
        url = self.driver.current_url
        return '/cart.html' in url

    def fillStepOneInfo(self, fname, lname, pcode):
        self.input_element(self.INPUT_NAME, fname)
        self.input_element(self.INPUT_LAST, lname)
        self.input_element(self.INPUT_CODE, pcode)
        self.wait_page()
        self.click_element(self.BTN_CONTINUE)
        self.wait_page()

    def finishCheckout(self):
        self.click_element(self.BTN_FINISH)
        self.wait_page()

    def validateMessage(self):
        msg = self.get_element_text(self.THANKS_MSG)
        return 'THANK YOU FOR YOUR ORDER' in msg
