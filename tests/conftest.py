# tests/conftest.py
import pytest
from faker import Faker

def pytest_add_option(parser):
    parser.add_option("--num_records", action="store", default=10, type=int, help="number of records to generate")

@pytest.fixture
def faker_fixture(request):
    num_records = request.config.getoption("--num_records")
    fake = Faker()
    return [fake.profile() for _ in range(num_records)]
    
@pytest.fixture
def calculator():
    from main import CommandPatternCalculator  # Import your updated calculator class
    return CommandPatternCalculator()
