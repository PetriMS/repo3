*** Settings ***
Resource  resource.robot


*** Test Cases ***
Register With Valid Username And Password
    Input New Credentials  jorma  jormantunnus1  
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User
    Input New Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Create User
    Input New Credentials  ka  kalle123
    Output Should Contain  Username should have at least 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Create User
    Input New Credentials  kalle!  kalle123
    Output Should Contain  Username should only contain letters a-z

Register With Valid Username And Too Short Password
    Create User
    Input New Credentials  kalle  kalle12
    Output Should Contain  Password should have at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User
    Input New Credentials  kalle  kallekalle
    Output Should Contain  Password should not contain only letters

*** Keywords ***
Create User
    Input New Credentials    kalle    kalle123