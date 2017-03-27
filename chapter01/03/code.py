def char_count(sentence):
    words = sentence.split(' ')
    return [(word, len(word)) for word in words]
