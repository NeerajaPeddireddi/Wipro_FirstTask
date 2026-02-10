*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Application
Suite Teardown    Close Browser

*** Variables ***
${URL}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}    Chrome

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
Login OrangHRm
    [Arguments]    ${username}    ${password}
    Go To    ${URL}
    Wait Until Element Is Visible    name=username    10s
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Click Button    xpath=//button[@type='submit']
    Click Element    xpath=//span[@class='oxd-userdropdown-tab']
    Wait Until Element Is Visible    xpath=//a[text()='Logout']    10s
    Click Element    xpath=//a[text()='Logout']
    Wait Until Element Is Visible    name=username    15s

*** Test Cases ***
Login using Data Driven
    [Template]    Login OrangHRm
    Admin    admin123
    Admin    wrongpass

