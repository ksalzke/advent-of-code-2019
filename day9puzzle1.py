
def intcode_string_to_list(intcode_string):
    assert type(intcode_string) is str
    intcode_string_list = intcode_string.split(",")
    intcode_list = list(map(int, intcode_string_list))
    return intcode_list


def run_intcode(intcode):

    def add_memory(total_memory_needed):
        if (len(intcode_list) < total_memory_needed):
            for _ in range(len(intcode_list), total_memory_needed):
                intcode_list.append(0)

    # convert input into list of integers
    if type(intcode) is str:
        intcode_list = intcode_string_to_list(intcode)
    else:
        intcode_list = intcode

    pos = 0

    add_memory(20000)

    # get next instruction
    instruction = str(intcode_list[pos])

    # only takes last digit (works if second-last digit is 0)
    opcode = int(instruction[-2:])

    relative_base = 0

    while opcode != 99 and pos < len(intcode_list):
        # print(instruction)
        # get mode - 0 is position mode, 2 is immediate mode, 3 is relative mode
        # print(relative_base)
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
            # print(first)
            print(intcode_list[first])
            pos += 2
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


#data = "104,1125899906842624,99"
data = "1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,3,0,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,0,1,1020,1102,29,1,1001,1101,0,28,1016,1102,1,31,1011,1102,1,396,1029,1101,26,0,1007,1101,0,641,1026,1101,466,0,1023,1101,30,0,1008,1102,1,22,1003,1101,0,35,1019,1101,0,36,1018,1102,1,37,1012,1102,1,405,1028,1102,638,1,1027,1102,33,1,1000,1102,1,27,1002,1101,21,0,1017,1101,0,20,1015,1101,0,34,1005,1101,0,23,1010,1102,25,1,1013,1101,39,0,1004,1101,32,0,1009,1101,0,38,1006,1101,0,473,1022,1102,1,1,1021,1101,0,607,1024,1102,1,602,1025,1101,24,0,1014,109,22,21108,40,40,-9,1005,1013,199,4,187,1105,1,203,1001,64,1,64,1002,64,2,64,109,-17,2102,1,4,63,1008,63,32,63,1005,63,229,4,209,1001,64,1,64,1105,1,229,1002,64,2,64,109,9,21108,41,44,1,1005,1015,245,1105,1,251,4,235,1001,64,1,64,1002,64,2,64,109,4,1206,3,263,1105,1,269,4,257,1001,64,1,64,1002,64,2,64,109,-8,21102,42,1,5,1008,1015,42,63,1005,63,291,4,275,1105,1,295,1001,64,1,64,1002,64,2,64,109,-13,1208,6,22,63,1005,63,313,4,301,1105,1,317,1001,64,1,64,1002,64,2,64,109,24,21107,43,44,-4,1005,1017,339,4,323,1001,64,1,64,1105,1,339,1002,64,2,64,109,-5,2107,29,-8,63,1005,63,361,4,345,1001,64,1,64,1105,1,361,1002,64,2,64,109,-4,2101,0,-3,63,1008,63,32,63,1005,63,387,4,367,1001,64,1,64,1106,0,387,1002,64,2,64,109,13,2106,0,3,4,393,1001,64,1,64,1105,1,405,1002,64,2,64,109,-27,2102,1,2,63,1008,63,35,63,1005,63,425,1105,1,431,4,411,1001,64,1,64,1002,64,2,64,109,5,1202,2,1,63,1008,63,31,63,1005,63,455,1001,64,1,64,1106,0,457,4,437,1002,64,2,64,109,19,2105,1,1,1001,64,1,64,1105,1,475,4,463,1002,64,2,64,109,-6,21102,44,1,1,1008,1017,45,63,1005,63,499,1001,64,1,64,1105,1,501,4,481,1002,64,2,64,109,6,1205,-2,513,1106,0,519,4,507,1001,64,1,64,1002,64,2,64,109,-17,1207,-1,40,63,1005,63,537,4,525,1106,0,541,1001,64,1,64,1002,64,2,64,109,-8,1201,9,0,63,1008,63,38,63,1005,63,567,4,547,1001,64,1,64,1106,0,567,1002,64,2,64,109,-3,2101,0,6,63,1008,63,32,63,1005,63,591,1001,64,1,64,1105,1,593,4,573,1002,64,2,64,109,22,2105,1,8,4,599,1106,0,611,1001,64,1,64,1002,64,2,64,109,8,1206,-4,625,4,617,1105,1,629,1001,64,1,64,1002,64,2,64,109,3,2106,0,0,1106,0,647,4,635,1001,64,1,64,1002,64,2,64,109,-29,2107,27,9,63,1005,63,667,1001,64,1,64,1106,0,669,4,653,1002,64,2,64,109,7,1207,-4,28,63,1005,63,689,1001,64,1,64,1105,1,691,4,675,1002,64,2,64,109,-7,2108,30,3,63,1005,63,711,1001,64,1,64,1105,1,713,4,697,1002,64,2,64,109,17,21101,45,0,-5,1008,1010,45,63,1005,63,735,4,719,1106,0,739,1001,64,1,64,1002,64,2,64,109,-9,1202,-2,1,63,1008,63,39,63,1005,63,765,4,745,1001,64,1,64,1106,0,765,1002,64,2,64,109,10,21101,46,0,-5,1008,1011,48,63,1005,63,785,1106,0,791,4,771,1001,64,1,64,1002,64,2,64,109,-10,1208,0,36,63,1005,63,811,1001,64,1,64,1105,1,813,4,797,1002,64,2,64,109,7,1205,8,827,4,819,1105,1,831,1001,64,1,64,1002,64,2,64,109,-15,2108,27,4,63,1005,63,853,4,837,1001,64,1,64,1106,0,853,1002,64,2,64,109,14,1201,-3,0,63,1008,63,30,63,1005,63,877,1001,64,1,64,1106,0,879,4,859,1002,64,2,64,109,11,21107,47,46,-5,1005,1018,899,1001,64,1,64,1105,1,901,4,885,4,64,99,21101,0,27,1,21101,0,915,0,1105,1,922,21201,1,31783,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,0,942,0,1106,0,922,21201,1,0,-1,21201,-2,-3,1,21101,0,957,0,1105,1,922,22201,1,-1,-2,1106,0,968,22102,1,-2,-2,109,-3,2105,1,0"
run_intcode(data)
