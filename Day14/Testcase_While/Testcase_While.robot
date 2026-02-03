*** Test Cases ***
While loop simple example
    ${i}    Set Variable   1
    WHILE    ${i}<= 5
        Log To Console    ${i}
        ${i}  Evaluate    ${i}+1
    END
*** Test Cases ***
While loop with break example
    ${i}    Set Variable   1
    WHILE    ${i}<= 5
        IF    ${i} == 4
            BREAK
        END
        Log To Console    ${i}
        ${i}  Evaluate    ${i}+1
    END  
Using try catch 
    TRY
        Log To Console    Try block
    EXCEPT   
        Log To Console    Exception block    
    FINALLY
        Log To Console    finally
        
    END
Run Keyword If Example
    ${status}=    Set Variable    PASS
    Run Keyword If    '${status}' == 'PASS'    Log    Test Passed
Run Keyword Unless Example
    ${status}=    Set Variable    FAIL
    Run Keyword Unless    '${status}' == 'PASS'    Log    Test Failed
