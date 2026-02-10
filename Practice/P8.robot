#Window Shifting
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://the-internet.herokuapp.com/windows
${BROWSER}    Chrome

*** Test Cases ***
Working on window shifting
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    The Internet

    Click Link    xpath=//a[@target='_blank']
    sleep    5s
#    Switch to new window
    Switch Window    New
    Title Should Be    New Window

#    Back to main
    Switch Window    Main
    Title Should Be    The Internet
    Close Browser