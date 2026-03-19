def marcsCakewalk(calorie):
    # Write your code here
    calorie.sort(reverse = True)
    res = 0
    for i in range(len(calorie)):
        res += (2 ** i) * calorie[i]
    return res