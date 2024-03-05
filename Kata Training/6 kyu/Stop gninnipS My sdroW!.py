def spin_words(sentence):
    sentence_split = sentence.split()
    for i in range(len(sentence_split)):
        if len(sentence_split[i]) >= 5:
            sentence_split[i] = sentence_split[i][::-1]
    return " ".join(sentence_split)
