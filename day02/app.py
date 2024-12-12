def is_report_safe(report: list[int]) -> bool:
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)

    return increasing or decreasing


def is_safe_dampener(report):
    if is_report_safe(report):
        return True

    # Try removing each level (one at a time) and check if the report becomes safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_report_safe(modified_report):
            return True

    return False


def part_one(reports: list[list[str]]):
    safe_count = 0
    for report in reports:
        if is_report_safe(report=report):
            safe_count += 1
    print(f"How many reports are safe? {safe_count}")


def part_two(reports: list[list[str]]):
    safe_count = 0
    for report in reports:
        if is_safe_dampener(report=report):
            safe_count += 1
    print(f"How many reports are safe? {safe_count}")


if __name__ == "__main__":
    with open(file="input.txt") as f:
        reports: list[list[int]] = [list(map(int, line.strip().split())) for line in f]

    part_one(reports=reports)
    part_two(reports=reports)
