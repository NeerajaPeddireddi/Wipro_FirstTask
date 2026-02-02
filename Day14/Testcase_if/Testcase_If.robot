*** Variables ***
${age}  17

*** Test Cases ***
Working with only if
    ${num}  Set Variable    5
    IF    ${num} == 5
        Log To Console    Equal
    END
Validaing age for vote
    IF    ${age} >= 18
        Log To Console    Eligible for Vote
    ELSE
        Log To Console    Not Eligible for vote 
    END
Working with if else if else
    ${marks}  Set Variable     70
    IF    ${marks} >= 90
        Log To Console    Grade A
    ELSE IF  ${marks} >=80
        Log To Console    Grade B
    ELSE
        Log To Console    Grade C
    END
Sinle Line If
    IF  ${age}==17  Log To Console  Same
    