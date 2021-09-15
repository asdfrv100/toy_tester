from flask import Flask, render_template
import threading
import keyboard
import time
app = Flask(__name__)
num_of_room=8
meetting_room=num_of_room*[0]
auditorium = 0
before_input=''
#auditorium은 meeting room8
def count_up(x):
    return x+1

def presscheck():
    pressed_flag = [0] * len(meetting_room)
    # while True:
    #     try :
    #         if (keyboard.is_pressed('a')):
    #             pressed_flag[0]=1
    #
    #         elif (keyboard.is_pressed('b')):
    #             pressed_flag[1]=1
    #
    #         elif(keyboard.is_pressed('p')):
    #             print('mt1_number_up')
    #             for i in range(0,[0]*len(meetting_room)):
    #                 if(pressed_flag[i]==1):
    #                      meetting_room[i]+=1
    #             pressed_flag=[0]*len(meetting_room)
    #         else:
    #             pass
    #
    #     except:
    #         print('notworking')
    while True:
        if (keyboard.is_pressed('1')):
             pressed_flag[0] = 1
        elif (keyboard.is_pressed('2')):
             pressed_flag[1] = 1
        elif (keyboard.is_pressed('3')):
             pressed_flag[2] = 1
        elif (keyboard.is_pressed('4')):
             pressed_flag[3] = 1
        elif (keyboard.is_pressed('5')):
             pressed_flag[4] = 1
        elif (keyboard.is_pressed('6')):
             pressed_flag[5] = 1
        elif (keyboard.is_pressed('7')):
             pressed_flag[6] = 1
        elif (keyboard.is_pressed('8')):
             pressed_flag[7] = 1

        #people num count up
        elif (keyboard.is_pressed('p')):
            for i in range(0, len(meetting_room)):
                if (pressed_flag[i] == 1):
                     meetting_room[i] += 1
                     print('mt1_number_up')
            pressed_flag = [0] * len(meetting_room)

        #people num count down
        elif (keyboard.is_pressed('q')):
            for i in range(0, len(meetting_room)):
                if ((pressed_flag[i] == 1) and (meetting_room[i]>0)):
                     meetting_room[i] -= 1
                     print('mt1_number_down')
            pressed_flag = [0] * len(meetting_room)

        else:
            pass


t = threading.Thread(target=presscheck, args=())
t.start()


@app.route("/")
def home():
    return render_template('poscocenter.html'
                           ,meeting_room_1=str(meetting_room[0])
                           ,meeting_room_2=str(meetting_room[1])
                           ,meeting_room_3=str(meetting_room[2])
                           ,meeting_room_4=str(meetting_room[3])
                           ,meeting_room_5=str(meetting_room[4])
                           ,meeting_room_6=str(meetting_room[5])
                           ,meeting_room_7=str(meetting_room[6])
                           ,auditorium=str(meetting_room[7]))

    # return render_template('poscocenter.html'
    #                        ,data={
    #                        "meeting_room_1":str(meetting_room[0]),
    #                        "meeting_room_2":str(meetting_room[1]),
    #                        "meeting_room_3":str(meetting_room[2]),
    #                        "meeting_room_4":str(meetting_room[3]),
    #                        "meeting_room_5":str(meetting_room[4]),
    #                        "meeting_room_6":str(meetting_room[5]),
    #                        "meeting_room_7":str(meetting_room[6]),
    #                        "auditorium": str(auditorium)})




if __name__ == "__main__":
    app.run()



#210913 16:42
# from flask import Flask, render_template
# import threading
# import keyboard
# import time
# app = Flask(__name__)
#
# meetting_room=[1,2,3]
#
# def count_up(x):
#     return x+1
#
# def presscheck():
#     while True:
#         try :
#             if keyboard.is_pressed('a'):
#                 print('mt1_number_up')
#                 meetting_room[0]+=1
#             else:
#                 pass
#
#         except:
#             print('notworking')
#
#
# t = threading.Thread(target=presscheck, args=())
# t.start()
#
#
# @app.route("/")
# def home():
#     return render_template('poscocenter.html', meeting_room=str(meetting_room[0]))
#
#
#
#
# if __name__ == "__main__":
#     app.run()