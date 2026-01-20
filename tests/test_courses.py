from playwright.sync_api import expect, sync_playwright, Playwright
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_text = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_text).to_be_visible()
    expect(courses_text).to_have_text('Courses')

    block_text = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(block_text).to_be_visible()
    expect(block_text).to_have_text('There is no results')

    courses_list = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(courses_list).to_be_visible()
    expect(courses_list).to_have_text('Results from the load test pipeline will be displayed here')

    icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_be_visible()