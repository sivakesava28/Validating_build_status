import sys


def read_line(filename):
    fd = open(filename, "r")
    count = 0
    substring = "warning"

    while(True):
        data = fd.readline()
        if (data.find(substring) > 0):
            count = count + 1
        print("len :%d, %s" % (len(data), data))
        print("count:", count)
        if (len(data) <= 0):
            break
    fd.close
    return count
count1 = read_line(sys.argv[1])
count2 = read_line(sys.argv[2])

if (count2 > count1):
    print("reject")
else:
    print("pass")
