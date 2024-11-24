def solution():
    # 정수를 입력받는다.
    number = int(input("정수 >> "))

    # 정수를 문자열로 변경한다.
    number_str = str(number)

    # 문자열의 각 자리에 해당하는 숫자를 리스트에 저장
    digits = [int(char) for char in number_str]

    # 3, 6, 9가 있는지 확인하고 그 개수를 셈
    result = 0
    for digit in digits:
        if digit == 3 or digit == 6 or digit == 9:
            result += 1

    print(f"result : {result}")

    # 배열을 출력하면 입력한 정수가 하나씩 보여진다.
    for digit in digits:
        print(digit, end=" ")

# 함수 호출
solution()
