def plus(num1:int, num2:int):
    print(num1 + num2)

if __name__ == '__main__':
    while True:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        operator = input("연산자를 입력하세요 (+, -, *, /): ")
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        if operator == "+":
            plus(num1, num2)
        elif operator == "-":
            plus(num1, num2)
            # 강님 함수 호출
        elif operator == "*":
            plus(num1, num2)
            # 다빈님 함수 호출
        elif operator == "/":
            plus(num1, num2)
            # 진우님 함수 호출
        else:
            print("잘못된 연산자입니다. 다시 입력해주세요.")
            continue
        
        choice = input("계속 하시겠습니까? (Y/N): ")
        if choice == "N":
            break
  