import serial
import time
import sys

class serial_Monitor():

	def __init__(self, address, baud_rate=9600, timeout=2, python3=False):
		self.ser = None
		self.last_line = ""
		# serial information
		self.address = address
		self.baud_rate = baud_rate
		self.timeout = timeout
		# flag 
		self.data_check = 0
		self.python3 = python3


	def init_connection(self):
		print ("Start Serial Connection")
		try:
			ser = serial.Serial(self.address, self.baud_rate, timeout=self.timeout)
		except:
			print ("Wrong serial address and shut donw system")
			sys.exit()

		self.ser = ser
		# sleep 500ms before accepting data
		time.sleep(0.1)
		self.ser.flushInput()


	def close_connection(self):
		print ("Close Serial Connection")
		self.ser.close()


	def is_ready(self, bytes_expected):
		return self.ser.in_waiting >= bytes_expected


	def collect_data(self):
		if self.data_check:
		#if self.ser.in_waiting>0:
			# read all new bytes
			bytesToRead = self.ser.in_waiting
			if bytesToRead>0:
				ser_bytes = self.ser.read(bytesToRead)
				# convert byte to string python 3
				if self.python3:
					ser_bytes = ser_bytes.decode("utf-8")
				return ser_bytes
		else:
			# discard the first corrupted line
			self.ser.reset_input_buffer()
			self.ser.readline()
			self.data_check = 1
			#print("nada")



