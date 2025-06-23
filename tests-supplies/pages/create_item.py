from playwright.sync_api import Page

class PageCreate(object):
    def __init__(self, page: Page) -> None:
        self.page = page

    def open_create_item(self):
        """備品登録ページを開く"""
        self.page.get_by_role("link", name="備品登録").click()  # ラベルが「備品登録」に変わっている前提

    def set_title(self, title: str):
        """タイトルを入力する"""
        self.page.locator("#id_title").fill(title)

    def set_description(self, description: str):
        """説明文を入力する"""
        self.page.locator("#id_description").fill(description)
 
    def select_category(self, category: str):
        """カテゴリーを選択する"""
        self.page.locator("#id_category").select_option(label=category)

    def set_thumbnail(self, file_path: str):
        """サムネイル画像を追加する"""
        self.page.locator("#id_thumbnail").set_input_files(file_path)

    def create_new_item(self):
        """備品を登録する"""
        self.page.get_by_role("button", name="作成する").click()
 