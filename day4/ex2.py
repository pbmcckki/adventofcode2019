# With proper test order adding one more test does not make it run slower than ex1
# as last test is executed in <0.1% cases - 550ms total
# inputs 353096-843212


# inputs 353096-843212


def check(tab):
    has_adjacent = False
    x = 1
    while x < len(tab):
        i = tab[x - 1]
        if i > tab[x]:
            return False
        elif i == tab[x]:
            x += 1
            more_than_two = False
            while x < len(tab):
                if i == tab[x]:
                    x += 1
                    more_than_two = True
                else:
                    break
            if not more_than_two:
                has_adjacent = True
        else:
            x += 1
    return has_adjacent


total = 0
for number in range(353096, 843212 + 1):
    digits = str(number)
    if check(digits):
        total += 1
print(total)
