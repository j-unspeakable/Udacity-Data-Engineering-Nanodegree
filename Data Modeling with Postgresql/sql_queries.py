# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays
        (
            songplay_id SERIAL PRIMARY KEY,
            start_time TIMESTAMP NOT NULL,
            user_id INTEGER,
            level VARCHAR,
            song_id VARCHAR,
            artist_id VARCHAR,
            session_id INTEGER, 
            location VARCHAR,
            user_agent VARCHAR,
            FOREIGN KEY(song_id) REFERENCES songs(song_id),
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(artist_id) REFERENCES artists(artist_id),
            FOREIGN KEY(start_time) REFERENCES time(start_time)
        );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
        (
            user_id INTEGER PRIMARY KEY,
            first_name VARCHAR NOT NULL,
            last_name VARCHAR NOT NULL,
            gender CHAR(1),
            level VARCHAR
        );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs
        (
            song_id VARCHAR PRIMARY KEY,
            title VARCHAR NOT NULL,
            artist_id VARCHAR NOT NULL,
            year INTEGER CHECK (year >= 0),
            duration FLOAT NOT NULL
        );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists
        (
            artist_id VARCHAR PRIMARY KEY,
            name VARCHAR NOT NULL,
            location VARCHAR,
            latitude DECIMAL,
            longitude DECIMAL
        );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
        (
            start_time TIMESTAMP PRIMARY KEY,
            hour INTEGER NOT NULL CHECK (hour >= 0),
            day INTEGER NOT NULL CHECK (day >= 0),
            week INTEGER NOT NULL CHECK (week >= 0),
            month INTEGER NOT NULL CHECK (month >= 0),
            year INTEGER NOT NULL CHECK (year >= 0),
            weekday VARCHAR NOT NULL
        );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays
        (
            start_time,
            user_id,
            level,
            song_id,
            artist_id,
            session_id,
            location,
            user_agent
        )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT
    DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users
        (
        user_id,
        first_name,
        last_name,
        gender, 
        level
        )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE 
        SET level=EXCLUDED.level;
""")

song_table_insert = ("""
    INSERT INTO songs
        (
        song_id,
        title,
        artist_id,
        year,
        duration        
        )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id)
    DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists
        (
            artist_id,
            name,
            location,
            latitude,
            longitude
        )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO time 
        (
            start_time,
            hour,
            day,
            week,
            month,
            year,
            weekday
        )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time)
    DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT
        s.song_id AS song_id,
        s.artist_id AS artist_id
    FROM
        songs AS s
    INNER JOIN 
        artists AS a
        ON s.artist_id = a.artist_id
    WHERE
        s.title = %s AND 
        a.name = %s AND 
        s.duration = %s  
        
""")

# QUERY LISTS

create_table_queries = [time_table_create, user_table_create, artist_table_create,
                         song_table_create, songplay_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop,
                         artist_table_drop, time_table_drop]