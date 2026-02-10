#Simple Alerts
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
working on alerts
    Open Browser    https://letcode.in/alert    chrome
    Maximize Browser Window
    wait until element is visible     xpath=//h1[1]    10s
    Click Button    xpath=//button[@id='accept']
    Alert Should Be Present    10s
    ${alert_text}=    Get Alert Message
    Log    Alert says: ${alert_text}
    Accept Alert

    Close Browser
