
import random





# using choice() to generate a random number from a
# given list.
print("A random number from list is : ", end="")
print(random.choice(["trash bin", "hamer", "window", "mouse", "brick"]))

# using randrange() to generate in range from 20
# to 50. The last parameter 3 is step size to skip
# three numbers when selecting.
print("A random number from range is : ", end="")
print(random.randrange(20, 50, 3)) 