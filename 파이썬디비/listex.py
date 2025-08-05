import os
import sys

def screen():
    print("\n### 간단한 회원 관리 프로그램 ###")
    print("0.초기생성 1.멤버추가 2.멤버리스트 3.멤버찾기 4. 정보수정 5. 화면지우기 6.종료")

def createNodeInit(memlist):
    newNode = createNode()
    newNode.append("Moon")
    newNode.append("msj8086@nate.com")
    newNode.append(23)

    memlist.append(newNode)
    return memlist

def createNode():
    newNode = []
    return newNode

def memberAdd(memlist) :
    newNode = createNode()

    name = input("->이름: ")
    newNode.append(name)
    email = input("->이메일: ")
    newNode.append(email)
    age = int(input("->나이: "))
    newNode.append((age))

    memlist.append(newNode)
    return memlist

def memberAllList(memlist):
    print("\n-------- 정보 -----------")
    print("이름\t\t이메일\t\t\t나이")
    for mem in memlist:
        print("%s\t%s\t %d" % (mem[0], mem[1], mem[2]))

def memberSearch(memlist):
    ser_name = input("찾고하고 싶은 이름:  ")
    for onemem in memlist:
        if ser_name in onemem:
            print("%s %s %d" % (ser_name, onemem[1], onemem[2]))
            break

def memberModify(memlist):
    ser_name = input("찾고하고 싶은 이름:  ")
    for onemem in memlist:
        if ser_name in onemem:
            print("%s %s %d" % (ser_name, onemem[1], onemem[2]))
            break
    print("-> %s, 이메일만 변경가능함" % onemem[1])
    onemem[1] = input("이메일 수정: ")
    print("변경 되었음.")

def main() :
    memlist = []

    while True:
        screen()
        choice = input("-> ")

        if choice == "0":
            print()
            memlist = createNodeInit(memlist)
        elif choice == "1":
            print()
            memlist = memberAdd(memlist)
        elif choice == "2":
            print()
            memberAllList(memlist)
        elif choice == "3":
            print()
            memberSearch(memlist)
        elif choice == "4":
            print()
            memberModify(memlist)
        elif choice == "5" :
            os.system("cls")
        elif choice == "6":
            sys.exit(1)
            break
        else:
            print("잘못된 번호! 다시 입력바랍니다.")

main()