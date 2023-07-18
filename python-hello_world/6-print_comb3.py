for i in range(10):
    for j in range(i + 1, 10):
        print("{:02}".format(i), end=", " if j < 9 else "\n")
