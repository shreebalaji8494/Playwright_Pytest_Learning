
import requests


# This file contains API smoke tests for the ReqRes mock service.
# The goal is to verify basic GET and POST operations behave as expected.


def test_api_get(playwright):
    """Validate that a GET request returns the expected user data."""
    # Create a dedicated request context to isolate API calls and attach headers.
    request = playwright.request.new_context(
        extra_http_headers={"Accept": "application/json", "X-API-Key": "reqres-free-v1"}
    )

    # Fetch a paginated list of users from the public ReqRes API.
    response = request.get("https://reqres.in/api/users?page=2")
    assert response.status == 200

    # Convert the response body into Python data for assertions.
    data = response.json()
    print(data)

    # Verify that the response contains the expected user fields for this specific page.
    assert data["data"][2]["first_name"] == "Tobias"
    assert data["data"][2]["last_name"] == "Funke"

    # Close the request context to free resources after the check.
    request.dispose()
    print("API GET request test completed successfully.")


def test_api_post(playwright):
    """Validate that a POST request creates a new user record successfully."""
    # Create a request context for JSON-based API communication.
    request = playwright.request.new_context(
        extra_http_headers={"Accept": "application/json", "Content-Type": "application/json"}
    )

    # Prepare the request payload for the new user record.
    json_body = {"name": "John", "job": "leader"}

    # Send a POST request to the ReqRes create-user endpoint.
    response = request.post("https://reqres.in/api/users", data=json_body)
    assert response.status == 201

    # Parse the created-user response and validate the returned values.
    data = response.json()
    print(data)
    assert data["name"] == "John"
    assert data["job"] == "leader"

    # Clean up the connection resources used for the API call.
    request.dispose()
    print("API POST request test completed successfully.")