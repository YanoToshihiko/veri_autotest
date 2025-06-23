import datetime
import re

from pages import login, signup, top
from playwright.sync_api import Page, expect

ADMIN_USERNAME = "admin"  # 各自のユーザーID
ADMIN_PASSWORD = "pass12345"  # 各自のパスワード


class TestUser(object):
    def test_signup(self, page: Page):
        """会員登録できることを確認する"""
        page_top = top.PageTop(page)
        page_top.navigate()

        # 会員登録する
        page_signup = signup.PageSignup(page)
        page_signup.open_signup()

        dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        username = f"test-{dt}"
        password = ADMIN_PASSWORD
        page_signup.signup_user(username, password)

        # 期待値確認: TOPページ
        expect(page).to_have_title(re.compile("備品一覧 | 社内備品管理システム"))

        # ログインする
        page_login = login.PageLogin(page)
        page_login.open_login()
        page_login.login_user(username, password)


    def test_login(self, page: Page):
        """ログイン後の画面表示が正しいことを確認する"""
        page_top = top.PageTop(page)
        page_top.navigate()

        # ログインする
        page_login = login.PageLogin(page)
        page_login.open_login()
        page_login.login_user(ADMIN_USERNAME, ADMIN_PASSWORD)

