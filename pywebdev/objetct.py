class Program():
        
	def __init__ (self, *args, **kwargs):
                
		self.lang = input("What language?: ")
		self.version = float(input("What version?: "))
		self.skill = input("What skill level?: ")

	
	def upgrade (self):
		new_version = float(input("What version?: "))
		self.version = new_version

		print ("We have updated the version for", self.lang,", to", self.version)


p1 = Program()


