*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
open application
    open browser    https://www.google.com    chrome
    maximize browser window

*** Test Cases ***
Testcase2_keywords.robot
    open application
    title should be     Google
    close browser