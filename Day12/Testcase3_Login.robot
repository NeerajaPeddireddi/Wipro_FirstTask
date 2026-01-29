*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}    chrome
${username}   Admin
${password}   admin123

*** Test Cases ***
Testcase3_Login.robot
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    10s
    Input Text    name=username    ${username}
    Wait Until Element Is Visible    name=password    10s
    Input Text    name=password    ${password}
    Wait Until Element Is Visible    xpath=//*[@type='submit']    10s
    Click Button    xpath=//*[@type='submit']
    Sleep    10s
    Close Browser
