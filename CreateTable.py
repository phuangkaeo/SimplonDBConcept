import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="phuangkaeo",
    password="simplon59",
    database="pycharm"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE city ("
                 "city_id INT NOT NULL AUTO_INCREMENT,"
                 "city_Name VARCHAR(50) NOT NULL,"
                 "inhabitants_number int,"
                 "distance_agent INT,"
                 "PRIMARY KEY (city_id))ENGINE=INNODB")

mycursor.execute("CREATE TABLE type ("
                 "type_id INT NOT NULL AUTO_INCREMENT,"
                 "type VARCHAR(40) NOT NULL,"
                 "description varchar(255),PRIMARY KEY (type_id))"
                 "ENGINE=INNODB")

mycursor.execute("CREATE TABLE logement ("
                 "lod_id INT NOT NULL AUTO_INCREMENT,"
                 "lod_address VARCHAR(50),"
                 "lod_ville VARCHAR(255),"
                 "size VARCHAR(50),"
                 "quartier VARCHAR(255),"
                 "prix INT,"
                 "loyer INT,"
                 "city_id INT REFERENCES city(city_id),"
                 "type_id INT REFERENCES typ(type_id),"
                 "PRIMARY KEY (lod_id))"
                 "ENGINE=INNODB")

mycursor.execute("CREATE TABLE contract("
                 "contract_id INT NOT NULL AUTO_INCREMENT,"
                 "contract_detail VARCHAR(255),"
                 "contract_start_date DATETIME NOT NULL,"
                 "contract_end_date DATETIME,"
                 "contract_status CHAR(2),"
                 "client_id INT REFERENCES client(client_ID),"
                 "lod_id INT REFERENCES logement(lod_id),"
                 "PRIMARY KEY (contract_id))"
                 "ENGINE=INNODB")

mycursor.execute("CREATE TABLE sex("
                 "sex_id char(2) NOT NULL,"
                 "sex varchar(25))"
                 "ENGINE=INNODB")

mycursor.execute("CREATE TABLE client("
                 "client_id INT NOT NULL AUTO_INCREMENT,"
                 "nom VARCHAR(255),"
                 "prenom VARCHAR(255),"
                 "dob DATETIME,"
                 "c_address VARCHAR(40),"
                 "c_ville VARCHAR(40),"
                 "postcode VARCHAR(25),"
                 "telno1 VARCHAR(10),"
                 "telno2 VARCHAR(10),"
                 "sex_id char(2) REFERENCES sex(sex_id),"
                 "PRIMARY KEY (client_id))"
                 "ENGINE=INNODB")

mycursor.execute("CREATE TABLE telephone("
                 "tel_id int NOT NULL AUTO_INCREMENT,"
                 "telno varchar(25),"
                 "client_id int REFERENCES client(client_id),"
                 "PRIMARY KEY (tel_id))"
                 "ENGINE=INNODB")
