*** Test Cases ***
While loop simple example
    ${i}    Set Variable   1
    WHILE    ${i}<= 5
        Log To Console    ${i}
        ${i}  Evaluate    ${i}+1
    END