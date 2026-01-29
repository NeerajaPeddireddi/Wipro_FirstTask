Day12 Question 1 – Robot Framework Basics (Coding)
Topics Covered: Introduction to Robot Framework Write a Robot Framework test suite (.robot file) that:
1. Uses the BuiltIn library
2. Contains at least two test cases
3. Logs messages using Log and Log To Console
4. Demonstrates the use of variables (scalar and list)
5. Executes successfully using the robot command

*** Settings ***
Library    BuiltIn

*** Variables ***
${name}     Ram
${age}      21
@{marks}    1    2    3

*** Test Cases ***
Test Case 1 - Logging Scalars
    Log    Hello, my name is ${name} and I am ${age} years old
    Log To Console    This msg is printed to console
    Log    Today we will demonstrate scalar and list variables

Test Case 2 - Using Lists
    Log    List of marks is: @{marks}
    Log To Console    The first mark in the list is: ${marks}[0]
    Log To Console    All marks in the list:
    FOR    ${mark}    IN    @{marks}
    Log To Console    ${mark}
    END
