*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    String

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Keywords ***
Create API Session
    Create Session    foodie    ${BASE_URL}
Create Restaurant
    ${random}=    Generate Random String    5
    ${images}=    Create List    img1.jpg
    ${body}=    Create Dictionary
    ...    name=Food Hub ${random}
    ...    category=Indian
    ...    location=Hyderabad
    ...    images=${images}
    ...    contact=9876543210
    ${response}=    POST On Session    foodie    /api/v1/restaurants    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201

Create User
    ${random}=    Generate Random String    5
    ${email}=    Set Variable    john${random}@test.com
    ${body}=    Create Dictionary
    ...    name=John
    ...    email=${email}
    ...    password=1234
    ${response}=    POST On Session    foodie    /api/v1/user/register    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201

Create Order
    ${dish_list}=    Create List    1
    ${body}=    Create Dictionary
    ...    user_id=1
    ...    restaurant_id=1
    ...    dishes=${dish_list}
    ${response}=    POST On Session    foodie    /api/v1/orders    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
Create Dish
    Create Restaurant
    ${body}=    Create Dictionary
    ...    name=Biryani
    ...    type=Veg
    ...    price=250
    ...    available_time=Lunch
    ${response}=    POST On Session    foodie    /api/v1/restaurants/1/dishes    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201