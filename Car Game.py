
started=False
while True:
    your_choice = input(">").lower()
    if your_choice == "start":
        if started:
         print("your car already started")
        else:
            started=True
            print("your car is start to moving ")
    elif your_choice== "stop":
        if not started:
            print("your car already Stopped")
        else:
          started=False
          print("your car is stopped..")
    elif your_choice == "exit":
        print(" exit")
        break
    elif your_choice== "help":
        print("""
 start :(to start car move)
 stop  :(to stop car moving)
 Exit  :(go to exit your game)
            """)
    else:
        print("i don't under stand that :!! ")


else:
    print("i don't under stand that :!! ")

