#!/usr/bin/env bash

# change $musyca to where the executable is
musyca="$HOME/bin/musyca"

cur_song_file="/tmp/cmus_song"
cur_state_file="/tmp/cmus_state"

# create files if it's not there
if [ ! -f "$cur_state_file" ]; then
    touch "$cur_state_file"
    prev_state=""
fi

if [ ! -f "$cur_song_file" ]; then
    touch "$cur_song_file"
fi

artist=$(cmus-remote -C "format_print %{artist}")
album=$(cmus-remote -C "format_print %{album}")
title=$(cmus-remote -C "format_print %{title}")
status=$(cmus-remote -C "format_print %{status}")

register_song() {
    python3 "$musyca" -a "$artist" -l "$album" -t "$title"
}

# if cmus is paused, register the state and current song in temp files and exit
if [ "$status" == "|" ]; then
    echo "|" > "$cur_state_file"
    echo "$artist - $title" > "$cur_song_file"
    exit 0
fi

# if cmus is stopped, clean state and song temp files
if [ "$status" == "." ]; then
    echo "" > "$cur_state_file"
    echo "" > "$cur_song_file"
    exit 0
fi

# check previous cmus state and song
prev_state=$(cat "$cur_state_file")
prev_song=$(cat "$cur_song_file")

# if cmus is playing, check if artist and song are the same as the previous one in the temp file
if [ "$status" == ">" ]; then

    # if it is the same, but you started the song from the beginning (it is not resuming), register
    if [ "$artist - $title" == "$prev_song" ] && [ "$prev_state" != "|" ]; then
        register_song
        exit 0

    # if it is a different song, register
    else
        echo "$artist - $title" > "$cur_song_file"
        echo "" > "$cur_state_file"
        register_song
    fi
fi

