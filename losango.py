size = int(input("Size of diamont (only odd numbers): "))
if (size % 2 == 1):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letterCounter = 0
    x = 1
    while (x < (size // 2) + 1):
        y = 1
        z = x * 2 - 1
        while (y <= size):
            lowerLimit = ((size // 2) + 1) - (z // 2)
            upperLimit = ((size // 2) + 1) + (z // 2)
            if (y >= lowerLimit and y <= upperLimit):
                print(alphabet[letterCounter], end='')
            else:
                print(' ', end='')
            y = y + 1
        print('')
        x += 1
        letterCounter += 1
        if (letterCounter + 1 > len(alphabet)):
            letterCounter = 0

    x = (size // 2) + 1
    while (x > 0):
        y = 1
        z = x * 2 - 1
        while (y <= size):
            lowerLimit = ((size // 2) + 1) - (z // 2)
            upperLimit = ((size // 2) + 1) + (z // 2)
            if (y >= lowerLimit and y <= upperLimit):
                print(alphabet[letterCounter], end='')
            else:
                print(' ', end='')
            y = y + 1
        print('')
        x -= 1
        letterCounter += 1
        if (letterCounter + 1 > len(alphabet)):
            letterCounter = 0
else:
    print("Not odd number! EXIT!!!!")