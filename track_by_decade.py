import simple_tracker
import sys
import os

def apply_to_decade(decade, pos_words, neg_words):
	fp = 'hansard/' + decade
	os.chdir(fp)

	for f in os.listdir():
		simple_tracker.calc_sentiment(f, pos_words, neg_words)

if __name__ == '__main__' :
	try:
		decade = sys.argv[1]
		pos_words = simple_tracker.get_words(sys.argv[2])
		neg_words = simple_tracker.get_words(sys.argv[3])
		apply_to_decade(decade, pos_words, neg_words)

	except IOError:
	 	print("Incorrect Argument Names - Try Again")