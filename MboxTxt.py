import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

#cur.execute('''DROP TABLE IF EXISTS emails''')
#cur.execute('''create table emails (email text)''')

cur.execute('''DROP TABLE IF EXISTS orgs''')
cur.execute('''create table orgs (org text)''')


fname = 'mbox.txt'
#if ( len(fname) < 1 ) : fname = 'mbox-short.txt'

fh = open(fname)
emails = [line.split()[1].split("@")[1] for line in fh if line.startswith('From:')]
for email in emails:
    cur.execute('''insert into orgs (org) values ('%s')'''%email)

conn.commit()

cur.execute("create table Counts as select org, count(*) as count from orgs group by org ")

for row in cur.fetchall() :
    print str(row[0]), row[1]

cur.close()


#--------------------------------------------------------
from collections import Counter
fh = open(fname)
orgs = Counter([line.split()[1].split("@")[1] for line in fh if line.startswith('From:')])
