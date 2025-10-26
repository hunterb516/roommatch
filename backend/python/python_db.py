import mysql.connector
from tabulate import tabulate

def open_database(hostname, user_name, mysql_pw, database_name):
    global conn, cursor
    conn = mysql.connector.connect(
        host=hostname,
        user=user_name,
        password=mysql_pw,
        database=database_name
    )
    cursor = conn.cursor()

def printFormat(result):
    """
    Formats a result set with headers via tabulate.
    """
    headers = [col[0] for col in cursor.description]
    print("\nQuery Result:\n")
    return tabulate(result, headers=headers)

def executeSelect(query):
    """
    Executes a SELECT query and returns the formatted results.
    """
    cursor.execute(query)
    return printFormat(cursor.fetchall())

def insert(table, values):
    """
    Inserts a new row into `table`.
    `values` should be the comma-separated column values (no enclosing parentheses).
    """
    sql = f"INSERT INTO `{table}` VALUES ({values});"
    cursor.execute(sql)
    conn.commit()

def nextId(table):
    """
    Returns the next integer primary key for `table`, assuming the PK column
    is named <TableName>Id (e.g. Student → StudentId).
    """
    pk = table + 'Id'
    sql = (
        f"SELECT IFNULL(MAX(`{pk}`), 0) AS max_id "
        f"FROM `{table}`;"
    )
    cursor.execute(sql)
    row = cursor.fetchone()
    current_max = row[0] if row and row[0] is not None else 0
    return current_max + 1

def executeUpdate(query):
    """
    Executes an UPDATE or DELETE query.
    """
    cursor.execute(query)
    conn.commit()

def close_db():
    """
    Closes cursor and connection.
    """
    cursor.close()
    conn.close()
