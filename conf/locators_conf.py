#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the Main page
TEMPERATURE_FIELD = "id,temperature"
BUY_BUTTON = "xpath,//button[contains(text(),'Buy %s')]"

#Product page
PAGE_HEADING = "xpath,//h2[text()='%s']"
PRODUCTS_LIST = "xpath,//div[contains(@class,'col-4')]"
ADD_PRODUCT_BUTTON = "xpath,//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"
CART_QUANTITY_TEXT = "id,cart"
CART_BUTTON = "xpath,//button[@onclick='goToCart()']"

#Cart page
CART_TITLE = "xpath,//h2[text()='Checkout']"
CART_ROW = "xpath,//tbody/descendant::tr"
CART_ROW_COLUMN = "xpath,//tbody/descendant::tr[%d]/descendant::td"
CART_TOTAL = "id,total"

#Payment Page
PAY_BUTTON="xpath,//button[@type='submit']"
EMAIL_FEILD='xpath,//input[@type="email"]'
CARD_FEILD='xpath,//input[@placeholder="Card number"]'
EXPIRE_FEILD='xpath,//input[@placeholder="MM / YY"]'
CVV_FEILD='xpath,//input[@placeholder="CVC"]'
ZIP_FEILD='xpath,//input[@placeholder="ZIP Code"]'
CHECKBOX='xpath,//a[@class="Checkbox"]'
PHONE_FEILD='xpath,//input[@autocomplete="mobile tel"]'
SUBMIT_BUTTON='xpath,//button[@type="submit"]'

#
PAYMENT_HEADER='xpath,//h2[contains(text(),"PAYMENT")]'