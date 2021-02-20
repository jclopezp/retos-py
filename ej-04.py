## Solución 1
def format_number(number):
    numero = "{:,}".format(number)
    return numero


format_number(12345467890)

## Solución 2
def group(number):
    num = "%d" % number
    groups = []
    while num and num[-1].isdigit():
        groups.append(num[-3:])
        num = num[:-3]
    return num + ",".join(reversed(groups))


group(-12345467890)