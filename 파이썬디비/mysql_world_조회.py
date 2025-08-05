from worldconn import get_connection
import pymysql

try: # 데이터 조회 SELECT
    connection = get_connection()
    with connection.cursor() as cursor:
        sql_query = """
            SELECT ID Name, CountryCode, District, Population
            FROM city;
        """
        
        cursor.execute(sql_query)
        result = cursor.fetchall() # 실제 디비에서 조회된 결과셋 정보를 가져옴

        for row in result:
            print(row)
        
except Exception as e:
    print('데이터 입력 오류 발생:', e)
finally:
    # 데이터베이스 연결 닫기
    connection.close()
    print('디비 연결 종료')