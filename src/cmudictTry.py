import cmudict

def convert_to_phonetics(word):
  # Get the phonetic pronunciation of the word
  pronunciation = cmudict.dict()[word]

  # If the word is not found in the dictionary, return an empty list
  if not pronunciation:
    return []

  # Otherwise, return the first pronunciation in the list (since the CMU dictionary can have multiple pronunciations for a single word)
  return pronunciation[0]

# Test the function
print(convert_to_phonetics("hello"))  # Output: ['HH', 'AH0', 'L', 'OW1']
print(convert_to_phonetics("world"))  # Output: ['W', 'ER1', 'L', 'D']
