from worldconn import get_connection

try:
    conn = get_connection() # 디비 연결 코드
    with conn.cursor() as cursor:
        # 수정할 데이터 입력
        Name = input('수정할 조건 도시명(Ansan): ')
        District = input('도명(Kyonggi): ')
       
       
        
        ## 데이터 수정 쿼리
        update_query = """
        UPDATE city
        SET District = %s
        WHERE name = %s;
        """
        
        # 수정할 데이터
        data_to_update = (District, Name)
        
        # cursor.execute("UPDATE city SET District = %s WHERE name = %s;",('서울시',"MSJ_City"))
        cursor.execute(update_query, data_to_update)
        conn.commit()
        print('도시정보 업데이트 함!')
        
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