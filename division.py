import main

def divide(number1: float, number2: float) -> float:
	if number2 == 0:
		print("0으로 나눌 수 없습니다.")
		return 0
	return number1 / number2
