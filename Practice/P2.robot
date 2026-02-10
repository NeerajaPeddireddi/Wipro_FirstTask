#Verify Element Present
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
verify title
    Open Browser    https://www.google.com/    chrome
    Maximize Browser Window
    Page Should Contain    Google
    Close Browser
