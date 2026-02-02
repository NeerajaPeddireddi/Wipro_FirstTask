*** Variables ***
@{colors}   Red Green Orange
@{USERS}    admin       user
@{PWDS}     admin@123   user123
*** Test Cases ***
Basic for loop
    FOR    ${name}    IN    Ram raj karan
        Log To Console    ${name}

    END
For loop using list variables
    FOR    ${color}    IN    @{colors}
        Log To Console    ${color}

    END
for loop to print range of values
    FOR    ${i}    IN RANGE    1   6
        Log To Console  Number:${i}

    END

For loop using Enumerate
    FOR    ${index}    ${value}    IN ENUMERATE    a    b    c
        Log To Console    ${index},${value}
    END

#FOR Loop Zip
#    FOR    ${u}    ${p}    IN ZIP    @{USERS}    @{PWDS}
#        Log To Console    ${u} / ${p}
#    END

Nested for loop
    FOR    ${i}    IN RANGE    1    5
        FOR    ${j}    IN RANGE    1    5
            Log To Console    ${i} ${j}
        END
    END

For loop with if condition
    FOR    ${i}    IN RANGE    1    5
        IF    ${i} == 3
            Log To Console    Break 3
        END
    END


For loop with break
    FOR    ${i}    IN RANGE    1    5
        IF    ${i} == 3
            BREAK
            Log To Console    Break 3
        END
        Log To Console    ${i}
    END


For loop with skip
    FOR    ${i}    IN RANGE    1    5
        IF    ${i} == 3
            CONTINUE
            Log To Console    Continue
        END
        Log To Console    ${i}
    END
  