###### FUNCTIONS #####
words = open("wordbank.txt","r") #opens text file for reading
words = words.read() #stores contents of txt file in variable
words = words.split() #place words into a list.
letter_dic = {}
wordbank ={}

for g in range(len(words)):
  wordbank[words[g]]=0
word_scores = {}

#  Returns a dictionary where each letter of the alphabet serves as a key, and the corresponding value is the number of words in the word bank that contain that letter.
def letter_frequency(words):
  
  letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  for g in range (26):
    letter_frequency= 0
    for word in words:
      if letters[g] in word:
        letter_frequency+=1
    letter_dic[letters[g]] = letter_frequency
  return letter_dic
    
  
      

# Returns the score for a five-letter word. This function calculates the score of a five-letter word by summing the frequency of each letter in the word. 
# For example: "horse" scores 15,435. "h":1702 + "0":3904 + "r":(3905) + "s":5924 + "e":5696 = 15,435
def score_word(word, letter_frequency):
  score = 0
  for letter in word:
    if letter in letter_dic.keys():
      score+=letter_dic[letter]
  return score
    
    
  
    
  
    
  
# Returns a dictionary that associates each word (key) with its corresponding score (value). To calculate the score for each word in the dictionary, iterate through the dictionary of words and apply the score_word() function to each one.
def score_wordbank(wordbank):
  for word in wordbank:
    wordbank[word] = score_word(word, letter_frequency)
  return wordbank






# Returns a dictionary of words that either do not contain the letter or contain more than two instance of the letter but not at the index.
def words_containing_letter(letter, wordbank):
  temp = {}
  for word in wordbank:
    if letter in word:
      temp[word] = wordbank[word]
  return temp

def words_not_containing_letter(letter, index, wordbank, list_guess):
  multiples = 0
  for g in range (5):
    if list_guess[g] == letter:
      multiples+=1
    else: continue
  for g in range(len(words)):
    if words[g][0] == letter or words[g][1] == letter or words[g][2] == letter or words[g][3] == letter or words[g][4] == letter:
      if multiples>= 2:
        if words[g][index] == letter:
          if words[g] in wordbank:
            del wordbank[words[g]]
            g-=1
      else:
        if words[g] in wordbank:
          del wordbank[words[g]]
          g-=1
        else:
          continue
      
  
  return wordbank
  
    

# Returns a dictionary of words with the letter at the specified index.
def words_containing_letter_at_index(letter, index, wordbank):
  for g in range(len(words)):
    if words[g][index] != letter:
      if words[g] in wordbank:
        del wordbank[words[g]]
        g-=1
      else:
        continue
  return wordbank
  
      
    
      


# Returns dictionary of words which do not contain the letter at the specified index.
def words_not_containing_letter_at_index(letter, index, wordbank):
  for g in range(len(words)):
    if words[g][index] == letter:
      if words[g] in wordbank:
        del wordbank[words[g]]
        g-=1
    else:
      if letter not in words[g]:
        if words[g] in wordbank:
          del wordbank[words[g]]
          g-=1
        else:
          continue
      else: continue
  return wordbank







# Function returns a sorted dictionary in which the key with smallest value is listed first and the key with largest value is listed last.
def sort_wordbank(wordbank):
	wordbank = dict(sorted(wordbank.items(), key=lambda x: x[1], reverse=False))

####### PROGRAM ######




letter_frequency(wordbank)
for g in range(6):
  guess = input("What word did you guess?(All lowercase)")
  score = input("What was your score. G for Green, B for Black, and Y for Yellow. Example: GGBBY.  ")
  list_guess = list(guess)
  list_score = list(score)
  if list_score[0]== 'G':
    words_containing_letter_at_index(list_guess[0], 0, wordbank)
  elif list_score[0]=='Y':
    words_not_containing_letter_at_index(list_guess[0], 0, wordbank)
  elif list_score[0]=='B':
    words_not_containing_letter(list_guess[0], 0, wordbank, list_guess)
  if list_score[1]== 'G':
    words_containing_letter_at_index(list_guess[1], 1, wordbank)
  elif list_score[1]=='Y':
    words_not_containing_letter_at_index(list_guess[1], 1, wordbank)
  elif list_score[1]=='B':
    words_not_containing_letter(list_guess[1], 1, wordbank, list_guess)
  if list_score[2]== 'G':
    words_containing_letter_at_index(list_guess[2], 2, wordbank)
  elif list_score[2]=='Y':
    words_not_containing_letter_at_index(list_guess[2], 2, wordbank)
  elif list_score[2]=='B':
    words_not_containing_letter(list_guess[2], 2, wordbank, list_guess)
  if list_score[3]== 'G':
    words_containing_letter_at_index(list_guess[3], 3, wordbank)
  elif list_score[3]=='Y':
    words_not_containing_letter_at_index(list_guess[3], 3, wordbank)
  elif list_score[3]=='B':
    words_not_containing_letter(list_guess[3], 3, wordbank, list_guess)
  if list_score[4]== 'G':
    words_containing_letter_at_index(list_guess[4], 4, wordbank)
  elif list_score[4]=='Y':
    words_not_containing_letter_at_index(list_guess[4], 4, wordbank)
  elif list_score[4]=='B':
    words_not_containing_letter(list_guess[4], 4, wordbank, list_guess)
  
  
  score_word(words, letter_frequency)
  score_wordbank(wordbank)
  sort_wordbank(wordbank)
  print(wordbank)
