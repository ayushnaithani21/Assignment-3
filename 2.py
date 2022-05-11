a = int(input('Enter first number: '))
operator = input('Enter operator\n1. add\t2. subtract\t3. multiply\t4. division\t5. floor division\t6. modulus\n')
b = int(input('Enter second number: '))

if int(operator) == 1:
    print('Result = ' + str(a + b))
elif int(operator) == 2:
    print('Result = ' + str(a - b))
elif int(operator) == 3:
    print('Result = ' + str(a * b))
elif int(operator) == 4:
    print('Result = ' + str(a / b))
elif int(operator) == 5:
    print('Result = ' + str(a // b))
else:
    print('Result = ' + str(a % b))