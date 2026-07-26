def can_vote(age):
    if age >= 18:
        return "You can Vote"
    else:
        return "You cannot vote yet"

print(can_vote(17))
print(can_vote(18))
print(can_vote(19))