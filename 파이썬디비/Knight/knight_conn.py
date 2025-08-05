import pymysql

def get_connection():
    """MySQL 데이터베이스 연결코드"""
    
    return pymysql.connect(
        host = 'localhost', # 127.0.0.1
        user='root',        # 계정명
        password='1234',    # 패스워드
        database = 'testdb', # 연동디비명
        port=3306
)

