CREATE = """
    CREATE TABLE IF NOT EXISTS performes (id SERIAL PRIMARY KEY, name VARCHAR(40) NOT NULL);

	CREATE TABLE IF NOT EXISTS album (id SERIAL PRIMARY KEY, name VARCHAR(40) NOT NULL, release INTEGER NOT NULL);

	CREATE TABLE IF NOT EXISTS tracks (id SERIAL PRIMARY KEY, name VARCHAR(40) NOT NULL, duration INTEGER NOT NULL);
	
	CREATE TABLE IF NOT EXISTS genre(id SERIAL PRIMARY KEY, name VARCHAR(40) NOT NULL);

	CREATE TABLE IF NOT EXISTS collection(id SERIAL PRIMARY KEY, name VARCHAR(40) NOT NULL, release INTEGER NOT NULL);
	
	
    CREATE TABLE IF NOT EXISTS performes_genre (performes_id INTEGER REFERENCES performes(id),
	genre_id INTEGER REFERENCES genre(id), CONSTRAINT pk PRIMARY KEY (performes_id, genre_id));

	CREATE TABLE IF NOT EXISTS performes_album (performes_id INTEGER REFERENCES performes(id),
	album_id INTEGER REFERENCES album(id), CONSTRAINT pk2 PRIMARY KEY (performes_id, album_id));

	CREATE TABLE IF NOT EXISTS tracks_collection (tracks_id INTEGER REFERENCES tracks(id),
	collection_id INTEGER REFERENCES collection(id), CONSTRAINT pk3 PRIMARY KEY (tracks_id, collection_id));

	ALTER TABLE tracks add column album_id integer references album(id);
"""