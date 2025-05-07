def parseInput() -> list[list[int]]:
    reports: list[list[int]] = []
    for line in open(0):
        reports.append([int(levels) for levels in line.split()])

    return reports


def isSafe(report: list[int], tolerance=True) -> bool:
    ascending = True
    descending = True
    for level, next_level in zip(report, report[1:]):
        if level > next_level:
            ascending = False
        if level < next_level:
            descending = False

    if not (ascending or descending):
        return False

    for level, next_level in zip(report, report[1:]):
        if not (3 >= abs(level - next_level) and abs(level - next_level) >= 1):
            return False

    return True


if __name__ == "__main__":
    safe_reports = 0

    for report in parseInput():
        for i in range(len(report)):
            if isSafe(report[:i] + report[i + 1 :]):
                safe_reports += 1
                break

    print(safe_reports)
