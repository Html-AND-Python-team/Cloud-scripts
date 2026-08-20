import os
import time
import psycopg
from datetime import datetime

DATABASE_URL = "postgresql://postgres:PyCoins2026@db.txtupflxioqqutekzvtn.supabase.co:5432/postgres"


def ping():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT NOW();")
            ahora = cur.fetchone()[0]
            print(f"[{datetime.now():%H:%M:%S}] OK -> {ahora}")


def main():
    print("PyCoin Supabase Keeper iniciado")

    while True:
        try:
            ping()
        except Exception as e:
            print("ERROR:", e)

        # Espera 5 minutos
        time.sleep(300)


if __name__ == "__main__":
    main()
