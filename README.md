<div align="center">
  <h3 align="center">MUSYCA</h3>

  <p align="center">
    Your own music listening habits database!<br>
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/crdpa/musyca?style=for-the-badge"><br>
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/crdpa/musyca?style=for-the-badge"><br>
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/crdpa/musyca?style=for-the-badge"><br>
  </p>
</div>

## ABOUT

Musyca is a python application that uses SQLite to store your music listening habits. I wrote for myself to use with [cmus music player](https://cmus.github.io/), but it is capable of interacting with any music player that can output the title song, artist name and album name.

Usage:
    musyca.py --artist "artist name" --album "album name" --title "song title"

The application only creates and populate the database with song title, album name, artist name and date played. It does NOT show any information. You have to interact with the database for that.

I'm still debating if displaying formatted information should be the aim of this application. I think creating other projects (like a web page) to interact with the database is a better solution.

## TODO
- [ ] option to use a remote SQLite database

## SCRIPTS

In the scripts folder there is a bash script made for cmus. Put the path to it in cmus "status_display_program" and it should work. Don't forget to edit the script to point to the "musyca" executable.
