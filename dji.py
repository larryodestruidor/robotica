from djitellopy import Tello
from time import sleep
TEMPO_ESPERA=0
percurso = []
tello = Tello()
tello.connect()

x = 0
y = 0
h_i = 0
h_a = 0

def p_bat():
    b = tello.get_battery()
    print("Battery:", b, "%")
    return b

def a_i():
    global alt_i
    alt_i = tello.get_distance_tof()
    print(alt_i)

def a_a():
    global alt_a
    alt_a = tello.get_distance_tof()
    print(alt_a)

def m_f_i():
    global y
    tello.move_forward(100)
    y += 100

def m_f_p():
    global y
    tello.move_forward(100)
    y -= 100

def abc():
    tello.move_forward(100)
    global x
    x += 100

def am_alt():
    tello.move_up(30)

def r_d():
    tello.rotate_clockwise(90)

def r_e():
    tello.rotate_counter_clockwise(90)

battery = p_bat()

if battery < 100:
    print("Bateria com menos de 100%, troque imediatamente.")
else:
    p_bat()


tello.takeoff()
am_alt()
a_i()


for j in range(1, 7):
    if j % 2 != 0:
        for i in range(1, 4):
            m_f_i()
            a_a()
            sleep(TEMPO_ESPERA)
            if abs(alt_a - alt_i) > 20:
                print(x,",", y,"; cm")
            else:
                continue
        sleep(TEMPO_ESPERA)
        r_d()
        sleep(TEMPO_ESPERA)
        abc()
        sleep(TEMPO_ESPERA)
        r_d()
    else:
        for i in range(1, 4):
            m_f_p()
            a_a()
            sleep(TEMPO_ESPERA)
            if abs(alt_a - alt_i) > 20:
                print(x,",", y,"; cm")
            else:
                continue
        sleep(TEMPO_ESPERA)
        r_e()
        sleep(TEMPO_ESPERA)
        abc()
        sleep(TEMPO_ESPERA)
        r_e()

tello.land()
   
   
   
   
   
            
"""
# hover para foto
time.sleep(3)
frame_read = tello.get_frame_read()
#print("Pressiona 's' para tirar uma foto ou 'q' para aterrar.")


tello.land()
#tello.streamoff()


photo_count = 0

while True:
    frame = frame_read.frame
    if frame is not None:
        cv2.imshow("Tello vídeo feed", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        filename = f"tello_photo_{photo_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"✅ Saved {filename}")
        photo_count += 1

    elif key == ord('q'):
        print("Landing...")
        tello.land()
        tello.streamoff()
        exit()

"""
