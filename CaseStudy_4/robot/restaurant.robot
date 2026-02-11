*** Settings ***
Resource    resources/keywords.robot
Suite Setup    Create API Session


*** Test Cases ***
#Restaurant Module
Add Restaurant Positive
    Create Restaurant
Get Restaurant
    Create Restaurant
    ${response}=    GET On Session    foodie    /api/v1/restaurants/1
    Should Be Equal As Integers    ${response.status_code}    200

Search Restaurant By Location
    ${params}=    Create Dictionary    location=Hyderabad
    ${response}=    GET On Session    foodie    /api/v1/restaurants/search    params=${params}
    Should Be Equal As Integers    ${response.status_code}    200
#Dish Module
Add Dish
    Create Dish

Update Dish
    Create Restaurant
    Create Dish
    ${update}=    Create Dictionary    price=300
    ${response}=    PUT On Session    foodie    /api/v1/dishes/1    json=${update}
    Should Be Equal As Integers    ${response.status_code}    200

Delete Dish
    Create Restaurant
    Create Dish
    ${response}=    DELETE On Session    foodie    /api/v1/dishes/1
    Should Be Equal As Integers    ${response.status_code}    200

User Registration
    Create User
#User Module
Duplicate User Registration
    ${random}=    Generate Random String    5
    ${email}=    Set Variable    john${random}@test.com

    ${body}=    Create Dictionary
    ...    name=John
    ...    email=${email}
    ...    password=1234

    ${response1}=    POST On Session    foodie    /api/v1/user/register    json=${body}
    Should Be Equal As Integers    ${response1.status_code}    201

    ${response2}=    POST On Session    foodie    /api/v1/user/register    json=${body}    expected_status=409
    Should Be Equal As Integers    ${response2.status_code}    409

#Order Module
Place Order
    Create Restaurant
    Create User
    Create Order

Get Orders By Restaurant
    Create Restaurant
    Create User
    Create Order
    ${response}=    GET On Session    foodie    /api/v1/restaurants/1/orders
    Should Be Equal As Integers    ${response.status_code}    200

Get Orders By User
    Create Restaurant
    Create User
    Create Order
    ${response}=    GET On Session    foodie    /api/v1/users/1/orders
    Should Be Equal As Integers    ${response.status_code}    200
#Rating Module
Add Rating
    Create Restaurant
    Create User
    Create Order
    ${body}=    Create Dictionary
    ...    order_id=1
    ...    rating=5
    ...    comment=Excellent
    ${response}=    POST On Session    foodie    /api/v1/ratings    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
 #Admin module
Admin Approve Restaurant
    Create Restaurant
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/1/approve
    Should Be Equal As Integers    ${response.status_code}    200

Admin Disable Restaurant
    Create Restaurant
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/1/disable
    Should Be Equal As Integers    ${response.status_code}    200

Admin Get Orders
    ${response}=    GET On Session    foodie    /api/v1/admin/orders
    Should Be Equal As Integers    ${response.status_code}    200

Admin Get Feedback
    ${response}=    GET On Session    foodie    /api/v1/admin/feedback
    Should Be Equal As Integers    ${response.status_code}    200