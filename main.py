from func import *

while True:
    clear_screen()
    print_logo()
    print_menu()
    choice = input("")
    if choice == "1":
        generatePass = True
        clear_screen()
        while generatePass:
            clear_screen()
            print_logo()
            length = get_pass_length()
            want_capital = colored_input("Do you want capital letters in your password? (y/n) ")
            want_numbers = colored_input("Do you want numbers in your password? (y/n) ")
            want_symbols = colored_input("Do you want symbols in your password? (y/n) ")

            password = generate_password(length, want_capital, want_numbers, want_symbols, letters, capital_letters, numbers, symbols)

            check_strength(length, want_capital, want_numbers, want_symbols)

            print(COLORS.BLUE + "Password: " + COLORS.RESET + password)
            want_save = input("Do you want to save this password? (y/n)").lower() == 'y'
            if want_save:
                with open("passwords.txt", "a") as file:
                    file.write(password + "\n")
            generatePass = input("Do you want to generate another password? (y/n)").lower() == 'y'
            clear_screen()
        continue
    elif choice == "2":
        goBack = True
        while goBack:
            clear_screen()
            print_logo()
            print("Your saved" + COLORS.BLUE + " passwords" + COLORS.RESET + ":")
            with open("passwords.txt", "r") as file:
                print(file.read())
            goBack = input("Do you want to go back? (y/n)")
            if goBack.lower() == "y":
                goBack = False
                clear_screen()
                break
            else:
                goBack = True
            clear_screen()
        continue
    elif choice == "3":
        clear_screen()
        break



    

