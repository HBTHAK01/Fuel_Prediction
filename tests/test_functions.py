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

# Testing profile function
def test_profile(client):
    response = client.post("/profile", data ={
        "name_Profile": "TestName",
        "email_address": "TestEmail",
        "Address1_Profile": "TestAddress1",
        "Address2_Profile": "TestAddress2",
        "city_Profile": "TestCity",
        "select-state": "Tx",
        "zipcode_Profile": "TestZip"
    })
    assert response.status_code == 200

    # Testing fuelQuote function
def test_fuelQuote(client):
    response = client.post("/fuelQuote", data ={
        "gallons_requested": "10",
        "delivery_date": "010101",
    })
    assert response.status_code == 200