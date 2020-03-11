from django.shortcuts import render
import psycopg2
def csvsql():
    conn = psycopg2.connect("host=localhost dbname=perso password=admin user=postgres")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE users(
    id integer PRIMARY KEY,
    email text,
    name text,
    address text)
    """)