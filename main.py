def count_letter(list_of_words, letter):
  count = 0
  for word in list_of_words:
      if letter in word:
        count = count + 1
  return count

print(count_letter(['python', 'c++', 'c', 'scala', 'java'], 'c'))

