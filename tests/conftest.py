# tests/conftest.py
import pytest
from faker import Faker

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="number of records to generate")

@pytest.fixture
def faker_fixture(request):
    num_records = request.config.getoption("--num_records")
    fake = Faker()
    return [fake.profile() for _ in range(num_records)]
# Example of using the faker_fixture
def test_user_profiles(faker_fixture):
    for profile in faker_fixture:
        assert 'mail' in profile  # Assuming 'mail' is part of the generated profiles
