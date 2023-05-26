# 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈
import socket

# 방법 2. socket으로 외부 사이트에 접속하고, 접속된 정보를 바탕으로 IP확인 => 좀더 정확
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# https의 기본 접속포트는 443
# 카페 등에서 와이파이를 사용할 경우,
# socket.gaierror: [Errno 11001] getaddrinfo faile 에러가 발생할 수 있는데, 이는 NDS / 네트워크 혼잡/ 네트워크 연결 문제 때문일 수 있음
in_addr.connect(("wwww.naver.com", 443))

# 연결된 소켓의 이름 출력
print(in_addr.getsockname()[0])
