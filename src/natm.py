


class addcredit():
	def add():
		print ("Does something")
		
	def request():
		print ("do more")

class sell():
	def sell():
		print ("Does something")

class buy():
	def buy():
		print ("Does something")

class createU():
	def creates():
		print ("Does something")
		
	def unique():
		print ("do more")

class deleteU():
	def exists():
		print ("Does something")
		
	def delete():
		print ("do more")

class login():
	@staticmethod
	def getAccounts(user):
		f = open("uaf.txt", "r")
		f1 = f.readlines()
		
		#reads uaf line by line and gets usernames
		for x in f1:
			#print (x[:15].strip())
			if (user == x[:15].strip()):
				print ("user is found")
				return 1
			
		print ("user not found")
		return 0
			
			
		f.close()
		
		
class logout():
	def write_file():
		print ("Does something")

class file_update():
	def update_atf():
		print ("Does something")
	
	def update_uaf():
		print ("do more")


def main(): 
	
	
	print("Natm menu \n")
	
	hold = input ("login: ")
	
	log = login()
	
	log.getAccounts(hold)
	
	
if __name__ == '__main__':
	main()
