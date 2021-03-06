import psycopg2
import psycopg2.extras
import csv

try:
	conn = psycopg2.connect("dbname='epistolae' user='jdavis1' host='localhost' password='jedavis13'")

except:
	print "I can't connect man!"

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    cur.execute("""SELECT * from letter""")
    rows = cur.fetchall()
    
    all_rows = []
    for row in rows:
        original_text = row['original_text']
        original_text = original_text[:10000]
        fulltext = row['fulltext']
        fulltext = fulltext[:10000]

    	row_data = (
            row['id'], row['date'], original_text, row['scholarly_notes'],
            row['manuscript_source'], row['printed_source'], row['authenticity'],
            row['translation_notes'], row['keywords'], row['modified'], row['deleted'],
            fulltext)
    	all_rows.append(row_data)

    with open('letter.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t',quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all_rows)
		#print all_rows

except Exception as e:
    print '%s (%s)' % (e.message, type(e))
    import pdb
    pdb.set_trace()