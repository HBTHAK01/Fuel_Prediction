# Functions to test all the functions of the application

# Testing forgotPassword function
def test_forgotPassword(client):
    response = client.post("/forgotPassword", data ={
        "username_Reset": "testUser",
        "password_Reset": "abcABC123",
        "c_password_Reset": "abcABC123",
    })
    assert response.status_code == 200