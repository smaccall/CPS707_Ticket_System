'''
Not another Ticket Master is a ticketing service that manages transactions between buyers and sellers for events. Buyers
    buy tickets from multiple vendors and are also able to request a refund. Sellers are able to market their tickets
    for the price they want to sell at their convenience. Admins are around to monitor priviledged transactions.

@author: Sarah MacCallum, Vinh Nguyen, Nikola Pavlovic
@version: 1.0
'''
import sys
import shutil
from os import path


class uInput:
    @staticmethod
    def userIn(prompt):
        hold = input(prompt)
        print("")
        if hold == ("EXIT"):
            sys.exit()
        return hold.strip()


class Ticket:
    '''
    A class to model a Ticket object and its associated properties such as event title, sale price of ticket, number of tickets, and sellers username.
    '''

    '''
    The constructor for a Ticket object

    :param self
    :param eventTitle
    :param salePrice
    :param numOfTickets
    :param sellerName
    :param buyOrSell
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
            return "03 {:<19} {:<13} {:0<3} {:0=6.2f}".format(self.__eTitle, self.__sName, self.__numOfTickets,
                                                              self.__sPrice)
        elif self.__bOrS == "4":
            return "04 {:<20} {:<13} {:0<3} {:0=6.2f}".format(self.__eTitle, self.__sName, self.__sPrice,
                                                              self.__numOfTickets)
        else:
            return "{:<20} {:<13} {:0<3} {:0=6.2f}".format(self.__eTitle, self.__sName, self.__numOfTickets,
                                                           self.__sPrice)

    '''
    User is adding tickets to sell and is being stored in atf.txt

    :param User
    '''

    @staticmethod
    def sell(user):
        # open both dtf and atf.txt
        file1 = open(dtf, "a")
        file2 = open(atf, "a")
        # Retrieve input from user for event title, sale price and number of tickets available
        eTitle = uIn.userIn("What is the name of your event: ")
        while len(eTitle) > 25:
            print("Please enter a valid event name")
            eTitle = uIn.userIn("What is the name of your event: ")
        salePrice = uIn.userIn("What is the price of your tickets: ")
        salePrice = float(salePrice)
        while salePrice > 999.99 or salePrice < 0:
            print("Invalid inputs.")
            salePrice = uIn.userIn("What is the price of your tickets: ")
            salePrice = float(salePrice)
        numOfTickets = uIn.userIn("What is the amount of tickets: ")
        while int(numOfTickets) > 100 or int(numOfTickets) < 0:
            print("Invalid inputs.")
            numOfTickets = uIn.userIn("What is the amount of tickets: ")
        print("Ticket will be available after logout")
        # Check to see if all input values are valid
        if int(numOfTickets) < 101 and float(salePrice) < 1000 and len(eTitle) < 26:
            ticketnum = int(numOfTickets)
            priceOfSale = int(salePrice)
            # Create ticket object for sale records in dtf
            T1 = Ticket(eTitle, priceOfSale, ticketnum, user.username, 3)
            # Create ticket object for atf.txt
            T2 = Ticket(eTitle, priceOfSale, ticketnum, user.username, 0)
            hold = int(numOfTickets)
            file1.write("\n03 {:<20} {:<13} {:03d} {:0=6.2f}".format(T1.__eTitle, T1.__sName, hold, priceOfSale))
            with open(atf, "r") as f:
                lines = f.readlines()
            with open(atf, "w") as f:
                for line in lines:
                    if line.strip("\n") != "END":
                        f.write(line)
            file2.write("{:<19} {:<14} {:03d} {:0=6.2f}".format(T1.__eTitle, T1.__sName, ticketnum, priceOfSale) + "\n")
            file2.write("END\n")
        else:
            print("Invalid inputs.")
        file1.close()
        file2.close()

    '''
    User is buying tickets for an event

    :param User
    '''

    @staticmethod
    def buy(user):
        file1 = open(dtf, "r+")
        file2 = open(atf, "r+")
        # Retrieve input from user for ticket they want to buy
        eTitle = uIn.userIn("Enter event title: ")
        sellerName = uIn.userIn("Enter the seller's username: ")
        exist = False
        confirmation = ""
        # Check to see if the ticket they want exists
        for ticket in file2:
            matchT = ticket[:20].strip()
            matchS = ticket[20:33].strip()
            # If the event title and seller name are correct move forward in th ebuying process
            if matchT.lower() == eTitle.lower() and matchS.lower() == sellerName.lower():
                exist = True

                # Create ticket object for easier access to values
                T = Ticket(matchT, ticket[39:].strip(), ticket[33:39].strip(), matchS, 4)
                # Get number of tickets wanted from user
                numOfTickets = uIn.userIn("Enter number of tickets: ")
                # Verify amount is valid for user requesting

                if int(numOfTickets) < 1:
                    print("Invalid number of tickets")
                    break
                if not user.role == "AA":
                    if int(numOfTickets) > 4:
                        print("Invalid number of tickets")
                        break
                # Check to see if there are enough tickets for sale
                if int(numOfTickets) > int(T.__numOfTickets):
                    print("Not enough tickets for sale.")
                    break
                # Calculate final cost
                total = int(numOfTickets) * float(T.__sPrice)
                hold = float(T.__sPrice)
                confirmation = uIn.userIn("Single ticket: $" + "{:.2f}".format(hold) + " | Total price is: $"
                                          + "{:.2f}".format(total) + ". Confirm yes/no: ")
                # Don't proceed if user does not confirm
                if confirmation.lower() == "no":
                    print("Transaction cancelled")
                    break
                if confirmation.lower() == "yes":
                    print("Ticket purchased.")
                file1.write("\n")
                ticketnum = int(T.__numOfTickets) - int(numOfTickets)
                file1.write("04 {:<20} {:<13} {:03d} {:0=6.2f}".format(T.__eTitle, T.__sName, ticketnum, hold))
                file1.close()
                file2.close()
                # Update atf.txt file with the correct amount of tickets available
                with open(atf, "r") as f:
                    lines = f.readlines()
                with open(atf, "w") as f:
                    for line in lines:
                        if (line[:20].strip().lower() != eTitle.lower() and line[
                                                                            20:33].strip().lower() != sellerName.lower()) and (
                                line.strip("\n") != "END"):
                            f.write(line)
                    T.__numOfTickets = ticketnum
                    f.write("{:<19} {:<14} {:03d} {:0=6.2f}".format(T.__eTitle, T.__sName, ticketnum, hold))
                    f.write("\nEND")
                break
        # User asked for a ticket that is not in the system
        if not exist:
            print("Ticket not found")


class addcredit:
    """
    Writes updates credit amount of a user to dtf
    Priviledge action
    XX_UUUUUUUUUUUUUUU_TT_CCCCCCCCC

    @param user
    @return null
    """

    @staticmethod
    def add(user):

        # Get amount of credit being added and to which account
        c = uIn.userIn("Enter amount: ")
        if float(c) > 1000.00:
            print("Invalid amount")
        else:
            uName = uIn.userIn("Enter username: ")
            total = float(c)
            with open(dtf, "r") as f:
                lines = f.readlines()
            with open(dtf, "w") as f:
                for x in lines:
                    if x[:3].strip() == "06":
                        if uName == x[3:18].strip():
                            value = float(x[23:].strip("\n"))
                            total += value
                    if x[:3].strip() == "00":
                        total = float(c)
                    f.write(x)
            if total > 1000.00:
                print("Credit can not be added")
            else:
                account = Login.getAccounts(uName)
                test = Login.getAccounts(uName)
                # Update amount of credit user has available
                account.credit = account.credit + float(c)
                # Record transaction in dtf
                hold = float(c)
                f = open(dtf, "a")
                f.write(
                    "\n06 " + "{:<15}".format(account.username) + " " + account.role + " " + "{:0=9.2f}".format(hold))
                f.close()
                # Update uaf.txt file with the users new available credit amount
                with open(uaf, "r") as f:
                    lines = f.readlines()
                with open(uaf, "w") as f:
                    for line in lines:
                        if line[:15].strip() != account.username:
                            f.write(line)
                    f.write("\n")
                    f.write("{:<15}".format(account.username) + " " + account.role + " " + "{:0=9.2f}".format(
                        account.credit))
                    f.close()
                print("Credit added")

    '''
    Creates a request log in the dtf 

    @param user
    @return null
    '''

    @staticmethod
    def request(user):
        f = open(dtf, "w")
        credit = uIn.userIn("Enter amount: ")
        hold = float(credit)
        f.write("\n07 " + "{:<15}".format(user.username) + " " + user.role + " " + "{:0=9.2f}".format(hold))
        f.close()
        print("Request made")


class User():
    '''
    Contructor class

    @param self
    @param username
    @param role
    @param credit
    @return
    '''

    def __init__(self, username, role, c):
        self.username = username
        self.role = role
        self.credit = c

    '''
    Logs the user action of logging out in dtf

    @param self
    @return null
    '''

    @staticmethod
    def logout(self):
        f = open(dtf, "a")
        c = float(self.credit)
        f.write("\n00 " + "{:<15}".format(self.username) + " " + self.role + " " + "{:0=9.2f}".format(c) + "\n")
        f.close()
        print("Logout successful")

    def is_float(string):
        try:
            if float(string) or int(string):
                return True
        except ValueError:
            return False

    '''
    promts user for username, account type and credit amount
    checks if the user already exists
    creates and logs new user into dtf and uaf.txt

    @param self
    @return null
    '''

    def create(self):
        name = uIn.userIn("Enter Username: ")
        chars = set("@#$%^&*()+-=_~[]{}:;.,\"\'/| ")
        if (len(name) > 15) or any((c in chars) for c in name) or (len(name) < 1):
            print("Invalid input.")
        else:
            while True:
                aType = uIn.userIn("Enter an account type: ")
                if aType.lower() == "admin":
                    aType = "AA"
                    print("Account type is Admin")
                    break
                elif aType.lower() == "full-standard":
                    aType = "FS"
                    print("Account type is Full-Standard")
                    break
                elif aType.lower() == "buy-standard":
                    aType = "BS"
                    print("Account type is Buy-Standard")
                    break
                elif aType.lower() == "sell-standard":
                    aType = "SS"
                    print("Account type is Sell-Standard")
                    break
                else:
                    print("Invalid input.")
            credit = uIn.userIn("Starting Credit: ")
            # print(User.is_float(credit))
            # print(len(credit.rsplit('.')[-1]))
            if not User.is_float(credit):
                print("Invalid credit amount")
                credit = uIn.userIn("Starting Credit: ")
            while ((float(credit) < 0.00) or (float(credit) > 999999.00) or (len(credit.rsplit('.')[-1]) > 2)):
                print("Invalid credit amount")
                credit = uIn.userIn("Starting Credit: ")
            f = open(uaf, "r+")
            exist = False
            for user in f:
                # print(user[0:15].strip())
                if user[0:15].strip() == name:
                    exist = True
                    print("User already exists.")
            if not exist:
                hold = float(credit)
                f.write("\n{:<15}".format(name) + " " + aType + " " + "{:0=9.2f}".format(hold))
                f.close()
                f2 = open(dtf, "w")
                f2.write("01 " + "{:<15}".format(name) + " " + aType + " " + "{:0=9.2f}".format(hold))
                f2.close()
                print("Account created")
            f.close()

    '''
    Prompts user for an account username to delete
    updates uaf.txt to remove account from listing
    logs action in dtf
    Can only be done from a priviledged account type

    @param null
    @return null
    '''

    def delete(self):
        name = uIn.userIn("Enter Username to delete: ")
        account = Login.getAccounts(name)
        if account != 0:
            if account.username == self.username:
                print("Can not delete current user logged in")
            else:
                with open(uaf, "r") as f:
                    lines = f.readlines()
                with open(uaf, "w") as f:
                    for line in lines:
                        if line[:15].strip() != name:
                            f.write(line)
                    f.close()
                f = open(dtf, "w")
                f.write(
                    "02 " + "{:<15}".format(self.username) + " " + self.role + " " + "{:0=9.2f}".format(self.credit))
                f.close()
                with open(atf, "w") as f:
                    for line in lines:
                        if line[23:36].strip() != name:
                            f.write(line)
                print("Deletion successful")

    '''
    Takes in user object as account processing transaction
    Prompts user for buyer and seller name to refund/ transfer credits between accounts

    @param user
    @return null
    '''

    @staticmethod
    def refund(user):
        buyer = uIn.userIn("Enter the buyer's username: ")
        seller = uIn.userIn("Enter the seller's username: ")
        userB = Login.getAccounts(buyer)
        userS = Login.getAccounts(seller)
        if not (userB == 0 or userS == 0):
            refundAmount = uIn.userIn("Credits amount for refund: ")
            floatAmount = float(refundAmount)
            while floatAmount > 999999.00:
                print("Credit amount invalid")
                refundAmount = uIn.userIn("Credits amount for refund: ")
                floatAmount = float(refundAmount)
            if (userS.credit - floatAmount) < 0.00:
                print("Seller does not have sufficent, can not process transaction")
            elif (userB.credit + floatAmount) > 999999.00:
                print("Maxiumum amount of credits reached, can not process transaction")

            else:
                userS.credit = userS.credit - float(refundAmount)
                userB.credit = userB.credit + float(refundAmount)
                ra = float(refundAmount)
                file1 = open(dtf, "w+")
                file1.write("05 " + "{:<15}".format(buyer) + "{:<15}".format(seller) + "{:0=9.2f}".format(ra) + "\n")
                file1.close()

                with open(uaf, "r") as f:
                    lines = f.readlines()
                with open(uaf, "w") as f:
                    for line in lines:
                        if not ((line[:15].strip() == userB.username) or (line[:15].strip() == userS.username)):
                            f.write(line)
                    buyerCredit = float(userB.credit)
                    sellerCredit = float(userS.credit)
                    f.write("\n" + "{:<15}".format(userB.username) + " " + userB.role + " " + "{:0=9.2f}".format(
                        buyerCredit) + "\n")
                    f.write("{:<15}".format(userS.username) + " " + userS.role + " " + "{:0=9.2f}".format(sellerCredit))
                    f.close()
                    print("Refund complete")


class Login:
    """
    Initalizes login sequence, asking user for username as input and returing the current user as object

    @return current_user
    """

    @staticmethod
    def login():
        a = uIn.userIn("To log in type login: ")
        while a.lower() != "login":
            a = uIn.userIn("To log in type login: ")
        user = uIn.userIn("Enter Username: ")
        current_user = Login.getAccounts(user)
        while current_user == 0:
            print("Invalid username, please try again")
            user = uIn.userIn("Enter Username: ")
            current_user = Login.getAccounts(user)
        print("Login successful")
        return current_user

    '''
    Given the username, this method will search through the uaf.txt to find and return 
    user account as an object

    @param user
    @return user1
    '''

    @staticmethod
    def getAccounts(user):
        f = open(uaf, "r")
        f1 = f.readlines()

        # reads uaf line by line and gets usernames
        for x in f1:
            if user == x[:15].strip():
                role = x[16:18]
                credit = x[19:]
                new_user = User(user, role, float(credit))
                f.close()
                return new_user

        print("User not found")
        f.close()
        return 0


def main():
    print("Welcome to Not Another Ticket Master")
    current_user = Login.login()

    action = uIn.userIn("Enter a command (logout, addcredit, createaccount, deleteaccount, buy, sell, refund)")
    while action != "EXIT":
        action = action.lower()
        action = action.strip()
        if action == "logout":
            current_user.logout(current_user)
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
                break
        elif action == "createaccount":
            if current_user.role == "AA":
                User.create(current_user)
            else:
                print("Access denied.")
        elif action == "deleteaccount":
            if current_user.role == "AA":
                User.delete(current_user)
            else:
                print("Access denied.")
        elif action == "refund":
            if current_user.role == "AA":
                User.refund(current_user)
            else:
                print("Access denied.")
        elif action == "addcredit":
            second_action = uIn.userIn("Enter add or request: ")
            if second_action == "add" and current_user.role == "AA":
                addcredit.add(current_user)
            elif second_action == "request":
                addcredit.request(current_user)
            else:
                print("Access denied.")
        else:
            print("Invalid option, try again.")

        action = uIn.userIn("Enter a command (logout, addcredit, createaccount, deleteaccount, buy, sell, refund)")


if __name__ == '__main__':
    uaf = sys.argv[1]
    atf = sys.argv[2]
    dtf = sys.argv[3]
    test = sys.argv[4]

    test_path = path.realpath(test)
    t_head, t_tail = path.split(test_path)
    t_tail = t_tail.split("_")

    uaf_path = path.realpath(uaf)
    head, tail = path.split(uaf_path)
    dst = head + "/output/" + t_tail[0] + "_uaf.txt"
    shutil.copy(uaf_path, dst)
    uaf = (dst)

    atf_path = path.realpath(atf)
    head, tail = path.split(atf_path)
    dst = head + "/output/" + t_tail[0] + "_atf.txt"
    shutil.copy(atf_path, dst)
    atf = (dst)

    dtf_path = path.realpath(dtf)
    head, tail = path.split(dtf_path)
    dst = head + "/output/" + t_tail[0] + "_dtf.txt"
    shutil.copy(dtf_path, dst)
    dtf = (dst)

    uIn = uInput()
    main()
