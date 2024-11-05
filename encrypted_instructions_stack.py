# Номер успешной посылки 123867589

from collections import deque


def decrypt(short_message: str) -> str:
    full_message, multiple = '', 0
    stack = deque()
    for i in short_message:
        if i.isalpha():
            full_message += i
        elif i.isdigit():
            multiple = multiple * 10 + int(i)
        elif i == '[':
            stack.append((full_message, multiple))
            full_message, multiple = '', 0
        elif i == ']':
            first_part, multiple = stack.pop()
            full_message = first_part + multiple * full_message
            multiple = 0
    return full_message


def main():
    short_message = input()
    print(decrypt(short_message))


if __name__ == '__main__':
    main()
    
