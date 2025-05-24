# Test for trying to iterate with negative indexes through a string

a = "abcde"

for i in range(len(a)):
    print(a[len(a) - (i + 1)])
