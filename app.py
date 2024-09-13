print("Running the doohickie")
for i in range(3):
    word = 'No input given'

    try:
        word = input("Enter any string: ")
        while len(word) < 3:
            word = input("Enter any string: ")
    except EOFError: 
        print(word)

    print("Your word reversed: " + word[::-1])
