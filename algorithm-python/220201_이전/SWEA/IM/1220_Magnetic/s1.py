import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 1은 N의 성질, 2는 S의 성질


    # 테이블 위에 존재하는 이동 가능한 모든 요소의 수를 카운팅 => 변수
    # 이동 가능한 존재가 없을 때까지 반복 => 1혹은 2가 있는 동안 반복
    # 1은 아래로, 2는 위로 => 이차원 리스트 상 인덱스로 보았을 때 1씩 증가, 1씩 감소한다.
    # -1, 1

    # 전수 조사 시작
    # 모든 요소들을 검사하는 중에
    # 1을 만났다.
        # N극 자성체 -> 아래로만 이동
            # 1. 벽 체크 -> 벽을 벗어나면 사라짐 -> 현재 위치 값 0으로 바뀜
                # 1-1. 사라짐 -> 움직일 수 있는 개체수 -1
            # 2. S극 만남...체크 -> s극과 n극이 만나면 교착상태 -> 둘 다 3으로 바꾸면 다음 조사때 신경쓰지 않는다. (교착 개수 +1)
                # 나와 내 아래가 모두 움직일 수 없게 됨 , 개체수 -2
            # 3. 이미 교착상태 만남... -> 나만 3으로 변경하여 교착상태로 만들어둠(교착 개수 유지)
                # 3-1. 나만 교착상태 -> 움직일 수 있는 개체수 -1

            # 아직 움직일 수 있는 개체수 유지
            # 4. N극 만남 -> 대기
            # 5. 아무것도 아니면 -> 한 칸 아래로 이동
    # 2를 만났다.
        # 위로만 이동



