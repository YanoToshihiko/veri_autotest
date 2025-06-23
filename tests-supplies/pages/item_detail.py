from playwright.sync_api import Page

class PageDetail(object):
    def __init__(self, page: Page):
        self.page = page
        self.item_description = page.locator("#item_description")  # ← 変更：book → item

    def open_update(self):
        """備品編集ページを開く"""
        self.page.get_by_role("link", name="編集する").click()

    def open_delete(self):
        """備品を削除する"""
        self.page.get_by_role("link", name="削除する").click()

    def open_detail(self, title: str):
        item_locator = self.page.locator(f'text="{title}"').locator('..')
        item_locator.get_by_role("link", name="詳細へ").click()