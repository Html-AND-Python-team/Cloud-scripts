DATABASE_URL = "postgresql://postgres:PyCoins2026@db.txtupflxioqqutekzvtn.supabase.co:5432/postgres"
import os
import psycopg

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT NOW()")
        print("Supabase OK:", cur.fetchone()[0])
