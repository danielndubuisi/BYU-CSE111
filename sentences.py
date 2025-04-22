""" A program that prints a random sentence based on quantiity and tense. For additioanl requirements, I made changes to the program by creating get_adverb() and get_adjective() functions, calling them as well as other functions multiple times (if need be) to print sentences in the format proposed in the ponder section.
"""
import random

# define main function
def main():
    # store the quantity and verb tense in a list
    sentence_values = [["single", "past"], ["single", "present"], ["single", "future"], ["plural", "past"], ["plural", "present"], ["plural", "future"]]

    # loop through each sentence value to provide a sentence
    for sentence_value in sentence_values:
        quantity_type = sentence_value[0]
        tense = sentence_value[1]

        # check quantity type to determine quantity
        if quantity_type == 'single':
            quantity = 1
            # call make sentence function with quantity as 1
            sentence = make_sentence(quantity, tense)
            print(sentence)
        else:
            quantity = 2 #assign a value that is NOt 1
            # call make sentence function with quantity NOT 1
            sentence = make_sentence(quantity, tense)
            print(sentence)
            

# get determiner function
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is a word like "the", "a", "one", "some", "many". If quantity is 1, this function will return either "a","one", or "the". Otherwise this function will return either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


# get noun function
def get_noun(quantity):
    """Return a randomly chosen noun. If quantity is 1, this function will return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    # Randomly choose and return a determiner.
    noun = random.choice(nouns)
    return noun


# get verb function
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past", this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1, this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == 'future':
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    else:
        verbs = []

    verb = random.choice(verbs)
    return verb


# get adjective function
def get_adjective():
    """Return a randomly chosen adjective from this list of adjectives:
        "beautiful", "curious", "energetic", "friendly", 
        "gentle", "happy", "intelligent" "joyful",
        "kind", "lovely", "peaceful", "strong"    
    Return: a randomly chosen adjective.
    """
    adjectives = ["beautiful", "curious", "energetic", "friendly", "gentle", "happy", "intelligent", "joyful", "kind", "lovely", "peaceful", "strong"]

    adjective = random.choice(adjectives)
    return adjective


# get adverb function
def get_adverb():
    """Return a randomly chosen adverb from this list of adverbs:
        "quickly", "carefully", "happily", "softly", 
        "loudly", "slowly", "eagerly", "sadly", 
        "angrily", "happily", "calmly", "bravely"    
    Return: a randomly chosen adverb.
    """
    adverbs = ["quickly", "carefully", "happily", "softly", "loudly", "slowly", "eagerly", "sadly", "angrily", "happily", "calmly", "bravely"]

    adverb = random.choice(adverbs)
    return adverb


# get preposition function
def get_preposition():
    """Return a randomly chosen preposition from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition.
    """
    prepostions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    prepostion = random.choice(prepostions)
    return prepostion


# get prepositional phrase function
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three words: a preposition, a determiner, and a noun by calling the get_preposition, get_determiner, and get_noun functions.
    Parameter
        quantity: an integer that determines if the determiner and noun in the prepositional phrase returned from this function should be single or pluaral.
    Return: a prepositional phrase.
    """
    # call get preposition function
    preposition = get_preposition()

    # call get determiner function
    determiner = get_determiner(quantity)

    # call get noun function
    noun = get_noun(quantity)

    # return prepositional phrase
    return f'{preposition} {determiner} {noun}'

# make sentence function
def make_sentence(quantity, tense):
    """Build and return a sentence in the ponder format of: a determiner, an adjective, a noun, a prepositional phrase, an adverb, a verb, another determiner, another adjective, another noun and another prepositional phrase. The grammatical quantity of the determiner and noun will match the number in the quantity parameter. The grammatical quantity and tense of the verb will match the number and tense in the quantity and tense parameters.
    Return: a sentence in the ponder format with only the first determiner letter capitalized.
    """
    # get determiners
    first_determiner = get_determiner(quantity)
    second_determiner = get_determiner(quantity)

    # get adjectives
    first_adjective = get_adjective()
    second_adjective = get_adjective()

    # get nouns
    first_noun = get_noun(quantity)
    second_noun = get_noun(quantity)

    # get verb
    verb = get_verb(quantity, tense)

    # get adverb
    adverb = get_adverb()
    
    # get prepositional phrases
    first_prepositional_phrase = get_prepositional_phrase(quantity)
    second_prepositional_phrase = get_prepositional_phrase(quantity)

    return f'{first_determiner.capitalize()} {first_adjective} {first_noun} {first_prepositional_phrase} {adverb} {verb} {second_determiner} {second_adjective} {second_noun} {second_prepositional_phrase}.'


# call the main function
main()