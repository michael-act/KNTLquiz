from database import DatabaseKNTL

import requests
from bs4 import BeautifulSoup

FILE_PATH = 'indonesian-wordlist/'
FILES = ['00-indonesian-wordlist.lst', 
		 '02-crawls-2005-sort-alpha.lst', 
		 '04-myspell2006-sort-alpha.lst', 
		 '01-kbbi3-2001-sort-alpha.lst', 
		 '03-indodict2008-sort-alpha.lst', 
		 '05-ivanlanin2011-sort-alpha.lst']

DB_DIR = 'db/'
DB_FILE = 'KNTLword.db'

class ScrapeKNTL:
	def __init__(self):
		self.addedWord = set()

	def check(self, word):
		'''
		Return: Boolean, make sure the word is match with keyword
		Parameter: word -> string, word to validate
		'''

		keyword = 'KENTEL'
		keyword = keyword.replace('E', 'O')
		if len(word) == 6:
			match = [1 for k, w in zip(keyword, word) if k == w]
			return len(match) > 2
		else:
			return False


	def definiting(self, word):
		'''
		Return: string, description of word
		Parameter: word -> string, word to define
		'''

		page = requests.get(f'https://www.kamusbesar.com/{word}')
		soup = BeautifulSoup(page.content, 'html.parser')
		title_parse = soup.find('div', {'class': 'title-left'})
		title = title_parse.text.upper()
		if title == word:
			desc_parse = soup.findAll('span', {'class': 'word_description'})
			desc = ', '.join([parse.text.capitalize() for parse in desc_parse])
			return desc


	def main(self, file):
		'''
		Return: None
		Parameter: file -> string, name of wordlist file
		Result: Database is get full of KNTL word and definition
		'''

		file = FILE_PATH+file

		db = DatabaseKNTL(DB_DIR, DB_FILE)
		db.create()
		with open(file, encoding='ISO-8859-1') as f:
			wordList = f.readlines()
			for word in wordList:
				word = word.strip().upper()
				valid = (word not in self.addedWord) and self.check(word)
				desc = self.definiting(word) if valid else False
				if desc:
					db.insert(word, desc)
					print('Sukses')
					self.addedWord.add(word)



if __name__ == '__main__':
	scrape = ScrapeKNTL()
	for file in FILES:
		scrape.main(file)
