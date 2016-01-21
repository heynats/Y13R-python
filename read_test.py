import time
import serial
          
ser = serial.Serial(
          port='/dev/ttyUSB0',
          baudrate = 9600,
          parity=serial.PARITY_NONE,
          stopbits=serial.STOPBITS_ONE,
          bytesize=serial.EIGHTBITS,
          timeout=3
          )
          
# Terminate test with Ctrl-C
def end_read(signal,frame):
    global do_test
    print "Ctrl+C captured, ending test."
    do_test = False

# Hook SIGINT
signal.signal(signal.SIGINT, end_read)

while do_test:
  reader_response = ser.readline()
  if reader_response != ""
          hex_msg = " ".join("{:02x}".format(ord(c)) for c in reader_response)
          print hex_msg
