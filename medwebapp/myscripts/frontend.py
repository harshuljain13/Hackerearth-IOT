import serial
import functions
import json
import requests
import time

global json_dict


def main():
    #ser = serial.Serial('COM4',9600)
    #memid = raw_input('enter your ID')
    memid = 'random1'
    ser = open('2.txt', 'r', 1)
    time1 = float(0)
    count = 0

    json_dict = {}
    y = []
    yn = []
    ref = []
    Fs = 62.5
    n = 1
    red_max = 0
    ir_max = 0
    red_min = 850
    ir_min = 850
    countw=1
    for line in ser:
        ##while True:
        time1 = count / Fs
        if time1 < 5:
            ##sensor=ser.readline()
            ##if sensor is '':
            ##    break
            a23 = line.split(' ')
            if len(a23) != 2:
                continue
            analog_red = int(a23[0])
            analog_ir = int(a23[1])

            if 100 < analog_red < 765 and 100 < analog_ir < 765:
                ref.append(analog_ir - analog_red)
                y.append(analog_red)
                yn.append(analog_ir)
                count += 1

            if analog_red > red_max:
                red_max = analog_red
            elif analog_red < red_min:
                red_min = analog_red

            if analog_ir > ir_max:
                ir_max = analog_ir
            elif analog_ir < ir_min:
                ir_min = analog_ir

        else:
            print '\n\n\n After.............. ', 2 * n, 'sec................\n\n'

            count = 0
            hr, rr = functions.estimate(y, yn, ref)
            hb = functions.hemoglobin(red_max, ir_max)

    #..........................................JSON...........................................................

            json_dict = {
                        'klopid':memid,
                        'heart_rate': int(hr),
                        'resp_rate': int(rr)
            }
            json_string_ser = json.dumps(json_dict)
            headers = {'content-type': 'application/json'}
            if countw == 1:
                r = requests.post('http://127.0.0.1:8000/klop/detail/random1/', data=json_string_ser, headers=headers)
                if r.status_code !=200:
                    d = requests.delete('http://127.0.0.1:8000/klop/detail/random1/')
                    r = requests.post('http://127.0.0.1:8000/klop/detail/random1/', data=json_string_ser,
                                      headers=headers)
                countw+=1
    #..........................................Resetiing storage..................................................................
            red_max = 0
            ir_max = 0
            red_min = 850
            ir_min = 850
            y = []
            yn = []
            ref = []
            n += 1

if __name__ == '__main__':
    main()

