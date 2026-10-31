
count = 0

def hanoi(n, a, b, c):
    global count

    if n == 1:
        count += 1
        print(count, "Move disk 1 from", a, "to", c)
        return

    hanoi(n-1, a, c, b)

    count += 1
    print(count, "Move disk", n, "from", a, "to", c)

    hanoi(n-1, b, a, c)

n = int(input("Enter number of disks: "))
hanoi(n, 'A', 'B', 'C')
print("Total moves:", count)
