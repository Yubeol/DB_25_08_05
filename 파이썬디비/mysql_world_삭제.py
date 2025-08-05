from worldconn import get_connection

try:
    conn = get_connection() # 디비 연결 코드
    with conn.cursor() as cursor:
       # 삭제할 데이터 입력
        Name = input('삭제할 도시명(Ansan): ')
       
       # 데이터 삭제 쿼리
        delete_query = """DELETE FROM city WHERE name = %s;"""
       
       # 데이터 삭제 cursor코드
        cursor.execute(delete_query, Name)
        conn.commit()
        print('도시정보 삭제함!')
        
    with conn.cursor() as cursor:
        
        sql_query = """
            SELECT ID, Name, CountryCode, District, Population
            FROM city order by ID desc limit 5;
        """
        
        cursor.execute(sql_query)
        
        result = cursor.fetchall()
        for row in result:
            print(row)
        
except Exception as e:
    print(f'데이터 수정시 예외발생 : (e)')
finally:
    print(f'데이터 베이스 종료')
    conn.close()