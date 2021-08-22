from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "browserVersion": "92.0",
    # "moon:options": {
    #     "enableVNC": True,
    #     "enableVideo": True,
    #     "name": "MyCoolTest",
    #     "screenResolution": "1024x768",
    #     "sessionTimeout": "5m",
    # }
}

driver = webdriver.Remote(
    command_executor='https://username:password@my-company.cloud.aerokube.com/wd/hub',
    desired_capabilities=capabilities
)

try:
    print('Session ID is: %s' % driver.session_id)  # This may be needed for debugging
    driver.get('https://example.com/')
    driver.get_screenshot_as_file(driver.session_id + '.png')
finally:
    driver.quit()
