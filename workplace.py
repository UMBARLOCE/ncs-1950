import pyautogui
import time
from selenium import webdriver


def get_driver():
    # print('get_driver')
    # service = Service('/Users/umbarloce/PycharmProjects/rest_pars_v3_mono/chromedriver')  # windows
    # service = Service('/usr/lib/chromium-browser/chromedriver')  # linux
    options = webdriver.ChromeOptions()
    # options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument('--headless')  # options.headless = True
    # options.page_load_strategy = 'eager'
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    return driver


def save_screenshot(url: str):
    color = url.split('/')[-1]
    lst = [(285, 790), (400, 790), (520, 790), (640, 790)]
    for x, y in lst:
        time.sleep(2)
        pyautogui.click(x, y)
        time.sleep(1)
        screenshot = pyautogui.screenshot(region=(100, 170, 590, 560))
        screenshot.save(f'{x}.png')
        

def main():
    driver = get_driver()
    driver.maximize_window()
    driver.get('https://akkras.ru/colors/ncs_index_original/ncs_s_0580_y70r.html')
    time.sleep(10)
    driver.quit()
    # save_screenshot('https://akkras.ru/colors/ncs_index_original/ncs_s_0580_y70r.html')

if __name__ == '__main__':
    main()

# pyautogui.displayMousePosition()
# pyautogui.screenshot(97, 172, 694, 731)
