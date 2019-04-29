import socket
import time
import math

# User and Game Server Information
NICKNAME = '파이썬'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def my(a, b, c, white, hole, ball):




    # 계산
    power = a/2 + 19

    key = (hole[1] - white[1]) / (hole[0] - white[0]) # 흰공하고 홀

    if (hole[1] > white[1]) and (hole[0] > white[0]):
        COSC = -((c ** 2 - a ** 2 - b ** 2) / (2 * a * b))
        x = abs(hole[0] - white[0])
        y = abs(hole[1] - white[1])
        C = math.acos(COSC)

        d = ((a * math.sin(C)) ** 2 + (a * COSC - (b + 15)) ** 2) ** (1 / 2)

        C2 = math.acos(-((b + 15) ** 2 - a ** 2 - d ** 2) / (2 * a * d))

        C1 = math.atan(y/x)
        print(1)
        if key < (ball[1] - white[1]) / (ball[0] - white[0]):
            result = abs(C1-C2)*(180/math.pi)
        else:
            result = (C1+C2) * (180 / math.pi)

    elif (hole[1] < white[1]) and (hole[0] > white[0]):
        hole[1] = hole[1]+(white[1]-hole[1])*2
        if ball[1]<white[1]:
            ball[1] = ball[1]+(white[1]-ball[1])*2
        else:
            ball[1] = ball[1] - abs(white[1] - ball[1]) * 2
        x = abs(hole[0] - white[0])
        y = abs(hole[1] - white[1])
        COSC = -((c ** 2 - a ** 2 - b ** 2) / (2 * a * b))

        C = math.acos(COSC)

        d = ((a * math.sin(C)) ** 2 + (a * COSC - (b + 15)) ** 2) ** (1 / 2)

        C2 = math.acos(-((b + 15) ** 2 - a ** 2 - d ** 2) / (2 * a * d))

        C1 = math.atan(y/x)
        print(2)
        if key < (ball[1] - white[1]) / (ball[0] - white[0]):
            result = 90 + (abs(C1 - C2) * (180 / math.pi))
        else:
            result = 90 + (C1+C2)*(180/math.pi)

    elif (hole[1] < white[1]) and (hole[0] < white[0]):
        print(3)
        hole[1] += (white[1]-hole[1])*2
        hole[0] += (white[0]-hole[0])*2
        if ball[1] < white[1]:
            ball[1] = ball[1]+(white[1]-ball[1])*2
        else:
            ball[1] = ball[1] - abs(white[1] - ball[1]) * 2
        if ball[0] < white[0]:
            ball[0] += (white[0]-ball[0])*2
        else:
            ball[0] -= abs(white[0] - ball[0]) * 2
        x = abs(hole[0] - white[0])
        y = abs(hole[1] - white[1])
        COSC = -((c ** 2 - a ** 2 - b ** 2) / (2 * a * b))

        C = math.acos(COSC)

        d = ((a * math.sin(C)) ** 2 + (a * COSC - (b + 15)) ** 2) ** (1 / 2)

        C2 = math.acos(-((b + 15) ** 2 - a ** 2 - d ** 2) / (2 * a * d))

        C1 = math.atan(y/x)
        if key < (ball[1] - white[1]) / (ball[0] - white[0]):
            result = 180 + abs(C1 - C2) * (180 / math.pi)
        else:
            result = 180 + (C1 + C2)*(180/math.pi)

    elif (hole[1] > white[1]) and (hole[0] < white[0]):
        print(4)
        hole[0] += (white[0] - hole[0]) * 2
        if ball[0] < white[0]:
            ball[0] += (white[0] - ball[0]) * 2
        else:
            ball[0] -= abs(white[0] - ball[0]) * 2
        x = abs(hole[0] - white[0])
        y = abs(hole[1] - white[1])
        COSC = -((c ** 2 - a ** 2 - b ** 2) / (2 * a * b))

        C = math.acos(COSC)

        d = ((a * math.sin(C)) ** 2 + (a * COSC - (b + 15)) ** 2) ** (1 / 2)

        C2 = math.acos(-((b + 15) ** 2 - a ** 2 - d ** 2) / (2 * a * d))

        C1 = math.atan(y/x)
        if key < (ball[1] - white[1]) / (ball[0] - white[0]):
            result = 270 + abs(C1 - C2) * (180 / math.pi)
        else:
            result = 270 + (C1 + C2)*(180/math.pi)

    else:
        return (30, 300)
    return (result, power)

def play(conn, gameData):
    # angle=0


    balls = gameData.balls
    ball = balls[1]
    for i in range(1, 5):
        if balls[i][0] or balls[i][1]:
            ball = balls[i]
            break

    HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]
    MIN = 0xfffffff
    for i in range(len(HOLES)):
        a = ((HOLES[i][0] - balls[0][0]) ** 2 + (HOLES[i][1] - balls[0][1]) ** 2) ** (1 / 2)
        b = ((HOLES[i][0] - ball[0]) ** 2 + (HOLES[i][1] - ball[1]) ** 2) ** (1 / 2)
        c = ((ball[0] - balls[0][0]) ** 2 + (ball[1] - balls[0][1]) ** 2) ** (1 / 2)
        if (HOLES[i][0]-ball[0])**2+(HOLES[i][1]-ball[1])**2 < MIN and (a**2 > b**2 + c**2):
            # if a**2 < b**2+c**2:

            MIN = (HOLES[i][0]-ball[0])**2+(HOLES[i][1]-ball[1])**2
            idx = i


    a = ((HOLES[idx][0] - balls[0][0]) ** 2 + (HOLES[idx][1] - balls[0][1]) ** 2) ** (1 / 2)
    b = ((HOLES[idx][0] - ball[0]) ** 2 + (HOLES[idx][1] - ball[1]) ** 2) ** (1 / 2)
    c = ((ball[0] - balls[0][0]) ** 2 + (ball[1] - balls[0][1]) ** 2) ** (1 / 2)
    angle, power = my(a, b, c, balls[0], HOLES[idx], ball)




    print(angle)
    ######################################################################################
    # 주어진 정보를 바탕으로 샷을 할 방향과 세기를 결정해서 angle, power 값으로 지정 #
    ######################################################################################
    conn.send(angle, power)




def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        play(conn, gameData)        
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
