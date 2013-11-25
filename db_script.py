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
    	if row[1] == '':
    		row_data = row['id'], 'no data'
    	else:
    		row_data = row['id'], row['date']
    	all_rows.append(row_data)
    	#print row

    with open('test.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerows(all_rows)
		print all_rows
except:
	print "I can't select anything!"