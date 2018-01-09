def encode(text):
    return ''.join([trans_char(c) for c in text])


def decode(text):
    return ''.join([trans_char(c) for c in text])


def trans_char(char):
    if char.islower():
        return chr(219 - ord(char))
    else:
        return char
