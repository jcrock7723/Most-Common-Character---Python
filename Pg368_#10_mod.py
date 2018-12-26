# Unit 8, pg368, #10
# This function displays the character that appears the most
# frequently in the sring. If several characters have the same
# highest frequency, it displays the first character with that frequency

def main():
    count=[0]*26
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = 0
    frequent = 0

    # Recieve user input
    user_string = input('Enter a string statement: ')
    for ch in user_string:
        ch = ch.upper()

        # Determing which letter this character is
        # in your substring
        index = letters.find(ch)
                    
        if index >= 0:
            print(index)
            print(count)
            dummy=input('press any key...')

            # increase the counting array for this letter
            count[index] += 1

    # Find out where it lives
    for i in range(len(count)):
        if count[i] > count[frequent]:
            frequent = i

    print('The character that appears most frequently' \
          ' in the string is ', letters[frequent], '.', \
          sep='')

    print('It appears', count[frequent], 'times within your statement.')
    
        
# Call the main function
main()
