<div align="center">
  <h1 align="center">MUSYCA</h1>

  <p align="center">
    Your own music listening database!<br><br>
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/crdpa/musyca?style=for-the-badge">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/crdpa/musyca?style=for-the-badge">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/crdpa/musyca?style=for-the-badge"><br>
  </p>
</div>

## ABOUT

Musyca is a python application that uses SQLite to store your music listening habits. I wrote Musyca to use with [cmus music player](https://cmus.github.io/), but it can be used with any music player that can output the song title, artist name and album name.

Usage:
    musyca.py --artist "artist name" --album "album name" --title "song title"

The application only creates and populate the database with song title, album name, artist name and date. It does NOT show any information. You have to interact with the database for that.

You can use [Kolekti](https://github.com/crdpa/kolekti) to check the top played songs, albums and artists.

## SCRIPTS

In the scripts folder there is a bash script made for cmus. Put the path to it in cmus "status_display_program" and it should work. Don't forget to edit the script to point to the "musyca" executable.

## LINKS

 - [Kolekti](https://github.com/crdpa/kolekti): interact with Musyca's database.
