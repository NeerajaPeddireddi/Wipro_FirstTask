#*** Test Cases ***
#Print Names
#    FOR    ${name}    IN   Ram Raj Karan
#        Log To Console  ${name}
#
#    END
*** Variables ***
@{names}    ram    arun    karna

*** Test Cases ***
Print Names Using For Loop
    FOR    ${name}    IN    @{names}
        Log    ${name}
    END

Print Names Using While Loop
    ${count}  Set Variable  1
    WHILE    ${count} <=5
        Log To Console   ${count}
        ${count}  Evaluate  ${count}+1
    END

