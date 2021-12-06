def gcd(x,y):
    # x가 0이 될 때까지 반복
    while x:
        # x를 y에 대입
        # y를 x%y에 대입
        x, y = y%x, x
    return y
    '''
    1. 1071은 1029로 딱 나눠지지 않기 때문에 1071을 1029로 나눈 나머지를 구함 -> 42
    2. 1029는 42로 딱 나눠지지 않기 때문에 1029를 42로 나눈 나머지를 구함 -> 21
    3. 42는 21로 나눠짐
    4. 최대공약수는 21
    '''

    # 앞의 몫은 이미 0으로 나눠진 것이므로 필요없고 뒤에 나머지만 보는 거임
    # 유클리드 호제법이 코테에 나올 확률은 적으므로 그냥 무조건 외우는 게 나을듯
T = int(input())
for i in range(T):
    A, B = list(map(int, input().split()))
    print(A*B//gcd(A,B))
    
