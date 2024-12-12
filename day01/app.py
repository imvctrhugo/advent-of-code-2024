def part_one(left_list: list[int], right_list: list[int]):
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    distances: list[int] = []
    for left, right in zip(sorted_left, sorted_right, strict=True):
        distance = right - left
        if distance < 0:
            distance *= -1
        distances.append(distance)

    sum: int = 0
    for distance in distances:
        sum += distance

    print(f"Total distance between the lists: {sum}")


def part_two(left_list: list[int], right_list: list[int]):
    similarity_score: int = 0

    for left in left_list:
        appearances = 0  # how often each number appears
        for right in right_list:
            if left == right:
                appearances += 1
        similarity_score += left * appearances

    print(f"The similarity score is: {similarity_score}")


if __name__ == "__main__":
    left, right = map(
        list, zip(*[map(int, line.split()) for line in open("input.txt")])
    )
    part_one(left, right)
    part_two(left, right)
