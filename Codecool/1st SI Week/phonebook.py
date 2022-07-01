# Hello there

ask_name = input("What's your name?: ")
print(f"Hello {ask_name}, I am your phonebook.")
#How old are you?

try:
    age = input("How old are you?: ")
    number = int(age)
    if number >= 0 and number < 18:
        print("You are so young! life is ahead of you!")
    elif number >= 18 and number < 40:
        print("That's a nice age!")
    elif number >= 40:
        print("You must be very wise!")
    else:
        print("Value must be greater than 0")

except ValueError:
    print("That doesn't seem to be an integer.")

#list

phone_list = ["98-777-653", "98-742-644", "34-855-326", "34-25-629", "34-489-115", "72-999-563", "9-321-459",
              "72-654-121", "72-4-694", "72-255-313", "98-111-323", "98-433-14", "34-577-342", "98-323-000",
              "98-202-666", "34-5435-454", "34-515-633"]

#check the length

list1 = []
list2 = []
for x in phone_list:
    if len(x) == 10:
        list1.append(x)
    else:
        list2.append(x)
print(f"These are the valid phone numbers in your phonebook:{list1}")
print(f"and these are the wrong ones:{list2}")

#area codes
good_list = list1
area_codes = []
phone_no = []

for x in good_list:
    area_codes.append(x[ :2])
print(f"Area codes:{area_codes}")

for x in good_list:
    phone_no.append(x[2: ])
print(f"Phone numbers: {phone_no}")

#Unique are codes
unique_area_codes = [] 
for x in area_codes: 
    if x not in unique_area_codes: 
        unique_area_codes.append(x) 
 
print ("The unique area codes : " + str(unique_area_codes)) 

#Count area codes
area_codes_number = []

count = 0
count2 = 0
count3 = 0
for pref in area_codes:
    if pref == '98':
        count += 1
for pref in area_codes:
    if pref == '34':
        count2 += 1
for pref in area_codes:
    if pref == '72':
        count3 += 1
print(f"You have {count} numbers from area 98, {count2} numbers from area 34, and {count3} numbers from area 72.")

