should_continue = True
if should_continue:
    print ("Hello")

known_people = ["John","Anna","Mary"]

#person = input("Enter the person you know: ")

# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("You don't {}!".format(person))

#if person not in known_people:

def who_do_you_know():
    #Ask the user for a list of people they know
    #Split the string into a list
    #Return the list
    # people = input("Enter the names of people you know, separated by commas: ")
    # people_list = people.split(",")
    # clean_people = []
    # for person in people_list:
    #     clean_people.append(person.strip())
    # return clean_people
    people = input("Enter the names of people you know, separated by commas: ")
    people_list = people.split(",")
    people_without_spaces = [person.strip() for person in people_list]
    return people_without_spaces

def ask_user():
    #Ask user for their name
    #See if their name is in the list of people do you know
    #Print out that they know the person
    person = input("Enter the person you know: ")

    if person in who_do_you_know():
        print("You know {}!".format(person))
    else:
        print("You don't {}!".format(person))

ask_user()