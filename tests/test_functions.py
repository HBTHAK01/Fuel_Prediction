# In this file, test all the functions of the application

# Testing createAccount function
def test_createAccount(client):
    response = client.post("/createAccount", data ={
        "username_Create": "testUser",
        "password_Create": "abcABC123",
        "password_Confirm": "abcABC123",
    })
    assert response.status_code == 200

# Testing forgotPassword function
def test_forgotPassword(client):
    response = client.post("/forgotPassword", data ={
        "username_Reset": "testUser",
        "password_Reset": "abcABC123",
        "c_password_Reset": "abcABC123",
    })
    assert response.status_code == 200

# Testing login function
def test_login(client):
    response = client.post("/", data ={
        "username_login": "testUser",
        "password_login": "abcABC123"
    })
    assert response.status_code == 302