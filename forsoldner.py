def recyds(self, year):

		cur.execute("""SELECT recyds, fname, lname FROM season_%s_totals ORDER BY recyds DESC LIMIT 10;""", (year))
		rows = cur.fetchall()

		for x, y, z in rows:
			print y, z, x
