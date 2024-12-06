#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import UARTDevice
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# #==========[Initialize]==========
# #==========[sensors]==========
# ev3 = EV3Brick()
# gyro = GyroSensor(Port.S1)
# ser = UARTDevice(Port.S2, baudrate=115200)

# #==========[motors]==========
# grab_motor = Motor(Port.B)
# shooting_motor = Motor(Port.C)

# left_motor = Motor(Port.A)
# right_motor = Motor(Port.D)
# robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=115)

# #==========[target_angle turn(gyro)]==========
# def turn(target_angle, power):
    
#     # left_motor.run(power)
#     # right_motor.run(-power)
#     # while True:
#     #     angle=gyro.angle()
        
#     #     if abs(angle)>target_angle-2:
#     #         left_motor.stop()
#     #         right_motor.stop()
#     #         break
#     # robot.turn()
#     print('robot turn')
#     robot.drive(power, power)
#     while True:
#         angle = gyro.angle()
#         print(angle)
#         if abs(angle)>target_angle-2:
#             robot.stop()
#             break

# #==========[camera_chase]==========
# def process_uart_data(data):
#     try:
#         # 데이터를 문자열로 디코드 (키워드 인자 제거)
#         data_str = data.decode().strip()
#         if not data_str:
#             pass

#         # 문자열에서 리스트 파싱
#         data_str = data_str.strip("[]")
#         parsed_list = [int(value.strip()) for value in data_str.split(",")]

#         # 파싱된 결과 반환
#         return parsed_list
#     except:
#         # 에러 처리
#         return [-1,-1] # -1이 나오면 무시하는 코드 사용

# def pd_control(cam_data, kp, kd, power):
#     global previous_error
#     error = cam_data - threshold
#     derivative = error - previous_error
#     output = (kp * error) + (kd * derivative)
#     robot.drive(power, output)
#     previous_error = error

# #==========[shooting positions]==========
# def grab(command):
#     if command == 'motion3':
#         #close
#         grab_motor.run_until_stalled(100,Stop.COAST,duty_limit=50)
#         #set_zero point
#         grab_motor.reset_angle(0)
#     elif command == 'motion1':
#         #open1
#         grab_motor.run_until_stalled(-100,Stop.COAST,duty_limit=50)
#     elif command == 'motion2':
#         #open2
#         grab_motor.run_target(100,-100)

# def shoot(command):
#     if command == 'zero':
#         #zero_position
#         shooting_motor.run_until_stalled(-100,Stop.COAST,duty_limit=50)
#     elif command == 'shoot':
#         #shooting
#         shooting_motor.run(1750)
#         time.sleep(0.25)
#         shooting_motor.stop()



#==========[setup]==========
# ev3.speaker.beep()
# threshold = 80
# previous_error = 0
# gyro.reset_angle(0)
# #==========[zero set position setting]==========
# shoot('zero') #shoot 모터가 안쪽이고,
# grab('motion3') #grab 모터가 바깥쪽이므로 shoot먼저 세팅 후 grab을 세팅해야한다
# time.sleep(1)
# grab('motion1') #공을 잡기 위한 높이로 열기

# print("Zero set postion completed")

# #==========[main loop]==========
# while True:
#     data = ser.read_all()
#     # 데이터 처리 및 결과 필터링
#     try:
#         filter_result = process_uart_data(data)
#         #filter_result[0] : x, filter_result[1] : y
#         if filter_result[0]!= -1 and filter_result[1]!= -1:
#         # if filter_result[0]!= -1 and filter_result[1]!= -1:
#             if filter_result[1] > 90: #공이 카메라 화면 기준으로 아래에 위치 = 로봇에 가까워졌다
#                 robot.straight(100) #강제로 앞으로 이동
#                 grab('motion3') #공을 잡기
#                 time.sleep(1) #동작간 딜레이
#                 turn(0,100) #정면(상대방 진영)바라보기
#                 time.sleep(1) #동작간 딜레이
#                 grab('motion1') #슛을 위한 열기
#                 time.sleep(0.5) #동작간 딜레이
#                 shoot('shoot') #공 날리기
#                 time.sleep(0.5) #동작간 딜레이
#                 shoot('zero')
#                 grab('motion2') 
#             else: #공이 카메라 화면 기준 멀리 위치해 있으면 chase한다
#                 pd_control(filter_result[0], kp=0.5, kd=0.1, power=100)
#         # else: # 센서가 공을 보지 못했을 경우의 움직임.
#         #     robot.straight(50)
#         #     robot.turn(10)

#         time.sleep_ms(50)
#     except:
#         pass

# while True:
#     try:
#         data = ser.read_all()
#         filter_result = process_uart_data(data)
#         if filter_result[0]!= -1 and filter_result[1]!= -1:
#             print(filter_result)
#             pd_control(filter_result[0], kp=0.5, kd=0.1, power=100)
#         wait(10)
#     except:
#         pass
        

#!/usr/bin/env python3
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import time

# 11111 
# run_motor = Motor(Port.A)

