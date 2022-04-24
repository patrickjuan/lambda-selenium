from src.controller import WebDriver


def main(event, context):
    driver = WebDriver()
    driver.get("https://www.google.com")
