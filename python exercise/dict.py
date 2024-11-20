# Dictionary allows us to store key value pairs.Also known as  Maps, Hashtables, Associative Arrays.
people = {"sam" :12345, "ram":98765, "kirti":94534}
print(people)
print(people["sam"])

for key in people:
    print("Key:", key,"value:", people[key])

if "sam" in people:
    print("you are right")