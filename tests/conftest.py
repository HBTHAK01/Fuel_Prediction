# import statements
import pytest
from fuel_app import create_app


# Defining fixtures to allow writing pieces of code that are reusable across tests
@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })


    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()