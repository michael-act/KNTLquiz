import sqlite3

class DatabaseKNTL:
	def __init__(self, dirdb, filedb):
		self.dirdb = dirdb
		self.filedb = filedb
		self.filesql = filedb.replace('db', 'sql')
		self.table = filedb[:-3]
		self.conndb = sqlite3.connect(self.dirdb + self.filedb)


	def create(self):
		'''
		Result: Creating a table for save all KNTL word
		Parameter: None
		'''

		query = f''' CREATE TABLE IF NOT EXISTS {self.table} (
						word_id INTEGER PRIMARY KEY,
						word TEXT NOT NULL UNIQUE,
						word_desc TEXT NOT NULL
					 ); '''
		self.conndb.execute(query)
		self.conndb.commit()


	def insert(self, word, desc):
		'''
		Result = Insert a word of KNTL and the Definition about the word to table
		Parameter: 
		word -> string
		desc -> string, definition about the word
		'''

		self.conndb.execute(f'INSERT INTO {self.table} (word, word_desc) VALUES ("{word}", "{desc}")')
		self.conndb.commit()


	def export(self):
		'''
		Result: Got a exported database file to sql
		'''

		file = open(self.dirdb+self.filesql, 'w')
		for line in self.conndb.iterdump():
			file.write('%s\n' % line)
		file.close()


	def getData(self, word_id=1, random=False):
		'''
		Return: Data that has selected
		Parameter: 
		word_id -> Integer
		random -> Boolean, will return random row if this parameter random is True
		'''

		cur = self.conndb.cursor()
		if random:
			cur.execute('SELECT * FROM table ORDER BY RANDOM() LIMIT 1')
		else:
			cur.execute(f'SELECT * FROM table WHERE word_id={word_id}')
		data = cur.fetchone()[0]
		return data



if __name__ == '__main__':
	KNTL = DatabaseKNTL('db/', 'KNTLword.db')
	KNTL.create()
	KNTL.insert('KENTAL', 'antara cair dan keras')
	print(KNTL.getData())
	KNTL.export()