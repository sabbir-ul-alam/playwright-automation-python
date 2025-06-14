import  pytest
import json


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="stg", help="Environment to run"
    )


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    with open(f"config/{env}.json") as f:
        return json.load(f)



