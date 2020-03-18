
#!/usr/bin/python
#
# Counts Arabic words with 1-10 characters in a text file.
# Counts hapaxes.
# Shadda is assumed to be equal to (1) character.
# All other diacritics and punctuation are discarded.
# Assumes tokenized UTF-8 input.

import sys
import os.path
import codecs
import re

# Input validation
input = "مرحبًا مرحبًا"
print('مرحبًا مرحبًا')
filename_input = sys.argv
# Clean up words containing non-arabic
all_but_arabic_letters = re.compile(u"[^\u0621-\u063A\u0641-\u064A\u0651]", flags=re.UNICODE)


all_but_arabic_letters_in_token = re.compile(u"^[^\u0621-\u063A\u0641-\u064A\u0651]+$", flags=re.UNICODE)


# Filter each word

lemmas = []
for word in input:
  if re.match(all_but_arabic_letters, word):
        continue
	
  clean_word = re.sub(all_but_arabic_letters, "", word)
lemmas.append(clean_word)						
# Create a unique list of lemmas using the set() built-in function.
# The list is a collection of tuples containing the lemma itself and
# the number of times it occurs in the text. List is sorted (alpha).

set_of_lemmas = []

for lemma in sorted(set(lemmas)):
	times = lemmas.count(lemma)
	set_of_lemmas.append((lemma, times))

  # -------------------------------------------------------------------
# Count hapaxes

hapaxes = [lemma[0] for lemma in set_of_lemmas if lemma[1] == 1]

# -------------------------------------------------------------------
# Prepare output file
output_list = sorted(set_of_lemmas, key=lambda freq: freq[1], reverse=True)
	

	# Write to the output file. Add a header with basic info.
	
  #output.write("File: " + filename_input)
  #output.write("\nLemmas in text: " + str(len(lemmas)) + "; ")
  #output.write("unique lemmas: " + str(len(set_of_lemmas)) + "; ")
 # output.write("hapaxes: " + str(len(hapaxes)) + "\n")
	
	# Column headers.
	
#output.write("LEMMA\tOCCURRENCES\n")
