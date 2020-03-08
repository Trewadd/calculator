value_dict = {}
list_elements = []


def add_spaces(new_value):
    value = ''
    prev_aln = False
    for element in new_value:
        if not element.isalnum():
            value += f' {element}'
            prev_aln = True
            continue
        else:
            if prev_aln:
                value += f' {element}'
                prev_aln = False
            else:
                value += element
    return value


while True:
    message = ''
    new_list_elements = []
    value = input()

    if len(value) == 0:  # check input length
        continue

    if value[0] is '/':  # check the commands
        if '/exit' in value:
            print('Bye!')
            break
        elif '/help' in value:
            print('Some help information')
        else:
            print('Unknown command')
            continue

    value = add_spaces(value)
    list_elements = [x for x in value.split()]

    if list_elements[0].isalpha() and len(list_elements) == 1:  # print variable
        if list_elements[0] in value_dict:
            print(value_dict[list_elements[0]])
        else:
            print('Unknown variable')
        continue

    elif list_elements[0].isalpha():  # save variable to dict
        if list_elements[1] == '=':
            if not list_elements[2].isdigit() and not list_elements[2].isalpha():
                print('Invalid assignment')
            if (list_elements[0].islower() ^ list_elements[0].isupper())\
                    and len(list_elements) == 3:
                if list_elements[2].isalpha():
                    value_dict[list_elements[0]] = value_dict[list_elements[2]]
                else:
                    value_dict[list_elements[0]] = list_elements[2]
            else:
                print('Invalid assignment')
            continue
    elif not list_elements[0].isdigit():
        print('Invalid identifier')
        continue
    for element in list_elements:  # change variable to value
        if element in value_dict:
            new_list_elements.append(value_dict[element])
        else:
            new_list_elements.append(element)
    list_elements = new_list_elements.copy()
    value = ''
    for element in list_elements:  # convert from list to str
        value += element

    try:  # calculation
        print(int(eval(value)))
    except SyntaxError:
        print('Invalid expression')
