import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_connection():
    try:
        # Database configuration from environment variables
        DB_HOST = os.getenv('DB_HOST', 'localhost')
        DB_NAME = os.getenv('DB_NAME', 'myapp')
        DB_USER = os.getenv('DB_USER', 'postgres')
        DB_PASSWORD = os.getenv('DB_PASSWORD', 'Jesuslove@12')
        DB_PORT = os.getenv('DB_PORT', '5432')
        
        print("Attempting to connect to PostgreSQL database...")
        print(f"Host: {DB_HOST}")
        print(f"Database: {DB_NAME}")
        print(f"User: {DB_USER}")
        print(f"Port: {DB_PORT}")
        
        # Attempt connection
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        
        print("\n✅ Successfully connected to the database!")
        print(f"PostgreSQL version: {db_version[0] if db_version else 'Unknown'}")
        
        # Test creating a table
        cur.execute('''
            CREATE TABLE IF NOT EXISTS test_table (
                id SERIAL PRIMARY KEY,
                test_data VARCHAR(100)
            );
        ''')
        
        cur.execute("INSERT INTO test_table (test_data) VALUES ('Test successful!');")
        conn.commit()
        
        cur.execute("SELECT * FROM test_table;")
        rows = cur.fetchall()
        
        print(f"\n✅ Successfully created and queried test table!")
        for row in rows:
            print(f"  Row: {row}")
        
        # Clean up
        cur.execute("DROP TABLE test_table;")
        conn.commit()
        
        cur.close()
        conn.close()
        
        print("\n✅ Database test completed successfully!")
        return True
        
    except Exception as e:
        print(f"\n❌ Error connecting to database: {e}")
        return False

if __name__ == "__main__":
    test_connection()