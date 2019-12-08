
import itertools


def intcode_string_to_list(intcode_string):
    assert type(intcode_string) is str
    intcode_string_list = intcode_string.split(",")
    intcode_list = list(map(int, intcode_string_list))
    return intcode_list


def run_intcode(intcode, amp_input, phase_setting, pos=0, inputs_entered=0):
    # convert input into list of integers
    intcode_list = intcode_string_to_list(intcode)

    # get next instruction
    instruction = str(intcode_list[pos])

    # only takes last digit (works if second-last digit is 0)
    opcode = int(instruction[-2:])

    while opcode != 99 and pos < len(intcode_list):
        # get mode
        try:
            first_mode = int(instruction[-3])
        except IndexError:
            first_mode = 0
        try:
            second_mode = int(instruction[-4])
        except IndexError:
            second_mode = 0
        # get parameters based on mode
        try:
            if first_mode is 0:
                first = intcode_list[pos + 1]
            elif first_mode is 1:
                first = pos + 1
            if second_mode is 0:
                second = intcode_list[pos + 2]
            elif second_mode is 1:
                second = pos + 2
            third = intcode_list[pos + 3]
        except IndexError:
            pass

        # execute instructions
        if opcode == 1:
            # adds together numbers read from two positions and stores the result in a third position
            calculated_value = intcode_list[first] + intcode_list[second]
            intcode_list[third] = calculated_value
            pos += 4
        elif opcode == 2:
            # multiplies numbers read from two positions and stores the result in a third position
            calculated_value = intcode_list[first] * intcode_list[second]
            intcode_list[third] = calculated_value
            pos += 4
        elif opcode == 3:
            # takes a single integer as input and saves it to the position given by its only parameter
            if inputs_entered == 0:
                calculated_value = phase_setting
            elif inputs_entered == 1:
                calculated_value = amp_input
            else:
                calculated_value = int(input("Enter input: "))
            intcode_list[first] = calculated_value
            pos += 2
            inputs_entered += 1
        elif opcode == 4:
            # outputs the value of its only parameter
            pos += 2
            return intcode_list[first]
        elif opcode == 5:
            # if first parameter non-zero, set instruction pointer to value from second parameter
            if intcode_list[first] != 0:
                pos = intcode_list[second]
            else:
                pos += 3
        elif opcode == 6:
            # if first parameter non-zero, set instruction pointer to value from second parameter
            if intcode_list[first] == 0:
                pos = intcode_list[second]
            else:
                pos += 3
        elif opcode == 7:
            # if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
            if intcode_list[first] < intcode_list[second]:
                intcode_list[third] = 1
            else:
                intcode_list[third] = 0
            pos += 4
        elif opcode == 8:
            # if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            if intcode_list[first] == intcode_list[second]:
                intcode_list[third] = 1
            else:
                intcode_list[third] = 0
            pos += 4
        else:
            print("opcode ", opcode, "?")
            print(intcode_list)
            return
        instruction = str(intcode_list[pos])
        opcode = int(instruction[-2:])


def test_setting(param):
    data = "3,8,1001,8,10,8,105,1,0,0,21,42,67,88,101,114,195,276,357,438,99999,3,9,101,3,9,9,1002,9,4,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,101,4,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99"
    a = run_intcode(data, 0, param[0])
    b = run_intcode(data, a, param[1])
    c = run_intcode(data, b, param[2])
    d = run_intcode(data, c, param[3])
    e = run_intcode(data, d, param[4])
    return e


possible_params = list(itertools.permutations([0, 1, 2, 3, 4]))

max_output = 0
for setting in possible_params:
    output = test_setting(setting)
    if output > max_output:
        max_output = output

print(max_output)
