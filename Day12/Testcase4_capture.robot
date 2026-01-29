*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}      firefox
${username}     Admin
${password}     admin123


*** Test Cases ***
TC004_Login.robot
    open browser    ${url}     ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    10s
    input text    name=username    ${username}
    input text    name=password    ${password}
    sleep  2s
    capture page screenshot    beforelogin.png
    Wait Until Element Is Visible    xpath=//*[@type='submit']    10s
    Click Button    xpath=//*[@type='submit']
    Wait Until Element Is Visible    xpath=//div[contains(text(),'Dashboard')]    10s
    Sleep    2s
    capture page screenshot    afterlogin.png
    close browser