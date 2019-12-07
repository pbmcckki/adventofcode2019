# This is not much faster (shall be for bigger range) than previous but short - execution time - 650ms
# inputs 353096-843212

import re

total = 0
adjacents = re.compile("11|22|33|44|55|66|77|88|99|00")
for number in range(353096, 843212 + 1):
    digits = str(number)
    if adjacents.search(digits) and sorted(digits) == list(digits):
        total += 1
        print(digits)

print(total)
