attendance_log = [True, False, True, True, False]

days_present = attendance_log.count(True)


total_days = len(attendance_log)
attendance_percentage = (days_present / total_days) * 100

print("Days Present:", days_present)
print("Attendance Percentage:", str(round(attendance_percentage)) + "%")
