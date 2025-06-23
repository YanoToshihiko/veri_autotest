import datetime

import pytest
from pages import item_detail, create_item, login, mypage, top, update_item
from playwright.sync_api import Page, expect

ADMIN_USERNAME = "admin"  # 各自のユーザーID
ADMIN_PASSWORD = "pass12345"  # 各自のパスワード
DATA_DIR = "./data"  # テストデータのディレクトリ


class TestSupplies:
    @pytest.mark.parametrize(
        "title, description, category, file_path",
        [
            ("カラーペンセット", "カラフルなボールペンのセット。", "消耗品", f"{DATA_DIR}/colorpenset.jpg"),
            ("瞬間接着剤", "壊れた部分の補修に最適。", "消耗品", f"{DATA_DIR}/instant_glue.jpg"),
        ],
        ids=["color_pens", "glue"],
    )
    def test_create_item(self, page: Page, title: str, description: str, category: str, file_path: str):
        """備品を新規登録した後、TOPページの新着備品の1番目に表示されることを確認する

        条件: 直前に同じ備品が登録されていないこと
        """
        page_top = top.PageTop(page)
        page_top.navigate()

        # ログインする
        page_login = login.PageLogin(page)
        page_login.open_login()
        page_login.login_user(ADMIN_USERNAME, ADMIN_PASSWORD)

        # 備品登録する
        page_create = create_item.PageCreate(page)
        page_create.open_create_item()
        page_create.set_title(title)
        page_create.set_description(description)
        page_create.select_category(category)
        page_create.set_thumbnail(file_path)
        page_create.create_new_item()

        # 期待値確認: TOPページ
        page_top.navigate()

    def test_update_item(self, page: Page):
        """登録済みの備品の説明文が正しく更新できることを確認する

        条件: 編集用の備品を登録しておくこと
        """
        page_top = top.PageTop(page)
        page_top.navigate()

        # ログインする
        page_login = login.PageLogin(page)
        page_login.open_login()
        page_login.login_user(ADMIN_USERNAME, ADMIN_PASSWORD)

        # 前処理: 編集用の備品登録
        title = "ファンシーシザー"
        before_description = "ファンシー過ぎて使えないぐらいファンシー"
        category = "道具"
        file_path = f"{DATA_DIR}/fansy_scissors.png"

        page_create = create_item.PageCreate(page)
        page_create.open_create_item()
        page_create.set_title(title)
        page_create.set_description(before_description)
        page_create.select_category(category)
        page_create.set_thumbnail(file_path)
        page_create.create_new_item()

        # マイぺージ -> 備品詳細 -> 備品編集
        page_mypage = mypage.PageMypage(page)
        page_mypage.open_mypage()
        page_mypage.open_item_detail(title)

        page_detail = item_detail.PageDetail(page)
        page_detail.open_update()

        # 備品を編集する
        dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        after_description = f"{before_description}-更新日:{dt}"
        page_update = update_item.PageUpdate(page)
        page_update.set_description(after_description)
        page_update.update_item()

        # 期待値確認: 備品詳細ページ
        expect(page_detail.item_description).to_have_text(after_description)

    def test_delete_supply(self, page: Page):
        """マイページから登録済みの備品を削除すると、マイページの備品一覧に表示されないことを確認する

        前処理: 削除用の備品を登録しておくこと
        """
        page_top = top.PageTop(page)
        page_top.navigate()

        # ログインする
        page_login = login.PageLogin(page)
        page_login.open_login()
        page_login.login_user(ADMIN_USERNAME, ADMIN_PASSWORD)

        # 前処理: 削除用の備品登録
        title = "瞬間接着剤"
        description = "壊れた部分の補修に最適。"
        category = "消耗品"
        file_path = f"{DATA_DIR}/instant_glue.jpg"

        page_create = create_item.PageCreate(page)
        page_create.open_create_item()
        page_create.set_title(title)
        page_create.set_description(description)
        page_create.select_category(category)
        page_create.set_thumbnail(file_path)
        page_create.create_new_item()

        # マイぺージ -> 備品詳細
        page_mypage = mypage.PageMypage(page)
        page_mypage.open_mypage()
        page_mypage.open_item_detail(title)

        # 備品を削除する
        page_detail = item_detail.PageDetail(page)
        page_detail.open_delete()

        # expect: トップページ
        page_top.navigate()
