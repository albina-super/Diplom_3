import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text


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


    def go_to_url(self, url):
        return self.driver.get(url)


    def script_for_click_to_ff(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_invisible_element(self, locator):
        print(locator,'locator')
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator)
        )


    def drag_and_drop_chrome(self, locator_from, locator_to):
        action = ActionChains(self.driver)
        element_from = self.find_element_with_wait(locator_from)
        element_to = self.find_element_with_wait(locator_to)
        print(locator_to, 'r67890')
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
        time.sleep(2)


