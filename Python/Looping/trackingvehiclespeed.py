


def track_speed_violations(speed_log, speed_limit):
    violations = []

    for speed in speed_log:
        if (speed > speed_limit):
            violations.append(speed)

    print("Number of violations:", len(violations))
    print("Vehicles exceeding speed limit:", violations)



speed_log = list(map(int, input("Enter numbers separated by space: ").split()))
print("speed limits:", speed_log)
speed_limit = 50

track_speed_violations(speed_log, speed_limit)
