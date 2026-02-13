import allure
import pytest
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.COURSES) # Добавили feature
@allure.story(AllureStory.COURSES) # Добавили story
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="", estimated_time="", description="", max_score="0", min_score="0"
        )

        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )

    class TestCourses:
        @allure.title("Edit course")
        @allure.severity(Severity.CRITICAL)
        def test_edit_course(
                self,
                courses_list_page: CoursesListPage,
                create_course_page: CreateCoursePage
        ):

            create_course_page.visit(
                "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"
            )


            create_course_page.create_course_toolbar_view.check_visible(mode='create')
            create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)


            create_course_page.image_upload_widget.upload_preview_image(
                './testdata/files/image.png'
            )
            create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)


            create_course_page.create_course_form.fill(
                title="Selenium WebDriver",
                estimated_time="3 weeks",
                description="Basic Selenium WebDriver course",
                max_score="100",
                min_score="40"
            )


            create_course_page.create_course_toolbar_view.click_create_course_button()


            courses_list_page.toolbar_view.check_visible()
            courses_list_page.course_view.check_visible(
                index=0,
                title="Selenium WebDriver",
                max_score="100",
                min_score="40",
                estimated_time="3 weeks"
            )


            courses_list_page.course_view.menu.click_edit(index=0)


            create_course_page.create_course_toolbar_view.check_visible(mode='update')


            create_course_page.create_course_form.fill(
                title="Advanced Selenium WebDriver",
                estimated_time="5 weeks",
                description="Advanced Selenium WebDriver with Page Object pattern",
                max_score="150",
                min_score="60"
            )


            create_course_page.create_course_toolbar_view.click_update_course_button()


            courses_list_page.toolbar_view.check_visible()
            courses_list_page.course_view.check_visible(
                index=0,
                title="Advanced Selenium WebDriver",
                max_score="150",
                min_score="60",
                estimated_time="5 weeks"
            )
