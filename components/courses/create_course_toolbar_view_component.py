from playwright.sync_api import Page
import allure
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_course_button = Button(
            page, 'create-course-toolbar-create-course-button', 'Create course'
        )
        self.update_course_button = Button(
            page, 'create-course-toolbar-create-course-button', 'Update course'
        )

    @allure.step('Check visible create course toolbar in {mode} mode')
    def check_visible(self, mode: str = 'create'):

        self.title.check_visible()

        if mode == 'create':
            self.title.check_have_text('Create course')
            self.create_course_button.check_visible()
        else:
            self.title.check_have_text('Update course')
            self.update_course_button.check_visible()

    def click_create_course_button(self):
        """Нажатие кнопки создания курса"""
        self.create_course_button.click()

    def click_update_course_button(self):
        """Нажатие кнопки обновления курса"""
        self.update_course_button.click()

    @allure.step('Check that create course button is disabled')
    def check_disabled_create_course_button(self):
        """Проверка, что кнопка создания отключена"""
        self.create_course_button.check_disabled()

    @allure.step('Check that update course button is disabled')
    def check_disabled_update_course_button(self):
        """Проверка, что кнопка обновления отключена"""
        self.update_course_button.check_disabled()