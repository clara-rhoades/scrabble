def run_scrabble(rack):
    """
    @params
    rack => a string of 2-7 characters. must be letters (upper or lowercase) or wildcards (* and ?)
    only two wildcards (one of each type) permitted

    returns 
    - a set containing a list of tuples and an int representing the number of possible words
    - each tuple contains word's score, word
    - tuples are sorted by highest score and then alphabetically
    """

    # ERROR MESSAGES
    a = 'I found an unexpected character. Please ensure your input only contains letters and wildcards (* and/or ?)'
    b = 'Please enter at least 2 and no more than 7 characters'
    c = 'Please enter no more than two wildcards. Please ensure you only have one of each type, * and/or ?.'

    # initialize wildcard counters to ensure no one is cheating at cheating at scrabble
    star_wildcard_counter = 0
    q_wildcard_counter = 0
    
    for char in rack:
        
        # ensure rack contains valid characters
        if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz*?':
            return a
        
        # ensure max of one *
        elif char == '*':
            star_wildcard_counter += 1

        # ensure max of one ?
        elif char == '?':
            q_wildcard_counter += 1
    
    if len(rack) < 2 or len(rack) > 7:
        return b

    if star_wildcard_counter > 1 or q_wildcard_counter > 1:
        return c
    
    # GET SCRABBLE WORDS
    # create list of all scrabble words with a length <= the length of rack + 1
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        scrabble_words = [datum.strip('\n') for datum in raw_input if len(datum) <= len(rack) + 1]

    # ensure input contains capital letters to match scrabble words
    rack = rack.upper()
    
    # DETERMINE WHICH SCRABBLE WORDS TO KEEP
    scorable_words = {}
    for word in scrabble_words:

        # store user input and scrabble word in new variables as lists
        mutate_rack = list(rack)
        mutate_word = list(word)
        
        # initialize list for holding unscorable letters
        do_not_score = ['']

        valid_word = True
        
        while len(mutate_word) > 0 and valid_word == True:
        # check letters in scrabble word against user input
            for letter in word:
                if letter in mutate_rack:
                    # remove letter from mutate_rack so it can't be used again
                    mutate_rack.remove(letter)
                    mutate_word.remove(letter)

                else:
                    # check mutate_rack for wildcard *
                    if '*' in mutate_rack:
                        do_not_score.append(letter)
                        mutate_rack.remove('*')
                        mutate_word.remove(letter)

                    # check mutate_rack for wildcard ?
                    elif '?' in mutate_rack:
                        do_not_score.append(letter)
                        mutate_rack.remove('?')
                        mutate_word.remove(letter)

                    else:
                        # move on to next word
                        valid_word = False
                        break
        
        # add word:do_not_score to dict scorable_words
        if valid_word == True:
            scorable_words[word] = do_not_score

    # SCORE WORDS
    import wordscore
    scrabble_output = []
    for item in scorable_words.items():
        scrabble_output.append(wordscore.score_word(item))

    # sort by score, alphabetically for score ties
    scrabble_output = sorted(scrabble_output, key=lambda x: (-x[0], x[1]))

    pear = scrabble_output, len(scrabble_output)

    if len(scrabble_output) == 0:
        return "I'm sorry. You can't make any words with those characters."
    
    else:
        return pear