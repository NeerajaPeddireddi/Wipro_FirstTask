*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}    chrome

*** Keywords ***
Open OrangeHRM
    Open Browser     ${url}    ${browser}
    Maximize Browser Window

OrangeHRM Login
    [Arguments]     ${username}    ${password}
    Capture Page Screenshot    beforelogin.png
    Wait Until Element Is Visible    xpath=//input[@name='username']    15s
    Input Text    xpath=//input[@name='username']    ${username}
    Wait Until Element Is Visible    xpath=//input[@name='password']    15s
    Input Text    xpath=//input[@name='password']    ${password}

    Click Button    xpath=//button[@type='submit']

    Capture Page Screenshot    afterlogin.png

    Close Browser

*** Test Cases ***
Login Test Data Driven
    Open OrangeHRM
    OrangeHRM Login    Admin    admin123
