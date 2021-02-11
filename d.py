class Robot:

    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year            
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name    

    def set_build_year(self, by):
        self.__build_year = by

    def get_build_year(self):
        return self.__build_year  

class Bot(Robot):
	def __init__(self,whatsapp,fb):
		#Robot.__init__(self,name,build_year)
		self.__whatsapp = whatsapp
		self.__fb = fb

	def get_w(self):
		return self.__whatsapp

	def get_f(self):
		return self.__fb








x = Robot("fr",145)
y = Bot(9852548556,"Rahul")
#print(y.get_build_year())
print(y.get_f())
print(y.get_w())