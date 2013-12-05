import psycopg2
import psycopg2.extras
import csv
import pdb

try:
	conn = psycopg2.connect("dbname='epistolae' user='jdavis1' host='localhost' password='jedavis13'")

except:
	print "I can't connect man!"

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

try:
    cur.execute("""SELECT * from letter""")
    letter_rows = cur.fetchall()
    
    all_rows = []
    header = (['id','date','text','original_text','historical_context',
        'scholarly_notes', 'manuscript_source', 'printed_source','authenticity',
        'translation_notes', 'keywords','modified','deleted','fulltext', 'woman_name'])
    all_rows.append(header)
    count = 0
    for row in letter_rows:
        letter_map_id = row['id']
        text = row['text']
        text = text[:10000]
        original_text = row['original_text']
        original_text = original_text[:10000]
        historical_context = row['historical_context']
        historical_context = historical_context[:10000]
        fulltext = row['fulltext']
        fulltext = fulltext[:10000]
        woman_name = ''

        cur.execute("SELECT * from participant WHERE letter_id = %s",(letter_map_id,))
        letter_map = cur.fetchall()
        for participant in letter_map:
            participant_id = participant[0]
            participant_letter_id = participant[1]
            participant_woman_id = participant[2]
            participant_name = participant[3]
            participant_role = participant[4]
            if participant_woman_id > 0:
                cur.execute("SELECT * from woman WHERE id = %s",(participant_woman_id,))
                woman = cur.fetchall()
                woman_name = woman[0][1]
            #pdb.set_trace()
        #letter_text = row['fulltext']
        #letter_text = fulltext[:10000]

    	row_data = (
            row['id'], row['date'], text, original_text, historical_context, row['scholarly_notes'],
            row['manuscript_source'], row['printed_source'], row['authenticity'],
            row['translation_notes'], row['keywords'], row['modified'], row['deleted'],
            fulltext, woman_name)
    	
        if count < 11:
            all_rows.append(row_data)
            count = count + 1


    with open('participant.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all_rows)
		#print all_rows

except Exception as e:
    print '%s (%s)' % (e.message, type(e))
    pdb.set_trace()