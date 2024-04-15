while True:
    prompt = input("\n Hello to Sudoku valitator,"
    "\n \n Please type in the path to your file and press 'Enter': ")
    try:
        sudoku = open(prompt, 'r').readlines()
    except FileNotFoundError:
        print("Wrong file or file path")
    else:
        break