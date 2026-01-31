*** Settings ***
Library    Process
Library    SeleniumLibrary

*** Test Cases ***
Environment Setup Verification
    Verify Python Installation
    Verify Robot Framework Installation
    Verify SeleniumLibrary Import
    Log    Environment verification completed successfully

*** Keywords ***
Verify Python Installation
    ${result}=    Run Process    python    --version    stdout=PIPE    stderr=PIPE
    Log    Python Version: ${result.stdout}

Verify Robot Framework Installation
    ${result}=    Run Process    python    -m    robot    --version    stdout=PIPE    stderr=PIPE
    Log    Robot Framework Version: ${result.stdout}

Verify SeleniumLibrary Import
    Log    SeleniumLibrary is installed
