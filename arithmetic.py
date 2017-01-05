def add(num_list):


    return reduce(lambda x, y: int(x)+int(y), num_list)

#    total = 0
#    for num in num_list:
#        total += int(num)
#    return total


def subtract(num_list):

    return reduce(lambda x, y: int(x)-int(y), num_list)

#    total = int(num_list[0])
#    for num in num_list[1:]:
#        total = total - int(num)
#    return total


def multiply(num_list):

    return reduce(lambda x, y: int(x)*int(y), num_list)

#    total = int(num_list[0])
#    for num in num_list[1:]:
#        total = total * int(num)
#    return total


def divide(num_list):
    # Need to turn at least argument to float for division to
    # not be integer division

    return reduce(lambda x, y: int(x)/int(y), num_list)

#    total = float(num_list[0])
#    for num in num_list[1:]:
#        total = total / float(num)
#    return total


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num_list):
    total = int(num_list[0])
    for num in num_list[1:]:
        total = total ** int(num)  # ** = exponent operator
    return total


def mod(num_list):
    total = int(num_list[0])
    for num in num_list[1:]:
        total = total % int(num)
    return total

