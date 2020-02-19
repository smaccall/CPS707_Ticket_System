class Ticket():
	'''
	A class to model a Ticket object and its associated properties such as event title, sale price of ticket, number of tickets, and sellers username.
	'''

	def __init__(self, eventTitle, salePrice, numOfTickets, sellerName, buyOrSell):
		'''
		Ticket(str, int, int, str, int)
		Creates a Ticket object with the given event name, sale price, number of tickets for sale, and the sellers username.
		'''
		# Private instance variables for class Ticket
		self.__eTitle = eventTitle
		self.__sPrice = salePrice
		self.__numOfTickets = numOfTickets
		self.__sName = sellerName
		self.__bOrS = buyOrSell

	def __str__(self):
		'''
		T.__str__() or str(T)  --> str
		Returns a str representation of this Ticket for the available tickets file and daily transaction file, depends on buyOrSell field:
		3: "03_EEEEEEEEEEEEEEEEEEE_SSSSSSSSSSSSS_TTT_PPPPPP"
		4: "04_EEEEEEEEEEEEEEEEEEE_SSSSSSSSSSSSS_TTT_PPPPPP"
		0: "EEEEEEEEEEEEEEEEEEE_SSSSSSSSSSSSS_TTT_PPPPPP"
		'''
		# If statements for which str representation, if its buy, sell or just for available tickets file
		if self.__bOrS == "3":
			return "03 {} {} {} {}".format(self.__eTitle, self.__sName, self.__numOfTickets, self.__sPrice)
		elif self.__bOrS == "4":
			return "04 {} {} {} {}".format(self.__eTitle, self.__sName, self.__numOfTickets, self.__sPrice)
		else:
			return "{} {} {} {}".format(self.__eTitle, self.__sName, self.__numOfTickets, self.__sPrice)


class addcredit:
	'''
	Writes addition to credits to dtf
	XX_UUUUUUUUUUUUUUU_TT_CCCCCCCCC
	'''
	@staticmethod
	def add(credit, user):
		f = open("txt_files/dtf.txt", "w")
		f.write("06 " + "{:<15}".format(user.username) + " AA " + "{:<9}".format(credit))
		f.close()
	@staticmethod
	def request(credit,user):
		f = open("txt_files/dtf.txt", "w")
		f.write("06 " + "{:<15}".format(user) + " " + user.role + " " + "{:<9}".format(credit))
		f.close()

class sell:
	def sell():
		print("Does something")


class buy:
	def buy():
		print("Does something")


class createU:
	def creates():
		print("Does something")

	def unique():
		print("do more")


class deleteU:
	def exists():
		print("Does something")

	def delete():
		print("do more")

class User:
	def __init__(self, username, role, credit):
		self.username = username
		self.role = role
		self.credit = credit


class login:
	@staticmethod
	def getAccounts(user):
		f = open("txt_files/user_accounts_file.txt", "r")
		f1 = f.readlines()

		# reads uaf line by line and gets usernames
		for x in f1:
			# print (x[:15].strip())
			if (user == x[:15].strip()):
				role = x[16:18]
				credit = x[19:]
				user1 = User(user, role, credit)
				return user1

		print("User not found")
		return 0

		f.close()


class logout:
	def write_file(transList):
		print("Does something")


class file_update:
	def update_atf():
		print("Does something")

	def update_uaf():
		print("do more")


# Sell method
def sell():
	file1 = open("dtf.txt", "a")
	file2 = open("atf.txt", "a")
	eTitle = input("Enter event title: ")
	salePrice = input("Enter sale price of one ticket: ")
	numOfTickets = input("Enter the number of tickets for sale: ")
	# Need to somehow get user logged in for seller name part
	T1 = Ticket(eTitle, salePrice, numOfTickets, userName, 3)
	# Create ticket entry for available tickets file as well
	T2 = Ticket(eTitle, salePrice, numOfTickets, userName, 0)
	file1.write("\n")
	file1.write(str(T1))
	file2.write("\n")
	file2.write(str(T2))
	file1.close()
	file2.close()


# Buy method
def buy():
	file1 = open("dtf.txt", "a")
	file2 = open("atf.txt", "a")
	eTitle = input("Enter event title: ")
	numOfTickets = input("Enter number of tickets: ")
	sellerName = input("Enter the seller's username: ")
	# Need to calculate total sale price and read from available tickets file
	confirmation = input("Total price is: $$$. Confirm yes/no: ")
	# Need to somehow subtract number of tickets from available tickets file
	# salePrice is cost of one ticket
	T = Ticket(eTitle, salePrice, numOfTickets, sellerName, 4)
	file1.write("\n")
	file1.write(str(T))
	file1.close()
	file2.close()


def main():
	print("N.A.T.M Menu \n")
	# The
	user = input("login: ")
	log = login.getAccounts(user)
	while log == 0:
		user = input("Invalid username. Please login: ")
		log = login.getAccounts(user)
	action = input("Enter a command (logout, addcredit, createaccount, deleteaccount, buy, sell, refund)")
	# List of users created
	uList = {}
	# List of actions on tickets list
	ticList = {}
	# List of transactions
	transList = []


if __name__ == '__main__':
	main()
