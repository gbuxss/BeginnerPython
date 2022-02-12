# program to check multiple options: car game

'''input commands: help
start- to start the car
stop - to stop the car
quit- to exit

except these options display some information message
'''

command = ""
started = False
print("Available Options\nHelp:\t Start:\t Stop:\t Quit:\t")
while True:
    command = input(">").lower()
    if command == "help":
        print("start- to start the car\nstop - to stop the car\nquit- to exit")
    elif command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Engine Start")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Engine stopped")
    elif command == "quit":
        print("Bye !!! \nSee you later")
        break
    else:
        print("Wrong command \nType 'help' to get help or 'quit' to terminate. ")