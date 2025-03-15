from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def type_into_elements(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()

    def check_display_status_of_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()

    def retrieve_element_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text

    """def get_element(self, locator_name, locator_value):
        if locator_name.endswith("_id"):
            return self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            return self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            return self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            return self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            return self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            return self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return None """

    def get_element(self, locator_name, locator_value, timeout=10):
        wait = WebDriverWait(self.driver, timeout)

        if locator_name.endswith("_id"):
            return wait.until(EC.presence_of_element_located((By.ID, locator_value)))
        elif locator_name.endswith("_name"):
            return wait.until(EC.presence_of_element_located((By.NAME, locator_value)))
        elif locator_name.endswith("_class_name"):
            return wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator_value)))
        elif locator_name.endswith("_link_text"):
            return wait.until(EC.presence_of_element_located((By.LINK_TEXT, locator_value)))
        elif locator_name.endswith("_xpath"):
            return wait.until(EC.presence_of_element_located((By.XPATH, locator_value)))
        elif locator_name.endswith("_css"):
            return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_value)))
        return None

