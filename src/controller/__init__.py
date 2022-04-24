from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class WebDriver:
    def __init__(self):
        self.options = Options()

        self.BASE_DIR = "/tmp"

        self.preferences = {
            "download.default_directory": self.BASE_DIR,
            "download.prompt_for_download": True,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False,
        }

        self.chrome_options = Options()

        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--kiosk")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--single-process")
        self.chrome_options.add_experimental_option("prefs", self.preferences)
        self.chrome_options.binary_location = "/opt/headless-chromium"

        self.driver = webdriver.Chrome(
            "/opt/chromedriver", chrome_options=self.chrome_options
        )

    def get(self, url: str):
        self.driver.get(url)
        print(self.driver.page_source)
