base = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

one_char_idx = [0, 4, 5, 6, 7, 8, 14, 15, 18]

def element_dic():
    abbrs = [word[0:2] for word in base.split(' ')]

    for idx in one_char_idx:
        abbrs[idx] = abbrs[idx][0]

    return {abbrs[i]: i + 1 for i in range(len(abbrs))}
