from dbconnection import create_db_connection

uname = "sreehari"
pwd = "Rsri@Nov1983"

try:
    engine=create_db_connection(username=uname,password=pwd)
    engine.connect()
    print("✅ SQLAlchemy connected successfully!")
except Exception as e:
    print("❌ SQLAlchemy connection failed:", e)