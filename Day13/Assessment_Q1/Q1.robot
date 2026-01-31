*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Day13 Assignment1
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window
    Title Should Be     Google
    Capture Page Screenshot    google_home.png
    Close Browser

