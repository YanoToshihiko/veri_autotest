from playwright.sync_api import Page


class PageLogin(object):
    def __init__(self, page: Page):
        self.page = page

    def login_user(self, username: str, password: str):
        """ユーザーIDとパスワードでログインする"""
        self.page.locator("[name='username']").fill(username)
        self.page.locator("[name='password']").fill(password)
        with self.page.expect_navigation():
            self.page.get_by_role("button", name="ログインする").click()

    def open_login(self):
        """ログインをクリックする"""
        self.page.get_by_role("link", name="ログイン").click()
