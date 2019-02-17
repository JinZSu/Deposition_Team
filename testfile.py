class deposition:
	def __init__(self):
		self.vibration = False
		# position z is when storage is ready to deposit gravel
		self.pos_z = 45
		# position x is when we deposit to the bin
		self.pos_x = 55
		# position y is the lowest bin position
		self.pos_y = 0
		self.curr_pos = 0
		self.weight = 50
		# when rack is false, it is at original position
		self.rack = False

	def actuator(self, target_pos):
		diff = self.curr_target - target_pos
		if diff >=  0:
			print "Actuator going up"
		else:
			print "Actuator going down"

	def vibration(self):
		if self.vibration:
			print "Turning off vibration"
			self.vibration = False
		else:
			print "Turning on vibration"
			self.vibration = True

	def deposition(self, purpose):
		if purpose == "collect":
			self.actuator(self.pos_z)
			self.vibration()
		elif purpose == "deposit":
			self.actuator(self.pos_x)
			self.push()
		self.actuator.pos_y()

	def push(self):
		print "Rack and pinion pushing"

	
	
		
		 
		
    		
