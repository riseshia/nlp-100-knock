def merge_str(str1, str2):
    l = ''
    for t in zip(str1, str2):
        l += ''.join(t)

    return l
