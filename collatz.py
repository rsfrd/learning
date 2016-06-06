def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
print("Please type a number: ")
userInt = int(input())
newInt = collatz(userInt)
print(collatz(userInt))
while collatz(newInt) > 1:
    newInt = collatz(newInt)
    print(collatz(newInt))
