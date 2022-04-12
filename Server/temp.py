#need to pull list from server, or check off of the server list
usernames = {"bob", "Joe", "billy"}
#Check if the entered user name exists in the user data base
print ("Thank you for your interest in Pelican, please fill out info below")
While: True
entered_user_name = input("Please enter your username:")
if entered_user_name in usernames :
        print("Username already taken please try another")
else:
        entered_password = input("please enter your password:")
print ("sucsess, your info has been sent to the server")
#need to send info to server
# dont know how to send this info either entered_user_name & entered_password