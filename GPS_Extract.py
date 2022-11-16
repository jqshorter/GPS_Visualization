import io
import pynmea2
import serial

ser = serial.Serial('COM3', 115200, timeout=5.0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))


def coordinate_conversion(lat, long):
    lens = [2, 7]
    res = []
    st = 0
    for size in lens:
        # slicing for particular length
        res.append(lat[st: st + size])
        st += size

    lat_final = float(res[0]) + float(res[1]) / 60

    lens = [3, 8]
    res = []
    st = 0
    for size in lens:
        # slicing for particular length
        res.append(long[st: st + size])
        st += size

    long_final = (float(res[0]) + (float(res[1]) / 60)) * -1
    return tuple([lat_final, long_final])


def data_return():
    while 1:
        try:
            line = sio.readline()
            line = line.split(",")
            if line[0] == "$GPRMC":
                coord = coordinate_conversion(line[3], line[5])
                return coord
        except serial.SerialException as e:
            print('Device error: {}'.format(e))
            break
        except pynmea2.ParseError as e:
            print('Parse error: {}'.format(e))
            continue

