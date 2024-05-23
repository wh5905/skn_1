



def 데이터베이스만들때():
    import pymysql.cursors


    # Establish a connection to your MySQL server.
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='')

    try:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE mydatabase")
    finally:
        connection.close()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def 테이블만들때():
    import pymysql.cursors
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='mydatabase')
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(40),
                address VARCHAR(100)
            )
            """)
        connection.commit()
    finally:
        connection.close()    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def 테이블에레코드인서트할때():
    import pymysql.cursors
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='test')
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO crawling (itemname, price, link) VALUES ('{}', '{}', '{}')").format("itemname", "price", "link")
        connection.commit()
    finally:
        connection.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def 테이블에서내용조회할때():
    import pymysql.cursors
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='mydatabase')
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT * FROM customers
            """)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def 테이블에서내용수정할때():
    import pymysql.cursors
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='mydatabase')
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
            UPDATE customers 
            SET address='456 New St' 
            WHERE name='John Doe'
            """)
        connection.commit()
    finally:
        connection.close()    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def 테이블에서내용삭제할때():
    import pymysql.cursors
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='mydatabase')
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
            DELETE FROM customers 
            WHERE name='John Doe'
            """)
        connection.commit()
    finally:
        connection.close()    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def 테이블에서내용넣을때():
    import pymysql.cursors
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='mydatabase')
    try:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                INSERT INTO customers (name, address) 
                VALUES ('John Doe', '123 Main St')
                """)
                connection.commit()
            except pymysql.Error as e:
                print(f"An error occurred: {e.args[0]}, {e.args[1]}")
    finally:
        connection.close()    