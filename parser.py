import pandas as pd
import errno
import os

def create_directory(path):
	try:
		os.makedirs(path)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

create_directory('data/hansard/')
curr = 1800
while curr <= 1900:
	create_directory('data/hansard/' + str(curr))
	curr += 10

input_file = 'membercontributions-20170106.tsv'
df = pd.read_csv(input_file, sep='\t')
cwd = os.getcwd()

for row in df.itertuples():
	# if not nan
	if row[3] == row[3]:
		date = row[3]
		year = int(date[:4])
		speech_id = row[2]

	fp = cwd + '/data/hansard/'
	doc_id = str(speech_id) + '.txt'
	text = str(row[7])

	if year >= 1800 and year < 1810:
		fp += '1800/'
	elif year >= 1810 and year < 1820:
		fp += '1810/'
	elif year >= 1820 and year < 1830:
		fp += '1820/'
	elif year >= 1830 and year < 1840:
		fp += '1830/'
	elif year >= 1840 and year < 1850:
		fp += '1840/'
	elif year >= 1850 and year < 1860:
		fp += '1850/'
	elif year >= 1860 and year < 1870:
		fp += '1860/'
	elif year >= 1870 and year < 1880:
		fp += '1870/'
	elif year >= 1880 and year < 1890:
		fp += '1880/'
	elif year >= 1890 and year < 1900:
		fp += '1890/'
	else:
		fp += '1900/'

	os.chdir(fp)
	file = open(doc_id, 'w+')
	file.write(text)


print('parsing complete')
