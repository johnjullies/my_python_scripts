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

    print 'Decoded message: %s' % (''.join(characters))

def main():
    message = raw_input('Enter message to decode: ')
    passcode = input('Enter the passcode: ')

    print 'Decoding...'

    decoder(message, passcode)

if __name__ == '__main__':
    main()
