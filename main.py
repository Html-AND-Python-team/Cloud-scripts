database_url = "postgresql://postgres:PyCoins2026@db.txtupflxioqqutekzvtn.supabase.co:5432/postgres"
import os
import psycopg


def main():
    with psycopg.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT NOW()")
            result = cur.fetchone()

    print(f"Supabase OK: {result[0]}")


if __name__ == "__main__":
    main()
