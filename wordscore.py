def score_word(word):
    """
    @ params
    word => a tuple containing the word to be scored and wildcard letters to be subtracted from score

    scores words based on predetermined letter values. 
    returns a tuple of score, word
    """
    
    # ensure letters are cased properly for score dictionary
    scrabble_word = word[0].lower()
    wildcard_replacer = ''.join(word[1])
    wildcard_replacer = wildcard_replacer.lower()

    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10}
    
    # determine the score for each word independent of wildcards
    word_score = 0
    for letter in scrabble_word:
        word_score += scores[letter]

    # subtract value of wildcard letters, stored as values
    if len(word[1]) > 0:
        for letter in wildcard_replacer:
            word_score -= scores[letter]

    scrabble_word = scrabble_word.upper()
    pair = word_score, scrabble_word

    return(pair)