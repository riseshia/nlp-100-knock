def n_gram(target, n, tokenizer=''):
    result_size = len(target) - n + 1
    return [tokenizer.join(target[i:i+n]) for i in range(result_size)]
