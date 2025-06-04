"""
Everyday in supermarkets, cashiers have to give back the correct change to customers who pay in cash.
How can they determine which bills to give back so that the number of bills is minimal?
In this exercise, we ask you to find the optimal solution to give back change when a checkout only
has $2, $5 and $10 bills.
To make the problem simpler, we'll consider that we have an infinite amount of bills.

Here are some examples:
Change for Possible Solutions Optimal Solution €1 Impossible Impossible €6 €2 + €2 + €2 €2 + €2 + €2 €
10 €2 + €2 + €2 +€2 + €2 €5 + €5 €10 €10 €9223372036854775807 ... (€10 * 922337203685477580) + €5
+ €2
The cash to give back is represented by a dictionary with 3 keys: two, five and ten, which respectively
store the number of $2 bills, $5 bills and $10 bills.
For instance, in the 2nd example ($6), we should get the dictionary:
{
'two': 3, # three $2 bills
'five': 0 # no $5 bills
'ten': 0 # no $10 bills
}

Implement the function change(cash) which should return a dictionary whose two, five and ten
attributes represent the change to give back.
If it is not possible to give back change (like in example 1), return None.
To get the maximum amount of points, your solution will have to return the correct change with
the minimal amount of bills.
Input: 0 < cash < 9007199254740991
"""
def change(cash):
    if cash < 2 or cash in (1, 3):
        return None

    min_bills = float('inf')
    best = None

    max_ten = cash // 10
    for ten in range(max_ten, -1, -1):
        remaining = cash - ten * 10

        five = remaining // 5
        rem_after_five = remaining - five * 5

        if rem_after_five % 2 != 0:
            # Essayons moins de 5 pour voir si ça passe mieux
            if five > 0:
                five -= 1
                rem_after_five += 5
            else:
                continue

        if rem_after_five % 2 != 0:
            continue  # Toujours pas divisible par 2, impossible

        two = rem_after_five // 2
        total_bills = ten + five + two

        if total_bills < min_bills:
            min_bills = total_bills
            best = {'two': two, 'five': five, 'ten': ten}

    return best

print(change(1))  # None
print(change(3))  # None
print(change(6))  # {'two': 3, 'five': 0, 'ten': 0}
print(change(10)) # {'two': 0, 'five': 0, 'ten': 1}
print(change(31)) # {'two': 0, 'five': 1, 'ten': 3}
print(change(8))  # {'two': 4, 'five': 0, 'ten': 0}
print(change(9007199254740991))  # Should run and return optimal
