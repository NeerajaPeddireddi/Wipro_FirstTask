* Settings *
Library    RequestsLibrary


* Variables *
${baseurl}  http://127.0.0.1:5000

* Test Cases *
Verify Get_User
        Create Session    mysession             ${baseurl}
        ${response}=  GET On Session    mysession   /users
        Status Should Be    200      ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True

Verify single_User
        Create Session    mysession             ${baseurl}
        ${response}=  GET On Session    mysession   /users/1
        Status Should Be    200      ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True
#Verify User_Not Present
#        Create Session    mysession             ${baseurl}
#        ${response}=  GET On Session    mysession   /users/8
#        Status Should Be    404      ${response}
#        ${res_jon}=     To Json    ${response.content}
#        log       ${res_jon}=   console=True
Verify Create_New_User
        ${data}=  Create Dictionary    name=arjun
        Create Session    mysession             ${baseurl}
        ${response}=  POST On Session    mysession   /users    json=${data}
        Status Should Be    201      ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True

Verify Update User
        ${data}=  Create Dictionary    name=karna
        Create Session    mysession             ${baseurl}
        ${response}=  PUT On Session    mysession   /users/1    json=${data}
        Status Should Be    200     ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True

Verify Patch User
        ${data}=  Create Dictionary    name=bheem
        Create Session    mysession             ${baseurl}
        ${response}=  PATCH On Session    mysession   /users/1    json=${data}
        Status Should Be    200     ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True
Verify Delete User by user id
        ${data}=  Create Dictionary    name=bheem
        Create Session    mysession             ${baseurl}
        ${response}=  DELETE On Session    mysession   /users/11    json=${data}
        Status Should Be    200     ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True
