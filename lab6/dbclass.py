import MySQLdb


class Connection:
    def __init__(self, user, passwd, db, host='localhost'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.use_unicode = True
        self.charset = "utf8"
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                use_unicode=self.use_unicode,
                charset=self.charset
            )


    def disconnect(self):
        if self._connection:
            self._connection.close()


class Computer:
    def __init__(self, db_connection, name, description):
        self.db_connection = db_connection.connection
        self.name = name
        self.description = description

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO `my_app_computer` (`name`, `description`) VALUES (%s, %s);", (self.name, self.description))

        self.db_connection.commit()
        c.close()

con = Connection('dbuser', '12345', 'first_db', 'localhost')
with con:
    computer = Computer(con, 'Компутер', 'Описание компутера')
    computer.save()
