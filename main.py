# bodmas calculator
# add function

operations_list = ("+", "-", "*", "/", "(", ")", "of")


def addition(*args):
    total = 0
    for x in args:
        total += x
    return total


def multiply(*args):
    product = 1
    for x in args:
        product *= x
    return product


def division(initial, *args):
    for x in args:
        initial /= x
    return initial


def subtract(initial, *args):
    for x in args:
        initial -= x
    return initial


# dealing with brackets
def string_break(sequence):
    # fetching operators
    ops_indexes = {}
    # add indexes to list for slicing for values
    indexes = []
    for ind, value in enumerate(sequence):
        if value in operations_list:
            x_index = ind
            new_dict = {x_index: value}
            ops_indexes.update(new_dict)
            indexes.append(ind)
    print(f"operators: {ops_indexes}")

    # todo fetching values
    # slicing at the indexes[]
    start = 0
    count = 0
    values_list = []

    # TODO account for start having an operator
    for i in indexes:
        v = sequence[start:i]
        start = i + 1
        values_list.append(v)

    # account for the value after the last operator

    indexes_length = len(indexes)
    fin_index = indexes[indexes_length - 1]
    last_value = sequence[fin_index + 1:]
    values_list.append(last_value)
    print(f"values : {values_list}")


string_break("378+76+7")


def brackets_operation(tuple1):
    for x in tuple1:
        if x in operations_list:
            operator = x
            # concatenate everything before the operator
            index1 = tuple1.index(x)
            num1 = tuple1[:index1]
            print(f" num 1 : {num1}")
            # num1 = int(num1)
            temp = tuple1[index1 + 1:]
            for y in temp:
                # print(y)
                if y in operations_list:
                    index2 = tuple1.index(y)
                    # concatenate everything between the operators
                    num2 = tuple1[index1 + 1:index2]
                    print(num2)
                    break
                    # print out the operation


calculation = input("enter a calculation : \n")
print(calculation)

# separating the operators from the numbers
index = 0
for x in calculation:
    # check for brackets
    if x == "(":
        first_index = calculation.index(x)
        for y in calculation[index:]:
            if y == ")":
                last_index = calculation.index(y)
                brackets = calculation[first_index:last_index + 1]
