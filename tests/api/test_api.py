
import requests


def test_api_get(playwright):
    #Creates a new request context like a browser context, but for API requests
    request=playwright.request.new_context(extra_http_headers={"Accept": "application/json","X-API-Key": "reqres-free-v1"})
    #High-level API GET request to a sample endpoint
    response = request.get("https://reqres.in/api/users?page=2")
    assert response.status == 200
    #Parse the JSON response into the variable 'data' and print it to the console
    data = response.json()
    print(data)

    #assertions
    assert data["data"][2]["first_name"] == "Tobias"
    assert data["data"][2]["last_name"] == "Funke"
    #Dispose of the request context to free up resources
    request.dispose()
    print("API GET request test completed successfully.")

def test_api_post(playwright):
    request = playwright.request.new_context(extra_http_headers={"Accept": "application/json", "Content-Type": "application/json"})
    json_body={"name": "John", "job": "leader"}
    response = request.post("https://reqres.in/api/users", data=json_body)
    assert response.status == 201
    data = response.json()
    print(data)
    assert data["name"] == "John"
    assert data["job"] == "leader"
    request.dispose()
    print("API POST request test completed successfully.")