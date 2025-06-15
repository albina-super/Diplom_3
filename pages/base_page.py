import time
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, timeout=15).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_element(*locator)


    def press_esc(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()


    def click_to_element(self, locator):
        WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()


    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)


    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text


    def get_actual_text_after_loading(self, locator):
        WebDriverWait(self.driver, timeout=30).until_not(
            EC.text_to_be_present_in_element(locator, "9999")
        )
        return self.driver.find_element(*locator).text


    def get_class_from_element(self, locator):
        return self.find_element_with_wait(locator).get_attribute("class")


    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)


    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    def get_current_url(self):
        return self.driver.current_url


    def drag_and_drop_chrome(self, locator_from, locator_to):
        action = ActionChains(self.driver)
        element_from = self.find_element_with_wait(locator_from)
        element_to = self.find_element_with_wait(locator_to)
        action.drag_and_drop(element_from, element_to).perform()
        time.sleep(2)


    def drag_and_drop_ff(self, element_from, element_to):

        from_element = self.find_element_with_wait(element_from)

        to_element = self.find_element_with_wait(element_to)

        self.driver.execute_script("""

        const [from_element, to_element] = arguments;

        const dataTransfer = new DataTransfer();

        // Эмуляция событий drag-and-drop

        ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {

        const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });

        (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);

        });

        """, from_element, to_element)


    def get_text_when_presence(self, locator, value):
        WebDriverWait(self.driver, timeout=15).until(
            EC.presence_of_element_located(locator)
        )
        WebDriverWait(self.driver, timeout=15).until_not(
            EC.text_to_be_present_in_element(locator, value)
        )
        return self.driver.find_element(*locator).text


    def wait_for_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, timeout=40).until(
            EC.invisibility_of_element_located(locator)
        )
