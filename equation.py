import sys, getopt

# Stores the solved equations
sovled_eq_dict = {}
# Store the input equations
unsovled_eq_dict = {}

# Custom test cases are read here
options, remainder = getopt.getopt(sys.argv[1:], 'i', ['ifile='])
if options:
    try:
        with open(options[0][1]) as input_file:
            test_equations = input_file.read().splitlines()
    except Exception as error:
        print('filename not recognized')

else:
    test_equations = [
        'offset = 4 + random + 1', 
        'location = 1 + origin + offset', 
        'origin = 3         + 5', 
        'random = 2',
    ]


def decypher_equation_string():
    unsolved_eq_dict = {}
    for test_equation in test_equations:
        formatted_equation = test_equation.replace(" ", "")
        left_hand_side, right_hand_side = tuple(formatted_equation.split("="))
        right_hand_side = right_hand_side.split("+")
        unsolved_eq_dict[left_hand_side] = right_hand_side

    return unsolved_eq_dict


def solve_for_variable(variable):
    variable_eq = unsovled_eq_dict[variable]
    result = 0

    for value in variable_eq:
        if value == variable:
            raise Exception("infinite loop %s = %s" % (value, variable))

        if not value.isalpha():
            result += int(value)
            continue
        
        if value not in sovled_eq_dict:
            solve_for_variable(value)

        result += sovled_eq_dict[value]

    sovled_eq_dict[variable] = result


if __name__ == "__main__":
    answers = []
    unsovled_eq_dict = decypher_equation_string()
    variables = sorted(list(unsovled_eq_dict.keys()))

    # Depth First Search Approach
    for variable in variables:
        try:
            solve_for_variable(variable)
            answer_string = "%s = %s\n" % (variable, sovled_eq_dict[variable])
            answers.append(answer_string)
        except Exception as error:
            print(error)
            break

    answer_file = open('answers.txt', 'w')
    answer_file.writelines(answers)
    answer_file.close()