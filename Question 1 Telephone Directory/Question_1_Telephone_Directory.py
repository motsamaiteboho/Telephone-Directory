adress = input('Enter the address: ')

vowels = 'aeiouAEIOU'
string = ''
for letter in adress:
    if letter  in vowels:
        if adress[0] == letter:
            string = string + letter
    if letter not in vowels:
        string = string + letter

print(string)
