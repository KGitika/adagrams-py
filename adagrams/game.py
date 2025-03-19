from random import randint
 
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    letter_pool_as_list = []
    for letter, freq in LETTER_POOL.items():
        letter_pool_as_list.extend([letter] * freq)

    letters = []
    for i in range(10):
        index = randint(0, len(letter_pool_as_list) - 1)
        letters.append(letter_pool_as_list.pop(index))
    return letters

    

def uses_available_letters(word, letter_bank):
    letters_with_freq = {}
    for letter in letter_bank:
        letter = letter.lower()
        if letter in letters_with_freq:
            letters_with_freq[letter] += 1
        else:
            letters_with_freq[letter] = 1
    for character in word:
        character = character.lower()
        if  character in letters_with_freq and letters_with_freq[character] != 0:
            letters_with_freq[character] -= 1
        else:
            return False
    return True

def score_word(word):
    score_chart = {
        'A': 1, 
        'E': 1, 
        'I': 1, 
        'O': 1, 
        'U': 1, 
        'L': 1, 
        'N': 1, 
        'R': 1, 
        'S': 1, 
        'T': 1, 
        'D': 2, 
        'G': 2, 
        'B': 3, 
        'C': 3, 
        'M': 3, 
        'P': 3, 
        'F': 4, 
        'H': 4, 
        'V': 4, 
        'W': 4, 
        'Y': 4, 
        'K': 5, 
        'J': 8, 
        'X': 8, 
        'q': 10, 
        'Z': 10
    }
    score = 0
    length = len(word)

    if length == 0:
        return score
    
    if length > 6 and length < 11:
        score += 8

    for character in word:
        character = character.upper()
        score += score_chart[character]

    return score

def get_highest_word_score(word_list):
    pass


