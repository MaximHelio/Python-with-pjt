# 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈
import socket

# 방법 1. 연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩
# 여러 개의 가상환경이 있을 경우 다른 환경의 ip가 출력되어 정확한 IP 출력이 어려울 수 있음 =
in_addr = socket.gethostbyname(socket.gethostname())

# in_addr을 출력하여 내부 IP확인
print(in_addr)
