num1 = int(input("Enter the FROM range: "))
num2 = int(input("Enter the TO range: "))
for i in range(num1,num2): # range(n1, n2-1)
    if i in range(11, 21):
        continue # skip

    if i == 33:
        pass

    print(i)

    if i == 90:
        break # cancel the execution of loop
    