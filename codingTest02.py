def solution():
    # 배열 크기를 입력받는다.
    N = int(input("배열 크기 >> "))

    # 배열에 점수를 입력받아 저장한다.
    datas = []
    print("점수 >> ", end="")
    for _ in range(N):
        number = int(input())
        datas.append(number)

    # 합을 구한다.
    sum_value = sum(datas)
    print(f"sum : {sum_value}")

    # 평균을 구한다.
    avg = sum_value / N
    print(f"avg : {avg}")

    # 배열의 원소를 출력한다.
    for num in datas:
        print(num, end=" ")

# 함수 호출
solution()
