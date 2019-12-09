
def intcode_string_to_list(intcode_string):
    assert type(intcode_string) is str
    intcode_string_list = intcode_string.split(",")
    intcode_list = list(map(int, intcode_string_list))
    return intcode_list


def run_intcode(intcode):
    # convert input into list of integers
    if type(intcode) is str:
        intcode_list = intcode_string_to_list(intcode)
    else:
        intcode_list = intcode

    pos = 0

    # get next instruction
    instruction = str(intcode_list[pos])

    # only takes last digit (works if second-last digit is 0)
    opcode = int(instruction[-2:])

    relative_base = 0

    while opcode != 99 and pos < len(intcode_list):
        # get mode - 0 is position mode, 2 is immediate mode, 3 is relative mode
        print(relative_base)
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
            elif first_mode is 2:
                first = intcode_list[pos + 1] + relative_base
            if second_mode is 0:
                second = intcode_list[pos + 2]
            elif second_mode is 1:
                second = pos + 2
            elif second_mode is 2:
                second = intcode_list[pos + 2] + relative_base
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
            calculated_value = int(input("Enter input: "))
            intcode_list[first] = calculated_value
            pos += 2
        elif opcode == 4:
            # outputs the value of its only parameter
            print(intcode_list[first])
            # pos += 2
            # return intcode_list[first], intcode_list, pos, inputs_entered, False
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
        elif opcode == 9:
            # offset relative base
            relative_base += first
            pos += 2
        else:
            print("opcode ", opcode, "?")
            print(intcode_list)
            return
        instruction = str(intcode_list[pos])
        opcode = int(instruction[-2:])
    # return amp_input, intcode_list, pos, inputs_entered, True


data = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
run_intcode(data)
