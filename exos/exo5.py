name1 = input("Enter your name : ")
time1 = input("Enter your time (in seconds) : ")

name2 = input("Enter your name : ")
time2 = input("Enter your time (in seconds) : ")

if time1<time2:
    print("Runner 1:\nName: ",name1,"\nTime(in seconds): ",time1)
    print("Runner 2:\nName: ",name2,"\nTime(in seconds): ",time2)
    print("The faster runner is: ",name2)
elif time1>time2:
    print("Runner 1:\nName: ",name1,"\nTime(in seconds): ",time1)
    print("The faster runner is: ",name1)
elif time1==time2:
    print("Runner 2:\nName: ",name2,"\nTime(in seconds): ",time2)
    print(name1, " and ",name2, " have the same time")