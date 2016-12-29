import sys

def message_coder(message, passcode):
    characters = list(message)

    for i in range(len(characters)):
        character = characters[i]

        if character.isalpha():
            character_num = ord(character)
            character_num -= passcode

            if character_num < 65:
                less = 65 - character_num
                character_num = 91 - less

            characters[i] = chr(character_num)

    print ''.join(characters)

if __name__ == '__main__':
    message = sys.argv[1]
    passcode = int(sys.argv[2])
    message_coder(message, passcode)
