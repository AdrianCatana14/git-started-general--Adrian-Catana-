# Implement flowchart "Prime" here.
print ("Start")
while True:
    try:
        n = int(input("Give me a number n (greater than 1): "))
        break
    except ValueError:
        print("Not an integer")

if n < 2:
    print("Too small")
    print("Stop")
i  = 2
while i < n:
    if n % i == 0:
        print("Not prime")
        break
    else:
        i = i + 1
print('Prime')





# Give me an integer (greater than 1)
# Possible outcomes:
# - Not an integer
# - Too small
# - Not prime
# - Prime
