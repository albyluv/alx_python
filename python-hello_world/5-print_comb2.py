# This program prints all possible different combinations of two digits.
for i in range(0, 100):
    if i < 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))