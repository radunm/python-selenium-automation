# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example:
# 348597 => [7,9,5,8,4,3]


def digitize(n):
    result = []
    digit = n % 10

    while n > 0:
        result.append(digit)
        n //= 10
        digit = n % 10
    return result


print(digitize(348597))
