import pytest
from fastapi import HTTPException
from scripts.security_lab_access_control import (
    Resource,
    get_owned_resource,
)


@pytest.fixture
def resources():
    return {
        1: Resource(1, 101, "User A Assignment"),
        2: Resource(2, 202, "User B Assignment"),
    }


def test_user_can_access_own_resource(resources):
    result = get_owned_resource(resources, 1, 101)

    assert result.title == "User A Assignment"


def test_user_cannot_access_another_users_resource(resources):
    with pytest.raises(HTTPException) as error:
        get_owned_resource(resources, 2, 101)

    assert error.value.status_code == 403


def test_missing_resource_returns_404(resources):
    with pytest.raises(HTTPException) as error:
        get_owned_resource(resources, 999, 101)

    assert error.value.status_code == 404


def test_resource_owner_can_access_their_resource(resources):
    result = get_owned_resource(resources, 2, 202)

    assert result.title == "User B Assignment"
