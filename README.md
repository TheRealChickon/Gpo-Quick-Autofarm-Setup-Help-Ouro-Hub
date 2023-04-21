# GpoOuroAutoJsonFormat

Read this thoroughly:

Run AutoFarm.py once to generate the following files required, if it does not create them for some Reason create them yourself manually. <br>

    1. AccountNames.txt
    2. PrivateServers.txt

How to use:  <br>
    1. Write your Roblox accounts names in the ***AccountNames.txt*** file. <br>
      &nbsp; &nbsp; &nbsp; &nbsp;  > Every line should only contain a single Account 
    
    Example:

    AccountName1
    AccountName2
    AccountName3
    AccountName4

How to use:  <br>
    2. Write your Private Server Codes in the ***PrivateServers.txt*** file. <br>
      &nbsp; &nbsp; &nbsp; &nbsp;  > Every line should only contain a single Code if you wish to use one per account. 
    
Note: If you wish to use a private server on multiple accounts at once you can just paste the same code on multiple lines in the file.

    Example:

    PrivateServerCode1
    PrivateServerCode2
    PrivateServerCode3
    PrivateServerCode4
        


*Want to change the Config file to suit your script save format?* <br>

- Change the ***config_template*** variable in AutoFarm.py to your desired format.
- It should be fairly easy to modify this for more customizability as long as you have basic Python knowledge, if you don't -> You're fucked. Try asking someone who is not me because I have no Plans of updating this as I made this for me rq in the first place.

### IMPORTANT NOTE

The line the account is in corresponds to his private server assigned.

**Example:** <br>
**Test1** -> *line 1* in AccountNames.txt <br>
Then his private server will be the one in *line 1* in PrivateServers.txt -> **PrivateServerCode1**