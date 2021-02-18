def calendar(m):
    months = ["january", "febuary", "march","april","may","june","july","august","september","october","november","december"]
    for i in range(0,len(months)):
        if m == months[i]:
            return i + 1

    return m + " is not a month"

print(calendar("winter"))
