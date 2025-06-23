from playwright.sync_api import Page

class PageUpdate(object):
    def __init__(self, page: Page):
        self.page = page

    def set_description(self, description: str):
        """説明文を入力する"""
        self.page.locator("#id_description").fill(description)

    def update_item(self):
        """備品の修正を確定する"""
        self.page.get_by_role("button", name="修正する").click()
