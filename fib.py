n1, n2 = 1,2

terms = int(input("Enter how many terms\n"))
terms = terms - 2
   #   print(f"{n1}\n{n2}")
flag = False

for count in range(terms):
    if flag == False:
        print(f"{n1}\n{n2}")
        flag = True

    n3 = n1 + n2
    print(n3)

    n1 = n2
    n2 = n3