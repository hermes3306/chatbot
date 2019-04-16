import random

n = random.randint(1,100)

print(n)


while (1):

    i = (int)(input("Guess my number:"))
    if (i > n):
        print("Bigger than my number!")
    elif( i < n):
        print("Smaller than my number!")
    else:
        print("Congratulations!!!!!!!!")
        print("Binggo my number is %d" %n)
        break;

