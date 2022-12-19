from behave import *
from selenium import webdriver
from src.utils.config import TestUtils
from src.pages.loginPage import LoginPage
from src.pages.InventoryPage import InventoryPage

@given(u'I am on the Saucelabs portal')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=TestUtils.CHROME_EXECUTABLE_PATH)

    try:
        context.driver.get(TestUtils.URL)
        context.loginPage = LoginPage(context.driver)
        context.inventoryPage = InventoryPage(context.driver)
    except:
        context.driver.close()
        assert False,"Test is failed in open login page section"

@given(u'I have provided my credentials')
def enter_login_creds(context):
    try:
        context.loginPage.enter_login_credentials(TestUtils.USERNAME, TestUtils.PASSWORD)
    except Exception: 
        context.driver.close()
        assert False, "Test is failed in enter login credentials"

@when(u'I click on the Login button')
def enter_login(context):
    try:
        context.loginPage.enter_login()
    except:
        context.driver.close()
        assert False, "Test is failed in enter login"

@then(u'I am successfully logged in and the inventory page is opened')
def validate_dashboard_page(context):
    try:
        context.inventoryPage.validateTitle()
    except:
        context.driver.close()
        assert False, "Test is failed in validate invetory page title"

@when(u'I add the first two elements to the cart')
def fill_cart(context):
    try:
        context.inventoryPage.addItemsToCart()
        assert context.inventoryPage.validateCartQuantity()
    except:
        context.driver.close()
        assert False, "Test is failed in adding items to the cart"

@when(u'I go to the cart and check out the added items')
def checkout_cart(context):
    try:
        context.inventoryPage.goToCart()
        assert context.inventoryPage.validateCartUrl()
        context.inventoryPage.checkoutCart()
    except:
        context.driver.close()
        assert False, "Test is failed checking out items in the cart"

@when(u'I enter my payment information')
def checkout_step_one(context):
    try:
        context.inventoryPage.fillStepOneInfo('Efrain Andres', 'Vergara', '100110')
    except:
        context.driver.close()
        assert False, "Test is failed checking filling step one"

@when(u'I finish the checkout process')
def finish_checkout(context):
    try:
        context.inventoryPage.finishCheckout()
    except:
        context.driver.close()
        assert False, "Test is failed almost at the end"

@then(u'I receive a confirmation message thanking me for my purchase')
def thanks(context):
    assert context.inventoryPage.validateMessage()
    
@when(u'I click on the hamburger menu and select the log out link')
def do_logout(context):
    context.loginPage.log_out()


@then(u'I am logged out of the system')
def step_impl(context):
    pass
