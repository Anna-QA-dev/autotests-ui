import pytest

@pytest.mark.smoke
def test_some_case():
    ...

@pytest.mark.regression
def test_regression_case():
    assert 2 * 2 == 4

@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        ...

    def test_case2(self):
        ...


@pytest.mark.regression
class TestUserAuthentication:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    pass