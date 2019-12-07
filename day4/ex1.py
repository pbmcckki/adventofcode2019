# Super ineffective but quick
# inputs 353096-843212


def check_adjacent(tab):
    i = tab[0]
    for x in range(1, len(tab)):
        if i == tab[x]:
            return True
        else:
            i = tab[x]
    return False


def check_monotonic(tab):
    i = tab[0]
    for x in range(1, len(tab)):
        if i <= tab[x]:
            i = tab[x]
        else:
            return False
    return True


total = 0
for number in range(353096, 843212 + 1):
    digits = str(number)
    if check_adjacent(digits) and check_monotonic(digits):
        total += 1

print(total)
