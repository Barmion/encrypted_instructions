# Номер успешной посылки 123843066

def decrypt(short_message: str) -> str:
    short_message = short_message.replace('[', '*(')
    short_message = short_message.replace(']', ')+')
    full_message = ''
    for i in short_message:
        if i.isalpha():
            i = '"' + i + '"+'
            if full_message:
                if full_message[-1].isnumeric():
                    i = '*' + i
        full_message += i
    full_message = full_message.replace('+)', ')')
    full_message = full_message.rstrip('+')
    return eval(full_message)


def main():
    short_message = input()
    print(decrypt(short_message))


if __name__ == '__main__':
    main()
