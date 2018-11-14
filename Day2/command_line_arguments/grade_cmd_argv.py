import sys
print(sys.argv)

grade = int(sys.argv[3])

if grade >= 90:
    if grade == 100:
        print('A+')
    else:
        print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
else:
    print('F')