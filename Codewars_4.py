string = "1 shot, 5 beers and 1 glass of wine"


def hydrate(drink_string):
    summ = 0
    a = drink_string.split()
    for i in a:
        if len(i) == 1:
            summ += int(i)
    if summ > 1:
        return f'{summ} glasses of water'
    else:
        return f'{summ} glass of water'


print(hydrate(string))
