
**Account Info Format** <br /> 
"id": UserID <br /> 
"username": username <br /> 
"email": Email <br /> 
"password": Password <br /> 
"tag": Tag <br />
**-----**


Tag: User Tag (Name:0001)
ID: User id for API, ord username+Tag
Username: Username for user
Email: private info, users email
Password: private allows user to login
Token: sha256 username+email+password, used like password for API


**Auth.py**  
```
Takes email and password and returns *Login Success* if info is correct, else it will return *Login Failed
```  
**Register.py**  
```
Takes username, email and password and returns *Register Success* if it works, if not it will return the reason [Invalid Username, Invalid Email, Password To Short]
```  
**AuthFunction.py**   
```  
Authenticate(token) authenticate a user by a token, returns True/False  
AuthenticateReturnID(token) authenticate a user by a token, returns UserID
AuthenticateUsername(token) authenticate a user by a token, returns Username
```

**Command to run django server**
```
python manage.py runserver
```

**Admin Panel**
```
Admin login = test:test
```
