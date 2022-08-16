class User:
   def __init__(self,id,name):
       self.id = id
       self.name = name
       self.followers = 0
       self.following = 0

   def follow(self,user):
       self.following += 1
       user.followers += 1


user_1 = User("001","Sats")
user_2 = User("002","Pan")
user_3 = User("003","Adhi")
user_4 = User("004","Praba")
# print(user_1.name)
# print(user_3.name)
# print(user_2.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
user_3.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
print(user_3.followers)
print(user_3.following)