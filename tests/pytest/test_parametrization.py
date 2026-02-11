import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number',[1, 2, 3, -1])
def test_number(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1,1), (2,4), (3,9),(4,16)])
def test_several_number(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
@pytest.mark.parametrize('os', ['macos','windows','linux','debian'])
def test_multiplication_numbers(os: str, browser: str):
    assert len(os+browser) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str):
    print("Running test on browser: {browser}")

@pytest.mark.parametrize('user', ['Zara', 'Alice'])
class TestOperation:

    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        ...

    def test_user_without_operations(self, user: str):
        ...


users = {
    '+79033685454': 'user with money on bank account',
    '+79120520789': 'user without money on bank account',
    '+79212064488': 'user with operations on bank account'
}

@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids= lambda phone_number: f'{phone_number}: {users[phone_number]}'
)


def test_identifiers(phone_number: str):
        ...





