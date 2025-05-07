def parseInput() -> list[list[int]]:
    reports: list[list[int]] = []
    for line in open(0):
        reports.append([int(levels) for levels in line.split()])

    return reports


if __name__ == "__main__":
    safe_reports = 0

    for report in parseInput():
        safe = True

        if not (report == sorted(report) or report == list(reversed(sorted(report)))):
            continue

        for level, next_level in zip(report, report[1:]):
            if not (3 >= abs(level - next_level) and abs(level - next_level) >= 1):
                safe = False
                continue

        if safe:
            safe_reports += 1

    print(safe_reports)
