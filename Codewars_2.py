# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#
# The output should be two capital letters with a dot separating them.
#
# It should look like this:
#
# Sam Harris => S.H
#
# Patrick Feeney => P.F


init_name = "Patrick Feeney"


def abbrev_name(name):
    result = name[0]
    index = 0
    while index < len(name):
        if name[index] == ' ':
            result += '.' + name[index + 1]
            return result.upper()
        index += 1


print(abbrev_name(init_name))
