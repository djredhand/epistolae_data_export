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
    cur.execute("""SELECT * from woman""")
    letter_rows = cur.fetchall()
    
    all_rows = []
    header = (['id','name','title','bio','bio_notes','birthdate', 'birthplace','fulltext'])
    all_rows.append(header)

    for row in letter_rows:
        bio = row['bio']
        bio = bio[:10000]
        fulltext = row['fulltext']
        fulltext = fulltext[:10000]

    	row_data = (
            row['id'], row['name'], row['title'], bio, row['bio_notes'], row['birthdate'], row['birthplace'], fulltext)
    	
        if count < 11:
            all_rows.append(row_data)
            count = count + 1


    with open('woman.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all_rows)
		#print all_rows

except Exception as e:
    print '%s (%s)' % (e.message, type(e))
    import pdb
    pdb.set_trace()