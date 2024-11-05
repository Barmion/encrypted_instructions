# Номер успешной посылки 123760667

def decrypt(short_message: str) -> str:
    full_message = [short_message[0]]
    multiple = ''
    for i in short_message[1:]:
        if i.isalpha():
            while full_message[-1].isdigit():
                multiple = full_message.pop() + multiple
                if not full_message:
                    break
        if multiple:
            full_message += i * int(multiple)
            multiple = ''
        else:
            full_message += i
        if i == ']':
            bracket = ''
            full_message.pop()
            while full_message[-1] != '[':
                bracket = full_message.pop() + bracket
            full_message.pop()
            while full_message[-1].isdigit():
                multiple = full_message.pop() + multiple
                if not full_message:
                    break
            full_message += bracket * int(multiple)
            multiple = ''
    return ''.join(full_message)


def main():
    short_message = input()
    print(decrypt(short_message))


if __name__ == '__main__':
    main()
