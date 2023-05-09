no_of_rows = int(input("enter no of rows \t"))
print(no_of_rows)

array =  []
for i in range(no_of_rows):
    a,b = list(map(int,input().split()))
    print(" a is {} b is {}".format(a,b))
    array += [[(a+b),a,b]]
    print(array)
    array.sort(reverse = False)
    print("reverse sort is {}".format(array))

