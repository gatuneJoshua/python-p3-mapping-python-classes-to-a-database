from config import CONN, CURSOR

class Song:
    pass
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT)
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES ( ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0] # it is added to the database and set it as the object ID
        CONN.commit()  # close the connection always after saving

    @classmethod
    def create(cls, name, album):  # create and save songs using one method
        song = Song(name, album)
        song.save()
        return song

    #The __repr__ method in Python is a special method that defines how an object of a class should be represented as a string.
    def __repr__(self):
        return f'{self.id} {self.name}, {self.album}'

song1 = Song.create("Sability", "Ayra Starr")
print(song1)

