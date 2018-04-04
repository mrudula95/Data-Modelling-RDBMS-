import datetime
import mysql.connector
#31
cnx = mysql.connector.connect(user='root', password='root123*', database='project')
v_cursor = cnx.cursor()

v_cursor.execute("select S5.mt as mt, S6.price16-S5.price16 as diff from Sep2015 S5  INNER JOIN Sep2016 S6 on S5.mt=S6.mt order by diff ASC")

for (mt,diff) in v_cursor :
  print("metro:{}| diff:{}".format(mt,diff))

v_cursor.close()
cnx.close()


###############################################
#32


cnx = mysql.connector.connect(user='root', password='Mike_43260627', database='project')

v_cursor = cnx.cursor()

v_cursor.execute("select max(price) as xp, min(price) as np, avg(price) as ap from price"
)

for (xp, np,ap) in v_cursor :
  print("maxprice:{}|minprice:{}|averageprice:{}".format(xp,np, ap))

v_cursor.close()

###################################################
#33
v_cursor = cnx.cursor()

v_cursor.execute("select max(pricepersqft) as xp, min(pricepersqft) as np, avg(pricepersqft) as ap from pricepersqft"
)

for (xp, np,ap) in v_cursor :
  print("maxpricepersqft:{}|minpricepersqft:{}|averagepricepersqft:{}".format(xp,np, ap))

v_cursor.close()
cnx.close()

####################################################
#34
v_cursor = cnx.cursor()
 
v_cursor.execute("select avg(price), state from price p INNER JOIN city on p.citycode = city.citycode  WHERE city.state like '%IL%';"
)

for (mt,diff) in v_cursor :
  print("metro:{}| diff:{}".format(mt,diff))

v_cursor.close()

#####################################################
#35
v_cursor = cnx.cursor()

v_cursor.execute("select count(distinct metro) as nmetro from city inner join price on price.citycode=city.citycode where price>1458.476681")

for (nmetro) in v_cursor :
  print("numberofmetro:{}".format(nmetro))

v_cursor.close()

###################################################
#36
v_cursor = cnx.cursor()

v_cursor.execute("select distinct (c.cityname) ,c.metro from city c JOIN price p on p.citycode = c.citycode where p.price>1458.476681")

for (nm, nc) in v_cursor :
  print("numberofmetro:{}|numberofcity:{}".format(nm,nc))

v_cursor.close()

################################################
#371
v_cursor = cnx.cursor()

v_cursor.execute("create table sep2016 as  select metro as mt, price as price16, state from city c INNER JOIN price p on p.citycode = c.citycode where metro is not null and yearmonth = 'September 2016'  group by mt"
)


v_cursor.close()

################################################
#372
v_cursor = cnx.cursor()

v_cursor.execute("create table sep2015 as  select metro as mt, price as price15, state from city c INNER JOIN price p on p.citycode = c.citycode where metro is not null and yearmonth = 'September 2015'  group by mt"
)


v_cursor.close()

###############################################
#373
v_cursor = cnx.cursor()
 
v_cursor.execute("select S5.mt as mt, S6.price16-S5.price15 as diff from Sep2015 S5 INNER JOIN Sep2016 S6 on S5.mt=S6.mt order by diff DESC limit 1"
)

for (mt,diff) in v_cursor :
  print("metro:{}| diff:{}".format(mt,diff))

v_cursor.close()