from playwright.sync_api import Page

BASE_URL = "http://127.0.0.1:8000"

class PageTop(object):
    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self):
        """トップページへ遷移する"""
        self.page.goto(BASE_URL, wait_until="load")
