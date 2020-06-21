import sqlite3
import csv
conn=sqlite3.connect('exoplanet.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS exoplanet')
cur.execute('''
CREATE TABLE "exoplanet"(
  "kepler_id" TEXT,
"koi_name" TEXT,
"kepler_name" TEXT,
"status" TEXT,
"period" REAL,
"radius" REAL,
"t_eq" REAL
)
''')

fname=input('enter the exoplanet csv file name:')
if len(fname)<1 :fname="planets.csv"
with open(fname, 'r') as csv_file:
  csv_reader=csv.reader(csv_file, delimiter=',')
  #csv_reader=csv_file.readlines()
  for row in csv_reader:
    print(row)
    kepler_id=row[
  0
]
    koi_name=row[
  1
]
    kepler_name=row[
  2
]
    status=row[
  3
]
    period=float(row[
  4
])
    radius=float(row[
  5
])
    t_eq=float(row[
  6
])
    cur.execute('''INSERT INTO exoplanet(kepler_id,koi_name,kepler_name,status,period,radius,t_eq)
      VALUES (%s,%s,%s,%s,%s,%s,%s)''',(kepler_id,koi_name,kepler_name,status,period,radius,t_eq))
    conn.commit
