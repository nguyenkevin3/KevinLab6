# Kevin Nguyen's password encoder

def encode(password):
    encoded_pass = ''

    for i in password:
        i = int(i)
        i += 3

        if i > 10:
            i -= 10

        encoded_pass += str(i)

    return encoded_pass

def main():
    run_menu = True

    while run_menu:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        user_input = int(input("Please enter an option: "))

        if user_input == 1:
            original_password = input("Please enter your password to encode: ")

            encoded_password = encode(original_password)

            print(encoded_password)

            print("Your password has been encoded and stored!\n")

        elif user_input == 2: # PARTNER: Add your code here and create decoder function above! The decoded password is already stored in original_password.
            pass


        elif user_input == 3:
            run_menu = False


if __name__ == '__main__':
    main()



