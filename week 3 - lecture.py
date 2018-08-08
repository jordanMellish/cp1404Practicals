import string

def count_characters(text):
    count = 0
    for character in text:
        if character.lower() in string.ascii_lowercase:
            count += 1
    return count

text = 'Blah'
total = count_characters(text)
print(total)