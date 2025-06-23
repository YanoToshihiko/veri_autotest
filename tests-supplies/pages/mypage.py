from playwright.sync_api import Page

BASE_URL = "http://127.0.0.1:8000"

class PageMypage(object):
    def __init__(self, page: Page):
        self.page = page

    def open_mypage(self):
        """トップページへ遷移"""
        self.page.goto(BASE_URL, wait_until="load")

    def open_item_detail(self, title: str):
        # タイトルを含むカードを絞り込む
        item_cards = self.page.locator('div.p-4.bg-light.border.border-success.rounded').filter(
            has_text=title
        )
        count = item_cards.count()
        if count == 0:
            raise Exception(f"タイトル '{title}' の備品が見つかりません")
        # 先頭のカードを取得してリンクをクリック
        item_card = item_cards.first
        item_card.get_by_role("link", name="詳細へ").click()
