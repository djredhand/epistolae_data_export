import psycopg2
import psycopg2.extras
import csv

try:
	conn = psycopg2.connect("dbname='epistolae' user='jdavis1' host='localhost' password='jedavis13'")

except:
	print "I can't connect man!"

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
count = 0
try:
    cur.execute("""SELECT * from participant""")
    other_rows = cur.fetchall()
    
    all_rows = []
    header = ('id','name')
    all_rows.append(header)
    

    for row in other_rows:
        name = row['name']
        name = name[:10000]
        name = name.rstrip()
        name = name.lstrip()
        row_data = (row['id'], name)

        if not name == '':
            all_rows.append(row_data)

    with open('other_profiles.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all_rows)
		#print all_rows

except Exception as e:
    print '%s (%s)' % (e.message, type(e))
    import pdb
    pdb.set_trace()