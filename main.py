# Kevin Nguyen's password encoder

def encode(password):
    encoded_pass = ''

    for i in password:
        i = int(i)
        i += 3

        if i >= 10:
            i -= 10

        encoded_pass += str(i)

    return encoded_pass

#Raiden Saunders' decoder
def decode(password): #just returns the original password ~ Raiden Saunders
    return password

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


            print("Your password has been encoded and stored!\n")

        elif user_input == 2: # Used decode funtion below to return the original password ~ Raiden Saunders
            original_pass = decode(original_password)
            print(f'The encoded pawword is {encoded_password}, and the original password is {original_pass}.')
            pass


        elif user_input == 3:
            run_menu = False


if __name__ == '__main__':
    main()



