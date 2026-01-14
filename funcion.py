# def hello():
#     print("hello")

# hello()

def getUserInfo(name, age):
    return f"Hello,{name},-{age}"

def writeFileInfo():
    name = input("Your name: ")
    address = input("Your name: ")
    age = int(input("Your address: "))
    phone = int(input("Your phone: "))

    with open("file.csv","a+") as f:
        f.write(f"{name},{age},{address},{phone}\n")
    print("hello")

info = getUserInfo("A", 20)
print(info)
# writeFileInfo()
