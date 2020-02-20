class Ticket:
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

	# Sell method
	@staticmethod
	def sell(user):
		file1 = open("dtf.txt", "a")
		file2 = open("atf.txt", "a")
		eTitle = input("Enter event title: ")
		salePrice = input("Enter sale price of one ticket: ")
		numOfTickets = input("Enter the number of tickets for sale: ")
		if numOfTickets < 101 and salePrice < 1000 and len(eTitle) < 26:
			# Need to somehow get user logged in for seller name part
			T1 = Ticket(eTitle, salePrice, numOfTickets, user.username, 3)
			# Create ticket entry for available tickets file as well
			T2 = Ticket(eTitle, salePrice, numOfTickets, user.username, 0)
			file1.write("\n")
			file1.write(str(T1))
			file2.write("\n")
			file2.write(str(T2))
		else:
			print("Invalid inputs.")
		file1.close()
		file2.close()

	# Buy method
	@staticmethod
	def buy(user):
		file1 = open("dtf.txt", "a")
		file2 = open("atf.txt", "a")
		eTitle = input("Enter event title: ")
		sellerName = input("Enter the seller's username: ")
		exist = False
		confirmation = ""
		for ticket in file2:
			matchT = ticket[:25].strip()
			matchS = ticket[26:41].strip()
			if matchT.lower() == eTitle.lower() and matchS.lower() == sellerName.lower():
				exist = True
				T = Ticket(matchT, matchS, ticket[42:45].strip(), ticket[46:].strip(), 4)
				numOfTickets = input("Enter number of tickets: ")
				if not user.account == "AA":
					if numOfTickets > 4:
						print("Invalid number of tickets")
						break
				if numOfTickets > T.__numOfTickets:
					print("Not enough tickets for sale.")
					break
				total = numOfTickets * T.__sPrice
				confirmation = input("Single ticket: $"+T.__sPrice+" | Total price is: $"+total+". Confirm yes/no: ")
				if confirmation.lower() == "no":
					print("Transaction cancelled")
					break
				# Need to somehow subtract number of tickets from available tickets file
				file1.write("\n")
				file1.write(str(T))
				file1.close()
				file2.close()
				break
		if confirmation.lower() == "yes":
			with open("txt_file/atf.txt", "r") as f:
				lines = f.readlines()
			with open("txt_file/atf.txt", "w") as f:
				for line in lines:
					if line.strip("\n") != T.__str__()[3:]:
						f.write(line)
				T.__numOfTickets = T.__numOfTickets - numOfTickets
				f.write(T.__str__()[3:])
		if not exist:
			print("Ticket not found")


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
	def request(credit, user):
		f = open("txt_files/dtf.txt", "w")
		f.write("06 " + "{:<15}".format(user) + " " + user.role + " " + "{:<9}".format(credit))
		f.close()

class User:
	def __init__(self, username, role, credit):
		self.username = username
		self.role = role
		self.credit = credit

	def logout(self):
		f = open("txt_files/dtf.txt", "w")
		f.write("00 " + "{:<15}".format(self.username) + " " + self.role + " " + "{:<9}".format(self.credit))
		f.close()

	def create(self):
		name = input("Username: ")
		aType = input("Account Type: ")
		credit = input("Starting Credit")
		f = open("txt_files/uaf.txt", "w")
		f.write("{:<15}".format(name) + " " + aType + " " + "{:<9}".format(credit))
		f.close()
		f = open("txt_files/dtf.txt", "w")
		f.write("01 " + "{:<15}".format(self.username) + " " + self.role + " " + "{:<9}".format(self.credit))
		f.close()

	def delete(self):
		name = input("Username: ")
		with open("txt_file/uaf.txt", "r") as f:
			lines = f.readlines()
		with open("txt_file/uaf.txt", "w") as f:
			for line in lines:
				if line[:15].strip() != name:
					f.write(line)
			f.close()
		f = open("txt_files/dtf.txt", "w")
		f.write("02 " + "{:<15}".format(self.username) + " " + self.role + " " + "{:<9}".format(self.credit))
		f.close()
	
	@staticmethod
	def refund(user):
		print("SOMETHING")

class Login:
	@staticmethod
	def login():
		user = input("login: ")
		current_user = Login.getAccounts(user)
		while current_user == 0:
			user = input("Invalid username. Please login: ")
			current_user = Login.getAccounts(user)
		return current_user

	@staticmethod
	def getAccounts(user):
		f = open("txt_files/uaf.txt", "r")
		f1 = f.readlines()

		# reads uaf line by line and gets usernames
		for x in f1:
			# print (x[:15].strip())
			if user == x[:15].strip():
				role = x[16:18]
				credit = x[19:]
				user1 = User(user, role, credit)
				f.close()
				return user1

		print("User not found")
		f.close()
		return 0

		f.close()

def main():
	print("N.A.T.M Menu \n")
	current_user = Login.login()
	action = input("Enter a command (logout, addcredit, createaccount, deleteaccount, buy, sell, refund)")
	while action != "EXIT":
		if action == "logout":
			current_user.logout()
			current_user = Login.login()
		elif action == "buy":
			if current_user.role != "SS":
				Ticket.buy(current_user)
			else:
				print("Access denied.")
		elif action == "sell":
			if current_user.role != "BS":
				Ticket.sell(current_user)
			else:
				print("Access denied.")
		elif action == "createaccount":
			if current_user == "AA":
				User.create(current_user)
			else:
				print("Access denied.")
		elif action == "deleteaccount":
			if current_user == "AA":
				User.delete(current_user)
			else:
				print("Access denied.")

		else:
			print("Invlaid option, try again.")

		action = input("Enter a command (logout, addcredit, createaccount, deleteaccount, buy, sell, refund)")


if __name__ == '__main__':
	main()
