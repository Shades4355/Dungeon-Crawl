##########
# Parser #
##########

def peek(word_list):
  if word_list:
    word = word_list[0]
    return word[0]
  else:
    return nil


def match(word_list, expecting):
  if word_list:
    word = word_list.pop(0)

    if word[0] == expecting:
      return word
    else:
      return nil


def skip(word_list, word_type):
  while peek(word_list) == word_type:
    match(word_list, word_type)


def parse_verb(word_list):
  skip(word_list, 'stop')
  if peek(word_list) == 'verb':
    return match(word_list, 'verb')
  # else:
    # raise parserError.new("Expected a verb next.")
    # above line is Ruby code, test to see if works in python


def parse_object(word_list):
  skip(word_list, 'stop')
  next_word = peek(word_list)

  if next_word == 'noun':
    return match(word_list, 'noun')
  elif next_word == 'direction':
    return match(word_list, 'direction')
  # else:
  #   raise parserError.new("Expected a noun or direction next. (object)")


def parse_sentence(word_list):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return(verb[1], obj[1])


###########
# Lexicon #
###########

class Lexicon:
  # __init__(self, input)

  def scan(input):
    words = input.lower().split()
    return_words = []

    directions = ['north', 'south', 'east', 'west']
    verbs = ['go', 'check', 'eat']
    stop = ['the', 'in', 'of', "to"]
    nouns = ['inventory', 'food', "inn", "sewer", "home", "house"]

    for i in words:
      if i in directions:
        return_words.append(['direction', i])

      elif i in verbs:
        return_words.append(['verb', i])

      elif i in stop:
        return_words.append(['stop', i])

      elif i in nouns:
        return_words.append(['noun', i])

      else:
        return_words.append(['error', i])

    parse_sentence(return_words)

############################
# do something with parsed #
############################






#
