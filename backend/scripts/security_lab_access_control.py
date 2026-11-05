"""Isolated security lab: user-level resource access control."""

from dataclasses import dataclass

from fastapi import HTTPException


@dataclass
class Resource:
    resource_id: int
    owner_id: int
    title: str


def get_owned_resource(
    resources: dict[int, Resource],
    resource_id: int,
    authenticated_user_id: int,
) -> Resource:
    """Return a resource only when the authenticated user owns it."""

    resource = resources.get(resource_id)

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="Resource not found",
        )

    if resource.owner_id != authenticated_user_id:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to access this resource",
        )

    return resource


def main():
    resources = {
        1: Resource(1, 101, "User A Assignment"),
        2: Resource(2, 202, "User B Assignment"),
    }

    print("=== User-Level Access Control Lab ===")

    # User A accesses their own resource.
    result = get_owned_resource(resources, 1, 101)
    print("Own resource:", result.title)

    # User A attempts to access User B's resource.
    try:
        get_owned_resource(resources, 2, 101)
    except HTTPException as error:
        print("Unauthorized access blocked:", error.status_code)


if __name__ == "__main__":
    main()
