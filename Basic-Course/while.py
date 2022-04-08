import random

is_active = True
count = 1
while is_active:    
    rand = random.randrange(10)
    print(str(count) + " - Time")
    print("Go Down")
    print("Come Up")
    count += 1
    if rand == 0:
        is_active = False
        print("I am Tired")