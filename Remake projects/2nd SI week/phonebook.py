def get_user_input():
    get_name = input("What's your name? ")
    print(f"Hello {get_name}, I am you'r phonebook. ")
    while True:
        try:
            get_age = int(input("How old are you? "))
            if get_age == 1 or get_age <= 18:
                print("You are so young! Life is ahead of you!")
                break
            elif get_age >= 19 or get_age <= 40:
                print("That's a nice age!")
                break
            elif get_age >= 41 or get_age <= 100:
                print("You must be very wise!")
                break
        except ValueError:
            print("That doesn't seem to be an integer.")

def get_propper_numbs(phone_list):
    propper_numbers = []
    for nums in phone_list:
        if len(nums) == 10:
            propper_numbers.append(nums)
    print(f"These are the valid phone numbers in your phonebook:{propper_numbers}")
    return propper_numbers

def get_wrong_numbs(phone_list):
    wrong_numbers = []
    for nums in phone_list:
        if len(nums) != 10:
            wrong_numbers.append(nums)
    print(f"and these are the wrong ones:{wrong_numbers}")
    return wrong_numbers



def get_area_codes(propper_numbers):
    propper_list = propper_numbers
    area_codes = []
    for nums in propper_list:
        area_codes.append(nums[:2])
    no_duplicates = sorted(set(area_codes))
    print(f"The area codes:{no_duplicates}")
    return area_codes

def get_numbs_no_areacodes(propper_numbers):
    propper_list = propper_numbers
    just_numbers = []
    for nums in propper_list:
        just_numbers.append(nums[2:])
    print(f"and the numbers without the area codes:{just_numbers}")
    return just_numbers

def count_numbs(area_codes):
    count98 = 0
    count34 = 0
    count72 = 0
    for numbs in area_codes:
        if numbs == '98':
            count98 += 1
        if numbs == '34':
            count34 += 1
        if numbs == '72':
            count72 += 1
    print(f"You have {count98} numbers from area 98, {count34} numbers from area 34, and {count72} numbers from area 72.")

def get_pretty_numbers(ugly_phone_list):
    pretty_nums = []
    ugly_nums = []
    for char in ugly_phone_list:
        if char[0] != '-' and char[2] == '-' and char[6] == '-' and len(char) == 10:
            pretty_nums.append(char)
        else:
            ugly_nums.append(char)
    print(f"These are the pretty phone numbers:{pretty_nums}")
    print(f"and these are the ugly ones:{ugly_nums}")




def main():
    phone_list = ["98-777-653", "98-742-644", "34-855-326", "34-25-629", "34-489-115", "72-999-563", "9-321-459",
              "72-654-121", "72-4-694", "72-255-313", "98-111-323", "98-433-14", "34-577-342", "98-323-000",
              "98-202-666", "34-5435-454", "34-515-633"]

    ugly_phone_list = ["98-333-111", "12--323-566", "123-34-221", "99-948-321", "-12-123-346",
                     "894-58438-543", "85-234-222",
                     "12-333-444-", "99-888--433", "15-465-876", "98-555-22", "-3-355-333", "3--344-53", "--2--45---",
                     "11-111-222", "12#22$34$222", "98 223 555"]
    user_input = get_user_input()
    propper_numbers = get_propper_numbs(phone_list)
    wrong_numbers = get_wrong_numbs(phone_list)
    area_codes = get_area_codes(propper_numbers)
    no_areacodes_nums = get_numbs_no_areacodes(propper_numbers)
    how_many_areacodes = count_numbs(area_codes)
    pretty_numbs = get_pretty_numbers(ugly_phone_list)

if __name__ == "__main__":
    main()

# Phonebook list
# "These are the valid phone numbers in your phonebook:"
# "and these are the wrong ones:"


# "The area codes:"
# "and the numbers without the area codes:"


# "The unique area codes:"


# "You have X numbers from area 98, Y numbers from area 34, and Z numbers from area 72."


# "These are the pretty phone numbers:"
# "and these are the ugly ones:"

# Greetings
# "What's your name?"
# "Hello XY, I am your phone book."


# "How old are you?"
# - "You are so young! Life is ahead of you!"
# - "That's a nice age!"
# - "You must be very wise!"
# - "That doesn't seem to be an integer."