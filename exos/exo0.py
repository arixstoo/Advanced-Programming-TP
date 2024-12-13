people = int(input("How many people need a ride?"))
taxi = int(input("How many people fit in one taxi??"))
taxies = people//taxi
if(people%taxi !=0):
    taxies+=1

print(f"Number of taxis needed: ", {taxies})