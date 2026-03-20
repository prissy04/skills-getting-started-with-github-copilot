import pytest
from copy import deepcopy
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a TestClient for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def original_activities():
    """Store the original activities state"""
    return deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities(original_activities):
    """Reset activities to original state before each test"""
    # Clear and repopulate activities dict
    activities.clear()
    activities.update(deepcopy(original_activities))
    yield
    # Cleanup after test
    activities.clear()
    activities.update(deepcopy(original_activities))
