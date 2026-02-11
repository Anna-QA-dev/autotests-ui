import pytest


@pytest.fixture(scope="function")
def function_browser():
    print("Данная фикстура будет запущена на каждый автотест")

@pytest.fixture(scope="class")
def class_browser():
    print("Данная фикстура будет запущена на каждый тестовый класс")

@pytest.fixture(scope="module")
def module_browser():
    print("Данная фикстура будет запущена на каждый модуль python")

@pytest.fixture(scope="session")
def session_browser():
    print("Данная фикстура будет запущена один раз на всю тестовую сессию")
