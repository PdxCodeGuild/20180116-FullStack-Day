yDis = float(input("what is the distance?:"))
yUnit = input("what are the input units:")
yOut = input("what are the output units?")


def fttransfter(yOut, yDis):
    if yOut == 'ft':
        out = yDis
    elif yOut == 'mi':
        out = (1 / 5280) * yDis
    elif yOut == 'm':
        out = 0.3048 * yDis
    elif yOut == 'km':
        out = 0.0003048 * yDis
    else:
        print('the units cannot read')
        return None

    return out


def transfer(yUnit, yOut, yDis):
    if yUnit == 'ft':
        ftDis = yDis
    elif yUnit == 'm':
        ftDis = yDis * (1 / 0.3048)
    elif yUnit == 'km':
        ftDis = yDis * (1000 / 0.3048)
    elif yUnit == 'mi':
        ftDis = yDis * 5280
    else:
        print('no unit')
        return None
    return fttransfter(yOut, ftDis)


out = transfer(yUnit, yOut, yDis)
print(out)
