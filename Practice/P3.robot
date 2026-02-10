#Input Text & Click Button
#Enter text in input field
#Click submit/login button
#Skills: Input Text, Click Button
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}    Chrome

*** Test Cases ***
Login
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username     10s
    Input Text    name=username   "Admin"
    Input Text    name=password    "admin123"
    Click Button    xpath=//button[@type='submit']
    Close Browser