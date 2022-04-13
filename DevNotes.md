
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


Auth.py: email, password  
Register.py: username, email, password  
AuthFunction.py:   
```  
  
Authenticate(token) authentacte a user by a token, returns True/False  
  
```