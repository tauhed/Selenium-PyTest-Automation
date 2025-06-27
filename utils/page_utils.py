def wait_for_element(driver, by_locator, timeout=10):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(by_locator))