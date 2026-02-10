*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://tutorialsninja.com/demo/
${BROWSER}    Chrome

*** Test Cases ***
Login using reenter vaues
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible     xpath=//a[@title="My Account"]   10s
    Click Link    xpath=//a[@title="My Account"]
    sleep    3s
    Click Link    xpath=//a[text()="Register"]
    sleep    3s
    Input Text    name=firstname    "Raj"
    Input Text    name=lastname    "kumar"
    Input Text    name=email    "Rajkumar12@gmail.com"
    Input Text    name=telephone    "8978675654"
    Input Text    name=password    "Admin123"
    Input Text    name=confirm    "Admin123"
    Select Radio Button    newsletter    1
    Select Checkbox    xpath=//input[@type="checkbox" and @value='1']
    Click Button    xpath=//input[@type="submit" and @value='Continue']

    Close Browser

