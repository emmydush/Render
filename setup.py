import os
import sys
import subprocess
import psycopg2
from dotenv import load_dotenv

def setup_application():
    """Setup script for the Python PostgreSQL Web App"""
    print("🚀 Setting up Python PostgreSQL Web App...")
    
    # Load environment variables
    load_dotenv()
    
    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found!")
        return False
    
    # Install Python dependencies
    print("📦 Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Python dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing Python dependencies: {e}")
        return False
    
    # Test database connection
    print("🔌 Testing database connection...")
    try:
        DB_HOST = os.getenv('DB_HOST', 'localhost')
        DB_NAME = os.getenv('DB_NAME', 'myapp')
        DB_USER = os.getenv('DB_USER', 'postgres')
        DB_PASSWORD = os.getenv('DB_PASSWORD', 'Jesuslove@12')
        DB_PORT = os.getenv('DB_PORT', '5432')
        
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        conn.commit()
        cur.close()
        conn.close()
        
        print("✅ Database connection successful!")
        print("✅ Users table created/verified!")
        
    except Exception as e:
        print(f"❌ Error with database setup: {e}")
        print("💡 Make sure PostgreSQL is running and credentials are correct")
        return False
    
    print("\n🎉 Setup completed successfully!")
    print("\nTo run the application:")
    print("  python app.py")
    print("\nTo test the database connection separately:")
    print("  python test_db.py")
    print("\nAPI endpoints:")
    print("  GET  /          - Welcome message")
    print("  GET  /health     - Health check")
    print("  GET  /users      - Get all users")
    print("  POST /users      - Create a new user")
    
    return True

if __name__ == "__main__":
    setup_application()