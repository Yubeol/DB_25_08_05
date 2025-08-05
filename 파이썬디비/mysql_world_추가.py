from worldconn import get_conntion

try:
    conntion = get_conntion()
    with conntion.cursor() as cursor:
       # 직접 입력
       Name = input('도시명(Ansan): ')
       CountryCode = input('국가코드(KOR): ')
       District = input('도명(Kyonggi): ')
       Population = int(input('인구수: '))
       
       # 데이터 입력 sql
       insert_query = """ 
        INSERT INTO CITY (Name, CountryCode, District, Population)
        VALUES (%s, %s, %s, %s);
       """
       
       #입력할 데이터
       data_to_insert = (Name, CountryCode,District, Population)
       
       cursor.execute(insert_query, data_to_insert)
       conntion.commit()
       print('데이터가 잘 주가되었음!!')
       
    with conntion.cursor() as cursor:
        # sql_query = """
        #     SELECT ID Name, CountryCode, District, Population
        #     FROM city WHERE Name=%s;
        # """
        
        sql_query = """
            SELECT ID, Name, CountryCode, District, Population
            FROM city order by ID desc limit 5;
        """
        
        #cursor.execute(sql_query, Name)
        cursor.execute(sql_query)
        
        result = cursor.fetchall()
        for row in result:
            print(row)
                
    # with connection.cursor() as cursor:
    #     sql_query = """
    #     SELECT ID Name, CountryCode, District, Population
    #     FROM city;
    #     """
    #     cursor.execute(sql_query)
    #     result = cursor.fetchall() # 실제 디비에서 조회된 결과셋 정보를 가져옴

    #     for row in result:
    #         print(row)
       
except get_conntion.MySQLError as e:
    print('데이터 입력 오류 발생:', e)
finally:
    # 데이터베이스 연결 닫기
    conntion.close()
    print('디비 연결 종료')
    
# try:  # 문제가 발생 할 수도 있는 코드
#     num1 = int(input('정수1: '))
#     num2 = int(input('정수2: '))

#     result = num1 / num2
# except ZeroDivisionError:
#     print('0으로 나눌수 없음')
# except ValueError:
#     print('숫자만 입력가능함')
# finally:
#     print('종료')