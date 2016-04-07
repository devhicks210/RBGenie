import pymysql

conn = pymysql.connect(host='localhost', port=xxxx, user='xxxx', passwd='xxxx', db= 'xxxxx')
cur = conn.cursor()

class idealRB1(object):

	def carries(self, year):

		cur.execute("""SELECT carries, fname, lname FROM season_%s_totals ORDER BY carries DESC LIMIT 10;""", (year))
		rows = cur.fetchall()

		for x, y, z in rows:
			print y, z, x

	def rushyds(self, year):

		cur.execute("""SELECT rushyds, fname, lname FROM season_%s_totals ORDER BY rushyds DESC LIMIT 10;""", (year))
		rows = cur.fetchall()

		for x, y, z in rows:
			print y, z, x

	def runtd(self, year):

		cur.execute("""SELECT runtd, fname, lname FROM season_%s_totals ORDER BY runtd DESC LIMIT 10;""", (year))
		rows = cur.fetchall()

		for x, y, z in rows:
			print y, z, x

	def rec(self, year):

		cur.execute("""SELECT rec, fname, lname FROM season_%s_totals ORDER BY rec DESC LIMIT 10;""", (year))
		rows = cur.fetchall()

		for x, y, z in rows:
			print y, z, x

	def recyds(self, year):

		cur.execute("""SELECT recyds, fname, lname FROM season_%s_totals ORDER BY recyds DESC LIMIT 10;""", (year))
		rows = cur.fetchall()

		for x, y, z in rows:
			print y, z, x

	def rectd(self, year):

		cur.execute("""SELECT rectd, fname, lname FROM season_%s_totals ORDER BY rectd DESC LIMIT 10;""", (year))
		rows = cur.fetchall()

		for x, y, z in rows:
			print y, z, x

	def fumble(self, year):

		cur.execute("""SELECT fum, fname, lname FROM season_%s_totals ORDER BY fum DESC LIMIT 10;""", (year))
		rows = cur.fetchall()

		for x, y, z in rows:
			yield y, z, x
