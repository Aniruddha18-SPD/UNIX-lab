import sys

def cipher(num):
    message = input()
    final_result = ""
    main_result = ''
    count = 1

    uppercase_message = message.upper() #convert to uppercase

    for letter in uppercase_message:

        if letter.isalpha():    # discard anything besides letters and words


            final_result += chr(((ord(letter) + num)-65) % 26 + 65) #Encoding each letter by shifting s amount

    final_result = [final_result[i:i+5] for i in range(0, len(final_result), 5)]  #final encoded message in blocks of five letters to the screen

    # count = 0

    for each_value in final_result:
        if count % 10 != 0:
            main_result += each_value + ' '
        else:
            main_result += each_value +'\n'
        count += 1    
    return (main_result)


number = int(sys.argv[1]) #enter the number to shift each letter 

print(cipher(number))

