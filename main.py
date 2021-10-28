import sqlalchemy


engine = sqlalchemy.create_engine('postgresql://laitkilla:MSUMCFZZ342511m@localhost:5432/homework4_1')
engine

connection = engine.connect()

albums_2018 = connection.execute('SELECT Year_of_release, Album_name FROM ALBUMS WHERE Year_of_release =2018;').fetchall()
print(albums_2018)
duration_track = connection.execute('SELECT Track_name, Duration FROM Tracks ORDER BY Duration DESC;').fetchone()
print(duration_track)
duration_track_2 = connection.execute('SELECT Track_name, Duration FROM Tracks WHERE Duration >=210;').fetchall()
print(duration_track_2)
collections = connection.execute('SELECT Name_colletion FROM Collection WHERE Year_of_release BETWEEN 2018 and 2020;').fetchall()
print(collections)
one_word = connection.execute('SELECT Name_of_the_artist FROM Artists WHERE Name_of_the_artist not LIKE '%% %%';').fetchall()
print(one_word)
tracks = connection.execute('SELECT Track_name FROM Tracks WHERE Track_name ILIKE '%%my%%' or Track_name ILIKE '%%мой%%';').fetchall()
print(tracks)