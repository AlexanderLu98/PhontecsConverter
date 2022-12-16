import pronouncing
#https://pronouncing.readthedocs.io/en/latest/index.html

#Note to self: Contains rhymes, but only perfect rhymes, better check for other modules

def get_phonetics(word):
  phonetics = pronouncing.phones_for_word(word)
  if phonetics:
    return phonetics[0]
  else:
    return None

# Test the function
print(get_phonetics("hello"))  # Output: "HH AH0 L OW1"
print(get_phonetics("apple"))  # Output: "AE1 P AH0 L"
print(get_phonetics("banana"))  # Output: "B AE1 N AH0 N AH0"