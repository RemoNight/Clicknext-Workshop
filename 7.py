x = int(input("Input: "))

hour = x // 3600
temp = x - (3600 * hour)
minutes = temp // 60
second = temp - (60 * minutes)

print("{0:02d}:{1:02d}:{2:02d}".format(hour, minutes, second))
