# with open("file.txt","a") as f:
#     f.write("hello")
# with open("file.txt","r") as f:
# 


# with open("file.txt","w") as f:
#       f.write("hi")
# with open("newfile.txt","w") as f:
#         f.write("hi")

for i in range(5):

    with open("anothernewfile.csv","a+") as f:
        name = input("Your name:")
        age = int(input("Your age:"))
        address = input("Your address:")
        phone = int(input("Your phone:"))
        subject = input("Your Subject:")
        f.write(f"Name:{name},Age:{age},Address:{address},Phone:{phone},Subject:{subject}\n")
        

