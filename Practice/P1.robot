*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Application
    Open Browser    https://www.google.com/    chrome
    Maximize Browser Window
    Title Should be     Google
    Close Browser
