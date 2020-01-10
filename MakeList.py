# Make list numbers

def MakeList():
    A = []
    print('Enter "q" for exit')
    print('Enter a number:')
    x = input()

    while x != 'q' and x != 'Q':
        try:
            A.append(int(x))
        except:
            print(x + ' not a number')
        x = input()
    print('Your list is: ', A)
