*** Settings ***
Library     BuiltIn

Suite Setup     Suite Setup Keyword
Suite Teardown  Suite Teardown Keyword

Test Setup      Test Setup Keyword
Test Teardown   Test Teardown Keyword

*** Keywords ***
Suite Setup Keyword
    Log     Suite Setup:Executed once before all tests
Suite Teardown Keyword
    Log     Suite Teardown:Executed once after all tests
Test Setup Keyword
     Log    Test Setup: Executed before each test
Test Teardown Keyword
    Log    Test Teardown: Executed after each test

*** Test Cases ***
Valid Login Test
    [Tags]      smoke       login
    Log     Executing Valid Login Test
    Should Be Equal    1    1
Invalid Login Test
    [Tags]      smoke       login
    Log     Executing InValid Login Test
    Should Be Equal    1    2