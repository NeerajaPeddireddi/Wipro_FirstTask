*** Settings ***
Library     SeleniumLibrary
Library     DataDriver    file=testdata.xlsx
Test Template   Login With Credentials

*** Variables ***
${URL}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}  chrome

*** Keywords ***
Open Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible   xpath=//input[@name='username']    10s
Login With Credentials
    [Arguments]    ${username}  ${password}
    Open Login Page
    Input Text  xpath=//input[@name='username']     ${username}
    Input Text  xpath=//input[@name='password']     ${password}
    Click Button   xpath=//button[@type='submit']
    Sleep   3s
    Capture Page Screenshot
    Close Browser
*** Test Cases ***
Login Test Using Excel
    ${username}    ${password}