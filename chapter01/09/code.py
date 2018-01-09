import random


def typoglycemia(text, seed=0):
    if len(text) <= 4:
        return text

    prefix, *middle, postfix = text
    random.seed(0)
    random.shuffle(middle)

    return ''.join([prefix, *middle, postfix])
