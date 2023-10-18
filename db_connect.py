import psycopg2
import pygame
import random


# Function that takes as input the emotion label and fetches all relevant song records under that label
def fetch_data(emo_label):
    # Connect to the DBMS PostgreSQL
    connection = psycopg2.connect(
    # Connect to the music database specifically
    database = "music_DB",
    user = "postgres",
    password = "Donyewakefield1999!"
    )

    # Open a cursor to perform database operations
    cur = connection.cursor()
    # Obtain label from AI model
    label = emo_label
    # Fetch all relevant info for the songs
    cur.execute(f"SELECT title, artists, songs.file_path, images.file_path, background_img FROM songs INNER JOIN images ON songs.img_id = images.img_id WHERE song_label = '{label}'")
    # Store query results as records
    records = cur.fetchall()  

    cur.close()
    connection.close()
    return records
