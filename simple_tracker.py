import string
import sys
import os

# this is a very simple tracker of whether a text in the hansard has a relatively 
# more positive or negative sentiment

# at the moment we do count duplicate words as well
# for example, for a positive word 'adequate,'
# if one text contains it twice and the other contains it only once, 
# the former has more "positive" sentiment than the latter

# each occurence of word is given a score
# for the purpose of this exercise, a positive word is given a score of +1, 
# while a negative word is given a score of -1

def get_words(file):
	res = []
	with open(file, 'r') as f:
		for line in f:
			# a one-element array
			word = line.split()[0]
			res.append(word)
	return res

def calc_sentiment(text, pos_words, neg_words):
	count = 0
	name = None

	with open(text, 'r',  encoding='latin-1') as f:
		name = os.path.basename(f.name)

		for line in f:
			sent = line.split()
			for word in sent:

				# getting rid of punctuation
				for c in string.punctuation:
					word = word.replace(c, "")

				if word in pos_words:
					count += 1
				elif word in neg_words:
					count -= 1

	if count == 0:
		print(name + ': neutral')
	elif count < 0:
		print(name + ': negative, ' + str(count))
	else:
		print(name + ': positive, +' + str(count))


if __name__ == '__main__' :
	try:
		text = sys.argv[1]
		pos_words = get_words(sys.argv[2])
		neg_words = get_words(sys.argv[3])
		calc_sentiment(text, pos_words, neg_words)

	except IOError:
		print("Incorrect Argument Names - Try Again")