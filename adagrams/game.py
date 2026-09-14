from random import randint

def draw_letters(): # list of letters. 
    letter_pool = [
        "A", "A", "A", "A", "A", "A", "A", "A", "A",
        "B", "B",
        "C", "C",
        "D", "D", "D", "D",
        "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
        "F", "F",
        "G", "G", "G",
        "H", "H",
        "I", "I", "I", "I", "I", "I", "I", "I", "I",
        "J",
        "K",
        "L", "L", "L", "L",
        "M", "M",
        "N", "N", "N", "N", "N", "N",
        "O", "O", "O", "O", "O", "O", "O", "O",
        "P", "P",
        "Q",
        "R", "R", "R", "R", "R", "R",
        "S", "S", "S", "S",
        "T", "T", "T", "T", "T", "T",
        "U", "U", "U", "U",
        "V", "V",
        "W", "W",
        "X",
        "Y", "Y",
        "Z"
    ] # 第一个 list

    hand = [] # 第二个 list

    for i in range(10):
        index = randint(0, len(letter_pool) - 1)
        letter = letter_pool[index]
        hand.append(letter)
        letter_pool.pop(index)

    return hand


def uses_available_letters(word, letter_bank):
    #we need to copy first to make sure the orignial letter bank  not affect
    available_letters = letter_bank.copy()
    for letter in word:
        letter = letter.upper()

        if letter in available_letters:
            available_letters.remove(letter)
        else:
            return False

    return True




    

def score_word(word):
    letter_scores = { # 按 points order so easy for later check and read grouped the letters by score, so the dictionary is easier to read. Letters with the same score are listed together.
        "A": 1,
        "E": 1,
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1,
        "N": 1,
        "R": 1,
        "S": 1,
        "T": 1,

        "D": 2,
        "G": 2,

        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,

        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,

        "K": 5,

        "J": 8,
        "X": 8,

        "Q": 10,
        "Z": 10
    }

    score = 0 
    for letter in word:
        letter = letter.upper()
        score += letter_scores[letter] 
    if len(word) >= 7:
        score += 8
    return score



def get_highest_word_score(word_list):
    # first assume first one word is winner 
    best_word = word_list[0]
    best_score = score_word(best_word)
# iterate every word 
    for word in word_list:
        current_score = score_word(word)
#if higher score update word and score  
        if current_score > best_score:
            best_word = word
            best_score = current_score
#if same score  tie breaking. 
        elif current_score == best_score: 
            if len(word) == 10 and len(best_word)!=10: #10 letter word priority 
                best_word = word
               

            elif len(word)!=10 and len(best_word) !=10:#if non 10 letters shorter wins 
                if len(word) < len(best_word):
                    best_word = word
                   

    return (best_word,best_score)
                    
