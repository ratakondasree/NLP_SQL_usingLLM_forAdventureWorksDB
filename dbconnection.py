import os
from dotenv import load_dotenv
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.utilities import SQLDatabase



load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

server = "LAPTOP-RES6G37K"
database = "atliq_tshirts"


def create_db_connection(username,password):
    connection_url = URL.create(
        "mssql+pyodbc",
        username=username,
        password=password,
        host="tcp:" + server,
        port=1433,
        database=database,
        query={"driver": "ODBC Driver 17 for SQL Server"}
    )

    engine = create_engine(connection_url)
    return engine 



# llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# # ✅ Create SQLDatabaseChain
# db_chain = SQLDatabaseChain.from_llm(llm, dbconn, verbose=True)

# # Example: Convert Natural Language to SQL
# nl_query = "how many total blue nike t-shirts are available?"

# # ✅ Generate SQL Query & Execute
# result = db_chain.invoke(nl_query)

# print("Query Result:", result)
