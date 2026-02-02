*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Test Browser
Suite Teardown    Close Browser

*** Variables ***
${URL}        https://testautomationpractice.blogspot.com/
${BROWSER}    chrome

*** Test Cases ***
Form Interaction Test
    Wait Until Element Is Visible    id:name    10

    Input Text    id:name     ram
    Input Text    id:email    ram@test.com

    Click Element    id:female

    Click Element    id:monday

    Select From List By Label    id:country    India

    Run Keyword If    '${BROWSER}' == 'chrome'    Log    Running on Chrome browser

*** Keywords ***
Open Test Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window