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
    cur.execute("""SELECT * from letter""")
    letter_rows = cur.fetchall()
    
    all_rows = []
    header = (['id','date','text','original_text','historical_context',
        'scholarly_notes', 'manuscript_source', 'printed_source','authenticity',
        'translation_notes', 'keywords','modified','deleted','fulltext'])
    all_rows.append(header)

    for row in letter_rows:
        text = row['text']
        text = text[:10000]
        original_text = row['original_text']
        original_text = original_text[:10000]
        historical_context = row['historical_context']
        historical_context = historical_context[:10000]
        fulltext = row['fulltext']
        fulltext = fulltext[:10000]

    	row_data = (
            row['id'], row['date'], text, original_text, historical_context, row['scholarly_notes'],
            row['manuscript_source'], row['printed_source'], row['authenticity'],
            row['translation_notes'], row['keywords'], row['modified'], row['deleted'],
            fulltext)
    	
        if count < 11:
            all_rows.append(row_data)
            count = count + 1


    with open('letter.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all_rows)
		#print all_rows

except Exception as e:
    print '%s (%s)' % (e.message, type(e))
    import pdb
    pdb.set_trace()