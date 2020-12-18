from os import system, name

options = [quit, ]


if __name__ == "__main__":
    while True:
        system('cls' if name == 'nt' else 'clear')
        print("Digital ballot box")
        print('''
            (1) Vote
            (2) Count Votes

            (0) Exit program
            ''')

        opt = int(input('> '))

        system('cls' if name == 'nt' else 'clear')
        request = options[opt]()

        sock.send(str.encode(request))

    sock.close()
