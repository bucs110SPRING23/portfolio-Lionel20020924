def star_pyramid():
    rows = int(input("请输入行数: "))
    for i in range(rows):
        print(" "*(rows-i-1) + "*"*(2*i+1))

def rstar_pyramid():
    num_rows = int(input("请输入行数："))
    for i in range(num_rows, 0, -1):
        for j in range(0, i):
            print("*", end="")
        print()
