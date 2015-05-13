import unicodecsv
import cStringIO

class UnicodeCSVTestFunction(input_string):
		f = cStringIO.StringIO(input_string)
		r = self.unicodecsv.reader(f, encoding="utf-8")
		for row in r
			pass
		f.close

