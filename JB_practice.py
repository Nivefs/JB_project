import random
print("Enter the number of friends joining (including you):")
number_friends = int(input())
if number_friends == 0 or number_friends < 0:
    print("No one is joining for the party")
    exit()

print("Enter the name of every friend (including you), each on a new line:")
friends = [input() for _ in range(number_friends)]

friends_dict = {key: 0 for key in friends}

print('Enter the total bill value:')
bill_initial = int(input())
bill_value = bill_initial / len(list(friends_dict))
friends_dict = {key: round(bill_value, 2) for key in friends}

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
decision = input()
name = ''
if decision == "Yes":
    bill_value = bill_initial / (len(list(friends_dict)) - 1)
    name = random.choice(list(friends_dict))
    friends_dict = {key: round(bill_value, 2) for key in friends}
    friends_dict[name] = 0
    print()
    print(name)
else:
    print()
    print('No one is going to be lucky')

print()

print(friends_dict)