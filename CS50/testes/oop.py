class User():
    user_count = 0
    def __init__(self, username, password, email):
        self.username = username
        self._email = email
        self.password = password
        User.user_count +=1

    @property
    def email (self):
        print ("Email Acessed")
        return self._email

    @email.setter

    def email (self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            print ("Invalid Email")



user1 = User("MarcoCotas", "Tugatr_006", "marco.cotas06@gmail.com")
user2 = User("Travolta", "travolta@gmail.com", "123456")
user1.email = ("fsdfgsgwse")

print (user1.email)
print (User.user_count)
