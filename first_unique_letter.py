# Create a function that will take a string as an input and return the 1st non-unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?


a = 'Google'


def firstunique(string):
    uniq_letter = {}
    for char in string.lower():
        if char not in uniq_letter:
            uniq_letter[char] = 1
        else:
            uniq_letter[char] += 1
    for i in uniq_letter:
        if uniq_letter.get(i) == 1:
            return i
    return ""


print(firstunique(a))