# run_motor.run_time(30)
# wait(1000)
# run_motor.run_time(-30)
# wait(1000)



# run_motor.reset_angle(0)
# run_motor.run(100)

# if <720



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
# 맨 윗줄 주석 아니니 지우면 안됨. 지우면 실행이 되지 않음.

# Create your objects here.
# ev3 = EV3Brick()

# class Motor(port,positive_direction = Direction.CLOCKWISE,gears = NONE)

# run_motor = Motor(Port.A)
# ev3.run_motor(Port.A)

# run_motor.run(200)


# ts = TouchSensor(Port.S1)

# while True:
#     if ts.pressed():
#         while ts.pressed():
#             pass
#     print("터치센서 눌림")

# ev3 = EV3Brick()

# # ts = TouchSensor(Port.S1)
# # while True:
# #     if ts.pressed():
# #         while ts.pressed():
# #             pass
# #     ev3.speaker.beep()


# ultra = UltrasonicSensor(Port.S3)

# distance = ultra.distance()
# print(distance)

# presence = ultra.presence()
# print(presence)


# ev3 = EV3Brick()
# ev3.speaker.beep()

# left_motor = Motor(Port.A)
# right_motor = Motor(Port.D)

# wheel_diameter = 5.6
# axle_track = 115

# robot = DriveBase(left_motor,right_motor,wheel_diameter,axle_track)

# shooting_motor = Motor(Port.C)
# grab_motor = Motor(Port.B)

# grab_motor.run_until_stalled(500, stop_type=Stop.HOLD, duty_limit=75) 
# grab_motor.reset_angle()  # 현재 각도를 기준으로 0으로 초기화

# robot.straight(100)

# grab_motor.run_target(speed=500, target_angle=-90, wait=True)  

# robot.straight(-50)

# robot.turn(90)

# shooting_motor.run(1000)  # 빠르게 모터 회전
# wait(500)                # 0.5초 동안 동작
# shooting_motor.stop()    # 모터 정지

wheel_diameter = 5.6
axle_track = 115

ev3 = EV3Brick()

#ultra = UltrasonicSensor(Port.S2)
color_sensor = ColorSensor(Port.S2)

shooting_motor_one = Motor(Port.C)
shooting_motor_two = Motor(Port.B)

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
robot = DriveBase(left_motor,right_motor,wheel_diameter,axle_track)
ev3.speaker.beep()



# 속도 50mm/s에서 25mm/s로 줄이고 시간 조정
# rgb = color_sensor.rgb()
# print(rgb)
# robot.drive_time(-100, 0, abs(65 / 25 * 1000))  # 후진 300mm
# shooting_motor.run_until_stalled(1000,Stop.COAST,duty_limit=100)
# time.sleep(1)
# shooting_motor.run_until_stalled(-1000,Stop.COAST,duty_limit=100)
# robot.drive_time(100, 0, abs(55 / 25 * 1000))  # 전진 200mm


shooting_motor_one.run_target(1000, -360)  # 첫 번째 모터 실행


robot.drive_time(100, 0, abs(55 / 25 * 1000))  # 전진 200mm

shooting_motor_one.run_target(1000, 360)
time.sleep(1)
shooting_motor_one.run_target(1000, -360)  # 첫 번째 모터 실행
robot.drive_time(-100, 0, abs(65 / 25 * 1000))  # 후진 300mm

time.sleep(1)


# shooting_motor_one.run_target(1000, -360, wait=False)  # 첫 번째 모터 실행



def move_shooting_arm(angle,speed):
    shooting_motor.run_target(speed,angle)

def shoot_with_power():
    shooting_motor.run_until_stalled(-1000,Stop.COAST,duty_limit=100)

def move_backward_until_blue(speed): # 후진속도 음수값
    robot.drive(speed, 0)  # 후진 시작
    while True:
        if color_sensor.color() == Color.BLUE:  # 파란색 감지
            robot.stop()  # 멈춤
            print("파란색 감지! 로봇 멈춤")
            break
        time.sleep(0.01)  # 센서를 주기적으로 확인
# 일정 거리만큼 전진하는 함수
def move_forward_by_distance(distance, speed):
    """
    로봇을 특정 거리만큼 전진(또는 후진)시킴.

    :param distance: 전진할 거리 (양수: 전진, 음수: 후진), 단위: mm
    :param speed: 전진 속도 (단위: mm/s)
    """
    robot.reset()  # 이전 이동 기록 초기화
    robot.drive_time(speed, 0, abs(distance / speed * 1000))  # 거리 계산 기반 이동
    robot.stop()

# # ==================== main ===========================

# while True:

#     move_shooting_arm(60,200)
#     time.sleep(0.5)

#     move_shooting_arm(-60,200)
#     time.sleep(0.5)

#     move_backward_until_blue(-100)

#     shoot_with_power()
#     time.sleep(0.5)

#     move_shooting_arm(60,200)
#     time.sleep(0.5)

#     move_forward_until_wall(100,threshold_distance=200)



