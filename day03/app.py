import re


def part_one(memories):
    # Define a regex pattern for mul(X,Y) where X and Y are integers
    pattern = r"mul\((\d+),(\d+)\)"

    # Find all matches for the mul(X,Y) pattern in the corrupted input
    matches = re.findall(pattern, memories)

    # Sum the products of each mul instruction
    total_sum = 0
    for match in matches:
        x, y = int(match[0]), int(match[1])
        total_sum += x * y

    print(
        f"What do you get if you add up all of the results of the multiplications? {total_sum}"
    )


def part_two(memories):
    pattern = r"mul\((\d+),(\d+)\)"

    enabled = True
    total_sum = 0

    instructions = re.split(r"(do\(\)|don't\(\))", memories)

    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        else:
            matches = re.findall(pattern, instruction)
            for match in matches:
                if enabled:
                    x, y = int(match[0]), int(match[1])
                    total_sum += x * y

    print(
        f"what do you get if you add up all of the results of just the enabled multiplications? {total_sum}"
    )


if __name__ == "__main__":
    # Read the input from the file
    with open(file="input.txt") as f:
        memories = f.read()

    # Get the result from part one and print it
    result = part_one(memories=memories)
    result = part_two(memories=memories)
