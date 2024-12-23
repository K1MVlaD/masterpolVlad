import pymysql
import sys
class SQL:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='root', database='Boba')
        try:
            with self.connection:
                self.cr = self.connection.cursor()
                self.cr.execute("SELECT VERSION()")
                print(self.connection.get_host_info())
        except:
            sys.exit()
    def login(self, fio, password):
        self.connection = pymysql.connect(host='localhost', user='root', password='root', database='Boba')
        with self.connection:
            self.cr = self.connection.cursor()
            sql = "SELECT FIO, password FROM sotrudniki WHERE FIO = %s AND password = %s"
            self.cr.execute(sql, (fio, password))
            result = self.cr.fetchall()
            return result
    def newpostavshik(self, FIO, type, INN):
        self.connection = pymysql.connect(host='localhost', user='root', password='root', database='Boba')
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `supplier` (`FIO`, `_type`, `INN`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (FIO, type, INN))
        self.connection.commit()
    def dobpartner(self, name, FIO, email, num, address, INN, rating):
        self.connection = pymysql.connect(host='localhost', user='root', password='root', database='Boba')
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `partner` (`_type`, `_name`, `director`, `email`, `num`, `address`, `INN`, `rating`) VALUES ('OOO', %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, FIO, email, num, address, INN, rating))
        self.connection.commit()
    def dobzakaz(self, name, partner, product, kol):
        self.connection = pymysql.connect(host='localhost', user='root', password='root', database='Boba')
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `zakazi` (`nam`, `partner_id`, `products_id`, `kol`, `stat`) VALUES (%s, %s, %s, %s, 'Новое')"
            cursor.execute(sql, (name, partner, product, kol))
        self.connection.commit()
    def pokaz_partneri(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='root', database='Boba')
        with self.connection:
            self.cr = self.connection.cursor()
            sql = 'SELECT * FROM partner'
            self.cr.execute(sql)
            result = self.cr.fetchall()
            for x in result:
                print(123)
            return result
    def pokaz_postavshiki(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='root', database='Boba')
        with self.connection:
            self.cr = self.connection.cursor()
            sql = 'SELECT * FROM supplier'
            self.cr.execute(sql)
            result = self.cr.fetchall()
            for x in result:
                print(321)
            return result
    def pokaz_zakazi(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='root', database='Boba')
        with self.connection:
            self.cr = self.connection.cursor()
            sql = 'SELECT z.statement_id, z.nam, p._name AS _name, pr._name AS _name, z.kol, z.stat FROM zakazi z LEFT JOIN partner p ON z.partner_id = p.partner_id LEFT JOIN products pr ON z.products_id = pr.product_id;'
            self.cr.execute(sql)
            result = self.cr.fetchall()
            for x in result:
                print(321)
            return result
