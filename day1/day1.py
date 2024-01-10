def sum_values(input_list):
    sum = 0
    for line in input_list:
        nums = []
        for letter in line: 
            if letter.isnumeric():
                nums.append(letter)

        sum += int(nums[0] + nums[-1])
    return sum



# part two calibration values
def sum_values_part2(input_list):
    sum = 0
    integernames = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for inp in input_list:
        nums = []
        for i, letter in enumerate(inp):
            for val, name in enumerate(integernames):
                if name in inp [i:i+len(name)]:
                    nums.append(str(val))
            if ord(letter)<= 57:
                nums.append(letter)

        sum += int(nums[0] + nums[-1])
    return sum

if __name__ == "__main__":
    file = open("day1/aoctest1.txt", "r")
    input = file.read()
    input_list = input.split('\n')
    sum = sum_values(input_list) 
    print(f"this is the return from test {sum}")
   
    file = open("day1/input.txt", "r")
    input = file.read()
    input_list = input.split('\n')
    sum = sum_values(input_list) 
    print(f"this is the return from input list {sum}")

    file = open("day1/test.txt", "r")
    input = file.read()
    input_list = input.split('\n')
    sum = sum_values_part2(input_list) 
    print(f"this is the return from part 2 test {sum}")

    file = open("day1/input.txt", "r")
    input = file.read()
    input_list = input.split('\n')
    sum = sum_values_part2(input_list) 
    print(f"this is the return from part 2 input list {sum}")