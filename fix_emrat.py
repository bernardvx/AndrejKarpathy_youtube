# Open the input file in read mode
with open('emrat_e_plote.txt', 'r') as file:
    # Read the content of the file
    file_content = file.read()
    
# Split the content into words
words = file_content.split()

keq  = ['À', 'Å', 'È', 'É', 'Ê', 'Ì', 'Í', 'Ò', 'Ó', 'Ö', 'Û', 'Ü']
for word in words:
    for i in keq:
        if i in word:
            words.remove(word)
# Convert each word to lowercase
    #lowercase_words = word.lower()

# Join the lowercase words back into a string
lowercase_content = ' '.join(words)

# Open the output file in write mode
with open('emrat_e_plotev2.txt', 'w') as file:
    # Write the modified content to the output file
    for a in lowercase_content.split():
        file.write(f'\n{a}')
