action=input("> ")
while(action == "help"):
   # if action=="help"or action=="Help":
    print("start :(to start car move)")
    print("stop :(to stop car moving)")
    print("Exit :(go to exit your game)")
    your_choies = input(">")
    if your_choies == "start":
        print("your car is start to moving ")
    elif your_choies == "stop":
        print("your car is stopped..")
    elif your_choies == "exit":
        print(" exit")
        break
else:
    print("i don't under stand that :!! ")

