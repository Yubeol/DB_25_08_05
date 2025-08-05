# 데이터베이스 테이블 생성
# UI구성 초기생성, 기사추가, 기사목록, 기사검색, 정보수정, 화면클리어, 종료

# main() 설계, 각각의 함수정의해야함(초기생성, 기사추가, 기사목록, 기사검색, 정보수정, 화면클리어, 종료)

import os, sys
from knight_conn import get_connection # 디비연동함수 호출

def screen():       # 메뉴 출력
    print('\n 간단한 데이터베이스 연동 기사 관리 프로그램 ####')
    print('0.초기생성 1.기사추가, 2.기사목록, 3.기사검색, 4.정보수정, 5.기사삭제, 6.화면클리어, 7.종료 8.제거')

def createNodeInit():   # 초기생성
    pass

def knightAdd():    # 기사 정보 추가
    name = input('기사명(SINKNIGHT): ')
    email = input('기사 이메일(kin@gmail.com): ')
    age = input('기사연령(25): ')
    
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            insert_sql = """INSERT INTO knight (name, email, age)VALUES (%s, %s, %s);"""
            
            insert_value = (name, email, age)
            cursor.execute(insert_sql, insert_value)
        conn.commit()
        print(f'{name}기사님 추가되었음!')
    except Exception as e:
        print(f'기사 전체 목록 추가 중 예외발생:{e}')
    finally:
        conn.close()

def knightAllList():    # 기사 전체 목록 출력
    print('\n---------------- 기사 전체 목록 ------------------')
    print('순번\t\t기사명\t\t\t이메일\t\t\t나이')
    print('--------------------------------------------------')
    conn = get_connection() # 디비 연결
    
    try:
        with conn.cursor() as cursor:
            view_sql = """SELECT idx, name, email, age FROM knight WHERE is_del=%s;"""
            cursor.execute(view_sql, 0)    # 커서를 이용한 쿼리 실행
            result = cursor.fetchall()  # 커서.fetchall 함수는 SELECT쿼리 때만 사용.
            for row in result:
                print(f'{row[0]} \t\t {row[1]} \t\t {row[2]} \t\t {row[3]} \t\t')
    except Exception as e:
        print(f'기사 전체 목록 출력 중 예외발생:{e}')
    finally:
        conn.close()

def knightSearch():     # 기사 정보 검색
    name = input('기사명(SINKNIGHT): ')
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            select_one_sql = """SELECT * FROM knight WHERE name=%s AND is_del=%s;"""
            select_one_value = (name, 0)
            cursor.execute(select_one_sql, select_one_value)
            result = cursor.fetchall()
            for row in result:
                print(f'{row[0]} \t\t {row[1]} \t\t {row[2]} \t\t {row[3]} \t\t')
                
    except Exception as e:
        print(f'기사 전체 목록 변경 중 예외발생:{e}')
    finally:
        conn.close()

def knightUpdate():     # 기사 정보 업데이드
    name = input('기사명(SINKNIGHT): ')
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            select_one_sql = """SELECT * FROM knight WHERE name=%s AND is_del=%s;"""
            select_one_value = (name, 0)
            cursor.execute(select_one_sql, select_one_value)
            result = cursor.fetchall()
    
            if result: # SELECT 결과가 1개 이상 있는 경우
                for row in result:
                    print(f'{row[0]} \t\t {row[1]} \t\t {row[2]} \t\t {row[3]} \t\t')
                    
                updateEmail = input('이메일 변경(kim@nate.com)-> ')
                updateAge = input('연령 변경(30)-> ')
                
                with conn.cursor() as cursor:
                    update_sql = """UPDATE knight SET email=%s, age=%s WHERE name=%s"""
                    update_value = (updateEmail, updateAge, name)
                    cursor.execute(update_sql, update_value)
                
                conn.commit()
                print(f'{name}기사님 정보가 변경되었음!')
            else:
                print(f'{name}기사님 정보변경되었음!')
    except Exception as e:
        print(f'기사 전체 목록 변경 중 예외발생:{e}')
    finally:
        conn.close()


def knightDel():     # 기사 정보 삭제
    name = input('제거할 기사명(SINKNIGHT): ')
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # select_one_sql = """SELECT * FROM knight WHERE name=%s;"""
            select_one_sql = """SELECT * FROM knight WHERE name=%s AND is_del=%s;"""
            select_one_value = (0, name)
            # cursor.execute(select_one_sql, name)
            cursor.execute(select_one_sql, select_one_value)
            result = cursor.fetchall()
            
            if result:  # SELECT 결과가 1개 이상 있는 경우만 삭제
                with conn.cursor()as cursor:
                    #delete_sql = """DELETE FROM knight WHERE name = %s"""
                    delete_sql = """UPDATE knight SET is_del=%s WHERE name = %s"""
                    delete_value = (1, name)
                    # cursor.execute(delete_sql, name)
                    cursor.execute(delete_sql, delete_value)
                conn.commit()
                print(f'{name}기사님 제거되었음!')
            else:
                print(f'{name}기사님 정보가 없음! (확인바람)')
    except Exception as e:
        print(f'기사 제거 중 예외발생:{e}')
    finally:
        conn.close()

def knightDelList():    # 기사 전체 목록 출력
    print('\n----------------제거된 기사 전체 목록 ------------------')
    print('순번\t\t기사명\t\t\t이메일\t\t\t나이')
    print('--------------------------------------------------')
    conn = get_connection() # 디비 연결
    
    try:
        with conn.cursor() as cursor:
            view_sql = """SELECT idx, name, email, age FROM knight WHERE is_del=%s;"""
            cursor.execute(view_sql, 1)    # 커서를 이용한 쿼리 실행
            result = cursor.fetchall()  # 커서.fetchall 함수는 SELECT쿼리 때만 사용.
            for row in result:
                print(f'{row[0]} \t\t {row[1]} \t\t {row[2]} \t\t {row[3]} \t\t')
    except Exception as e:
        print(f'기사 전체 목록 출력 중 예외발생:{e}')
    finally:
        conn.close()

if __name__ == '__main__':
    knightlist = [] # 초기 변수 필요없음. 디비 하기 때문에
    while True:
        screen()
        try:
            choice = int(input('-> '))
        except:
            continue
        match choice:
            case 0:
                pass
            case 1:
                knightAdd()
            case 2:
                knightAllList() 
            case 3:
                knightSearch()   
            case 4:
                knightUpdate()      # 기사 정보 업데이트
            case 5:
                knightDel()
            case 6:
                os.system('cls') # 콘솔 터미널창에서 화면 지우기 기능 호출
            case 7:
                sys.exit(1) # 강제 종료
            case 8:
                knightDelList()
            case _:
                print("잘못된 번호입니다. 다시 입력하세요.")