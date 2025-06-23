from playwright.sync_api import Page

class PageSignup(object):
    def __init__(self, page: Page):
        self.page = page

    def signup_user(self, username: str, password: str):
        """ユーザーIDとパスワードを入力して会員登録する"""
        self.page.locator("#username").fill(username)
        self.page.locator("#password1").fill(password)
        self.page.locator("#password2").fill(password)
        with self.page.expect_navigation():
            self.page.get_by_role("button", name="アカウント作成").click()

    def open_signup(self):
        """会員登録ページを開く"""
        with self.page.expect_navigation():
            self.page.get_by_role("link", name="サインアップ").click()
