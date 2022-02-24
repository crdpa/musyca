#!/usr/bin/env python3

import argparse
import os.path
import sys
import sqlite3
from datetime import date
from pathlib import Path
from sqlite3 import Error
from shutil import which


def check_requirements():
    """ check if sqlite3 is installed """
    if which("sqlite3") is None:
        print("SQLite not available")
        sys.exit()


def check_dir(db_dir):
    """ create database directory """
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)


def create_connection(db_file):
    """ create a connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        sys.exit()

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        sys.exit()


def insert_song(conn, track):
    """ insert or update current song into the database """
    sql = """INSERT INTO songs (name, date, album)
          SELECT (?) AS song_name, (?) AS date,
          id AS album FROM albums WHERE name = (?)"""
    cur = conn.cursor()
    cur.execute(sql, track)
    conn.commit()
    return cur.lastrowid


def insert_album(conn, album):
    """ insert or update current album into the database """
    sql = """INSERT INTO albums (name, artist)
          SELECT (?) AS album_name, id AS artist
          FROM artists WHERE name = (?)
          ON CONFLICT DO NOTHING"""
    cur = conn.cursor()
    cur.execute(sql, album)
    conn.commit()
    return cur.lastrowid


def insert_artist(conn, artist):
    """ insert or update current artist into the database """
    sql = """INSERT INTO artists (name) VALUES (?)
          ON CONFLICT DO NOTHING"""
    cur = conn.cursor()
    cur.execute(sql, artist)
    conn.commit()
    return cur.lastrowid


def main():
    parser = argparse.ArgumentParser(prog='musyca.py',
                                     usage='%(prog)s -a [artist] -l [album] '
                                           ' -t [song title]')
    parser.add_argument('--artist', '-a', type=str, required=True,
                        help='artist name')
    parser.add_argument('--album', '-l', type=str, required=True,
                        help='album title')
    parser.add_argument('--title', '-t', type=str, required=True,
                        help='song title')
    args = parser.parse_args()

    db_dir = str(Path.home())+r'/.config/musyca'
    db_file = db_dir+r'/database.db'

    sql_create_songs_table = """ CREATE TABLE IF NOT EXISTS songs (
                                      id INTEGER PRIMARY KEY,
                                      name varchar(100) NOT NULL,
                                      date date NOT NULL,
                                      album INTEGER NOT NULL,
                                      FOREIGN KEY (album) REFERENCES albums(id)
                                  );"""

    sql_create_albums_table = """ CREATE TABLE IF NOT EXISTS albums (
                                      id INTEGER PRIMARY KEY,
                                      name varchar(100) NOT NULL,
                                      artist INTEGER NOT NULL,
                                      FOREIGN KEY (artist) REFERENCES artists(id)
                                      UNIQUE (name)
                                  );"""

    sql_create_artists_table = """ CREATE TABLE IF NOT EXISTS artists (
                                       id INTEGER PRIMARY KEY,
                                       name varchar(100) NOT NULL,
                                       UNIQUE (name)
                                   );"""

    check_requirements()
    check_dir(db_dir)
    conn = create_connection(db_file)

    if conn is not None:
        create_table(conn, sql_create_songs_table)
        create_table(conn, sql_create_albums_table)
        create_table(conn, sql_create_artists_table)

        today = date.today()
        insert_artist(conn, (args.artist,))
        insert_album(conn, (args.album, args.artist))
        insert_song(conn, (args.title, today, args.album))

    else:
        print("Cannot create the database connection.")
        sys.exit()


if __name__ == "__main__":
    main()
