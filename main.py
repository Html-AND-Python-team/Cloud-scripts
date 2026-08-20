import os
import psycopg


def main():
    database_url = os.environ["DATABASE_URL"]

    with psycopg.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT NOW()")
            result = cur.fetchone()

    print(f"Supabase OK: {result[0]}")


if __name__ == "__main__":
    main()
