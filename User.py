class Users:
    posts = []
    user_manager = {}
    def __init__(self, name, email, dlnumber):
        self.name = name  
        self.email = email
        self._dlnumber = dlnumber
        self.post = "this is my first post"

        Users.user_manager[self.name] = self
   
    def __repr__(self):
        return (f"Name: {self.name} | Email: {self.email} | posts : {Users.posts}")
    @property
    def get_dlnumber(self):
       return self._dlnumber
   
    @classmethod
    def add_post(cls):
        name = input("Name: ")
        email = input("Email Address: ")
        post = input("What would you like to post? ")
        Users.posts.append(post)
        cls(name, email, post)
    
    @staticmethod
    def view_all_users():
        for user in Users.user_manager.values():
            print(repr(user))
    def intro(self):
        print(f"Hi, my name is {self.name}, my email address is {self.email} : Here's what I'm up to right now: {self.post}")
    

caleb = Users("Caleb", "caleb.a.davis114@gmail.com", 292928343)
julia = Users("Julia", "juliadias@gmail.com", 4985673)
steven = Users(email="steventhekingsen@gmail.com",dlnumber=29304058,name="Steven")
julia.intro()
caleb.intro()
steven.intro()

while True:
    Users.add_post()
    Users.view_all_users()