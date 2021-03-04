import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="phuangkaeo",
    password="simplon59",
    database="pycharm"
)

mycursor = mydb.cursor()
sql = "INSERT INTO sex (sex_id, sex) VALUES (%s,%s)"
val = [
    ('M', 'Male'),
	('F', 'Female'),
	('U', 'Undefined')
]

sql = "INSERT INTO telephone (telno, client_id) VALUES (%s,%s)"
val = [
	('0766089558','1'),
	('0766089559','1'),
	('0766089560','2'),
	('0766089561','3'),
	('0766089562','4')
]

sql = "INSERT INTO city (city_name, inhabitants_number, distance_agent) VALUES (%s,%s,%s)"
val = [
	('Ronchin','12606','2'),
	('La Madeleine','23148','4'),
	('Faches-Thumesnil','22884','4'),
	('Lambersart' ,'26576','5'),
	('Lomme','16786','3')
]

sql = "INSERT INTO type (type, description) VALUES (%s,%s)"
val = [
	('Studio','T1 avec cuisine non séparée'),
	('T1','1 pièce principale à la fois chambre et salon + 1 cuisine + 1 salle de bains avec WC séparés ou inclus'),
	('T2', '2 pièces 1 chambre + 1 salon + 1 cuisine + 1 salle de bains avec WC séparés ou inclus'),
	('T2 Bis','2 pièces 1 chambre + 1 salon dont l’une est suffisamment grande pour être séparée en deux zones distinctes + 1 cuisine + 1 salle de bains avec WC'),
	('T3','3 pièces 2 chambres + 1 salon + 1 cuisine + 1 salle de bains avec WC séparés ou inclus'),
	('T3 Bis,','3 pièces 2 chambres + 1 salon dont l’une est suffisamment grande pour être séparée en deux zones distinctes + 1 cuisine + 1 salle de bains avec'),
	('T4','4 pièces 3 chambres + 1 salon séjour OU 2 chambres + 1 salon + 1 salle à manger + 1 cuisine + 1 salle de bains avec WC séparés ou inclus'),
	('T3 T4','T4 transformé en T3 en réunissant deux pièces pour en faire 1 grande'),
	('T5','5 pièces 4 chambres + 1 salon séjour OU 3 chambres + 1 salon + 1 salle à manger + 1 cuisine + 1 salle de bains ou + avec WC séparés ou inclus')
]

sql = "INSERT INTO logement (lod_address, lod_ville, size, quartier, prix, loyer, city_id, type_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
val = [
	('100 rue colbert','Lomme','80','Lomme','590','50','5','1'),
	('101 rue colbert','Ronchin','40','Ronchin','300','50','1','2'),
	('102 rue colbert','Lambersart' ,'120','Lambersart ','800','120','4','1'),
	('103 rue colbert','La Madeleine','75','La Madeleine','590','50','2','5'),
	('104 rue colbert','Ronchin','70','Ronchin','300','50','1','4')
]

sql = "INSERT INTO contract (contract_detail, contract_start_date, contract_end_date, contract_status, client_id, lod_id) VALUES (%s,%s,%s,%s,%s,%s)"
val = [
	('xxxxxx','2010-01-29 09:05:23',None,'A','2','2'),
	('xxxxxx','2006-09-25 09:25:32',None,'A','3','3'),
	('xxxxxx','2000-06-21 10:03:10',None,'A','3','1'),
	('xxxxxx','2006-11-02 16:28:20',None,'A','1','2'),
	('xxxxxx','2000-10-07 10:02:21','2006-09-25 09:25:32','I','5','4')
]

sql = "INSERT INTO client (nom, prenom, dob, c_address, c_ville, postcode, telno1, telno2, sex_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = [
	('PHUANGKAEO','Phichet','1999-07-14','229 Rue Gambetta','Ronchin','59000','0766089558',null,'U'),
	('Karbiche','Rachid','2012-11-17','230 Rue Gambetta','La Madeleine','59160','0766089559','0766089560','M'),
	('Gagno','Anthony','2008-02-18','231 Rue Gambetta','Faches-Thumesnil','59350','0766089560',null, 'M'),
	('Allard','Frédéric','2002-07-25','232 Rue Gambetta','Lambersart','59777','0766089561',null,'M'),
	('Marie','Raccuglia','1995-07-01','233 Rue Gambetta','Lomme','59800','0766089562',null,'F')
]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount,"was inserted.")
