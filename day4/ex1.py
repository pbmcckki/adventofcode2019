# More effective, 1 loop only on digits; executio ~ 560ms
# inputs 353096-843212


def check(tab):
    i = tab[0]
    has_adjacent = False
    for x in range(1, len(tab)):
        if i == tab[x]:
            has_adjacent = True
            i = tab[x]
            continue
        elif i > tab[x]:
            return False
        else:
            i = tab[x]
    return has_adjacent


total = 0
for number in range(353096, 843212 + 1):
    digits = str(number)
    if check(digits):
        total += 1

print(total)
