#FizzBuzz
for x in range(0, 100):
    if x % 3 == 0 and x % 5 == 0:
        print('Fizz Buzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fizz')
    else:
        print(x)


