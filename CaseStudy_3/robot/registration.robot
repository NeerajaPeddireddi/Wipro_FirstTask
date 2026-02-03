*** Settings ***
Library     SeleniumLibrary
Suite Setup     Open Browser    http://127.0.0.1:5000    chrome
Suite Teardown    Close Browser

*** Test Cases ***
Register New Patient
    Input Patient Details    Ravi    35    Male    9876543210    Fever    Dr. Sharma
*** Keywords ***
Input Patient Details
    [Arguments]    ${name}    ${age}    ${gender}    ${contact}    ${disease}    ${doctor}
    Input Text    name=name    ${name}
    Input Text    name=age     ${age}
    Click Element    xpath=//input[@value='${gender}']
    Input Text    name=contact    ${contact}
    Input Text    name=disease    ${disease}
    Select From List By Label    name=doctor    ${doctor}
    Click Button    Register
