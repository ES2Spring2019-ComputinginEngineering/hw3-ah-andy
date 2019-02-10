import microbit
import math

def xangle(accel_z, accel_x):
    angle_x = math.atan2(accel_x, accel_z)
    return (math.degrees(angle_x))

def yangle(accel_z, accel_y):
    angle_y = math.atan2(accel_y, accel_z)
    return (math.degrees(angle_y))

while True:
    microbit.sleep(50)
    accel_x = microbit.accelerometer.get_x()
    accel_y = microbit.accelerometer.get_y()
    accel_z = microbit.accelerometer.get_z()



    Xangle = xangle(accel_z, accel_x)
    Yangle = yangle(accel_z, accel_y)


    if 185 > Xangle > 175 and 185 > Yangle > 175:
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "00900:"
                                             "00000:"
                                             "00000:"))

    elif 175 >= Xangle > 145 and 175 >= Yangle > 145:
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "00000:"
                                             "00090:"
                                             "00000:"))

    elif 175 >= Xangle > 145 and (-175) <= Yangle < (-145):
        microbit.display.show(microbit.Image("00000:"
                                             "00090:"
                                             "00000:"
                                             "00000:"
                                             "00000:"))

    elif (-175) <= Xangle < (-145) and 175 >= Yangle > 145:
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "00000:"
                                             "09000:"
                                             "00000:"))

    elif (-175) <= Xangle < (-145) and (-175) <= Yangle < (-145):
        microbit.display.show(microbit.Image("00000:"
                                             "09000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"))
    elif (185) >= Xangle >= (175) and (-175) <= Yangle < (-145):
        microbit.display.show(microbit.Image("00000:"
                                             "00900:"
                                             "00000:"
                                             "00000:"
                                             "00000:"))
    elif (175) >= Xangle >= (145) and (-175) > Yangle > (-185):
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "00090:"
                                             "00000:"
                                             "00000:"))
    elif (185) >= Xangle >= (175) and (175) > Yangle > (145):
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "00000:"
                                             "00900:"
                                             "00000:"))
    elif (-145) >= Xangle >= (-185) and (185) > Yangle > (175):
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "09000:"
                                             "00000:"
                                             "00000:"))
    elif (-90) >= Xangle >= (-145) and (185) > Yangle > (175):
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "90000:"
                                             "00000:"
                                             "00000:"))
    elif (185) >= Xangle >= (175) and (145) > Yangle > (90):
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"
                                             "00900:"))
    elif (145) >= Xangle >= (90) and (-175) > Yangle > (-185):
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "00009:"
                                             "00000:"
                                             "00000:"))
    elif (185) >= Xangle >= (175) and (-145) <= Yangle < (-90):
        microbit.display.show(microbit.Image("00900:"
                                             "00000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"))
    elif (-145) <= Xangle < (-90) and (-145) <= Yangle < (-90):
        microbit.display.show(microbit.Image("90000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"))
    elif (-145) <= Xangle < (-90) and 145 >= Yangle > 90:
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"
                                             "90000:"))
    elif 145 >= Xangle > 90 and 145 >= Yangle > 90:
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"
                                             "00009:"))
    elif 145 >= Xangle > 90 and (-145) <= Yangle < (-90):
        microbit.display.show(microbit.Image("00009:"
                                             "00000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"))
    elif 145 >= Xangle > 90 and (-175) <= Yangle < (-135):
        microbit.display.show(microbit.Image("00000:"
                                             "00009:"
                                             "00000:"
                                             "00000:"
                                             "00000:"))
    elif 145 >= Xangle > 90 and 175 >= Yangle > 145:
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "00000:"
                                             "00009:"
                                             "00000:"))
    elif (-145) <= Xangle < (-90) and 175 >= Yangle > 145:
        microbit.display.show(microbit.Image("00000:"
                                             "00000:"
                                             "00000:"
                                             "90000:"
                                             "00000:"))
    elif (-145) <= Xangle < (-90) and (-175) <= Yangle < (-145):
        microbit.display.show(microbit.Image("00000:"
                                             "90000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"))
    elif 175 >= Xangle > 145 and (-145) <= Yangle < (-90):
        microbit.display.show(microbit.Image("00090:"
                                             "00000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"))
    elif (-175) <= Xangle < (-145) and (-145) <= Yangle < (-90):
        microbit.display.show(microbit.Image("09000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"
                                             "00000:"))

