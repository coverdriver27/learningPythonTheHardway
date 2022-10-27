# Exercise 25: Even More Practise

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentance(sentence):
    """Takes a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentance(sentence)
    print_first_word(words)
    print_last_word(words)

# Now we can go to the terminal and run >> python
# and since we defined some functions and made them do things, we can go ahead and import this as like a module for
# example when we imported the sys module's argv function in previous lessons
# our module will be called ex25 ---->  import ex25

# Example output
# >>> import ex25
# >>> sentence = "All good things comes to thee that is caffinated."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'comes', 'to', 'thee', 'that', 'is', 'caffinated.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'caffinated.', 'comes', 'good', 'is', 'that', 'thee', 'things', 'to']
# >>> print(sorted_words)
# ['All', 'caffinated.', 'comes', 'good', 'is', 'that', 'thee', 'things', 'to']
# >>> ex25.print_first_word(words)
# All
# >>> words
# ['good', 'things', 'comes', 'to', 'thee', 'that', 'is', 'caffinated.']
# >>> ex25.print_last_word(words)
# caffinated.
# >>> words
# ['good', 'things', 'comes', 'to', 'thee', 'that', 'is']
# >>> quit()

