import sys

def decoder(message, passcode):
    characters = list(message)

    for i in range(len(characters)):
        character = characters[i]

        if character.isalpha():
            character_num = ord(character)
            character_num += passcode

            if character_num > 90:
                excess = character_num - 90
                character_num = 64 + excess

            characters[i] = chr(character_num)

    print ''.join(characters)

if __name__ == '__main__':
    message = sys.argv[1]
    passcode = int(sys.argv[2])
    decoder(message, passcode)
