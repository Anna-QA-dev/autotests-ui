from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    def verify_dashboard_title_visible(self) -> None:
        expect(self.dashboard_title).to_be_visible()

    def verify_dashboard_title_text(self) -> None:
        expect(self.dashboard_title).to_have_text("Dashboard")

    def verify_dashboard_title(self) -> None:
        self.verify_dashboard_title_visible()
        self.verify_dashboard_title_text()