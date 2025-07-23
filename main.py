import datetime

print("Helo World")
print(5+6)
riedel = "5"
print(riedel)
dowdow = "11a"
print(int(riedel) + int(dowdow.replace("a", "2")))
reibert = 10 % 3
print (reibert)
reibert = 10 / 3
print (reibert)
print(datetime.date.today())
now = datetime.datetime.now()
print(" es ist: \n " + str(now.strftime("%d/%m/%Y, %H:%M")) + " uhr")
 

name = input("wie heißt Du")
print("hallo " + name)


alter = int(input("wie alt"))
if alter <= 17:
    print("minderjährig") 
    if name == "heinrich":
        print ("riedel")


if alter >=18:
    print (alter)






