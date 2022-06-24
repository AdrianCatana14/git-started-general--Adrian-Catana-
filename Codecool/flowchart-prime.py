# Implement flowchart "Prime" here.
print ("Start")
i = 2
while True:
    try:
        n = int(input("Give me a number n (greater than 1): "))
        break;
    except ValueError:
        print("Not an integer")

if n < 2:
    print("Too small")
    print("Stop")
elif n > i and n % i == 0:
    print("Not prime")
    print("Stop")
elif n > i and not n % i == 0:
    i = i + 1
    print("Prime")
    print("Stop")





# Give me an integer (greater than 1)
# Possible outcomes:
# - Not an integer
# - Too small
# - Not prime
# - Prime
