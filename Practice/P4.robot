#Clear Text Field
#Clear existing text
#Enter new value
#Skills: Clear Element Text
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}    Chrome

*** Test Cases ***
Login using reenter vaues
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    10s
    Input Text    name=username    "admin"
    sleep    3s
    Clear Element Text    name=username
    sleep    3s
    Input Text    name=username    "Admin"
    Input Text    name=password    "admin123"
    Click Button    xpath=//button[@type='submit']
    Close Browser