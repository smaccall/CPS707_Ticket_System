'''
Not another Ticket Master is a ticketing service that manages transactions between buyers and sellers for events. Buyers
    buy tickets from multiple vendors and are also able to request a refund. Sellers are able to market their tickets
    for the price they want to sell at their convenience. Admins are around to monitor priviledged transactions.

@author: Sarah MacCallum, Vinh Nguyen, Nikola Pavlovic
@version: 1.0
'''
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
            return "03 {} {} {} {}".format(self.__eTitle, self.__sName, self.__numOfTickets, self.__sPrice)
        elif self.__bOrS == "4":
            return "04 {} {} {} {}".format(self.__eTitle, self.__sName, self.__numOfTickets, self.__sPrice)
        else:
            return "{} {} {} {}".format(self.__eTitle, self.__sName, self.__numOfTickets, self.__sPrice)

    '''
    User is adding tickets to sell and is being stored in atf.txt
    
    :param User
    '''
    @staticmethod
    def sell(user):
        # open both dtf.txt and atf.txt
        file1 = open("dtf.txt", "a")
        file2 = open("atf.txt", "a")
        # Retrieve input from user for event title, sale price and number of tickets available
        eTitle = input("Enter event title: ")
        salePrice = input("Enter sale price of one ticket: ")
        numOfTickets = input("Enter the number of tickets for sale: ")
        # Check to see if all input values are valid
        if numOfTickets < 101 and salePrice < 1000 and len(eTitle) < 26:
            # Create ticket object for sale records in dtf.txt
            T1 = Ticket(eTitle, salePrice, numOfTickets, user.username, 3)
            # Create ticket object for atf.txt
            T2 = Ticket(eTitle, salePrice, numOfTickets, user.username, 0)
            file1.write("\n" + str(T1))
            file2.write("\n" + str(T2))
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
        file1 = open("dtf.txt", "a")
        file2 = open("atf.txt", "a")
        # Retrieve input from user for ticket they want to buy
        eTitle = input("Enter event title: ")
        sellerName = input("Enter the seller's username: ")
        exist = False
        confirmation = ""
        # Check to see if the ticket they want exists
        for ticket in file2:
            matchT = ticket[:25].strip()
            matchS = ticket[26:41].strip()
            # If the event title and seller name are correct move forward in th ebuying process
            if matchT.lower() == eTitle.lower() and matchS.lower() == sellerName.lower():
                exist = True
                # Create ticket object for easier access to values
                T = Ticket(matchT, matchS, ticket[42:45].strip(), ticket[46:].strip(), 4)
                # Get number of tickets wanted from user
                numOfTickets = input("Enter number of tickets: ")
                # Verify amount is valid for user requesting
                if not user.account == "AA":
                    if numOfTickets > 4:
                        print("Invalid number of tickets")
                        break
                # Check to see if there are enough tickets for sale
                if numOfTickets > T.__numOfTickets:
                    print("Not enough tickets for sale.")
                    break
                # Calculate final cost
                total = numOfTickets * T.__sPrice
                confirmation = input("Single ticket: $" + T.__sPrice + " | Total price is: $"
                                     + total + ". Confirm yes/no: ")
                # Don't proceed if user does not confirm
                if confirmation.lower() == "no":
                    print("Transaction cancelled")
                    break
                file1.write("\n")
                file1.write(str(T))
                file1.close()
                file2.close()
                # Update atf.txt file with the correct amount of tickets available
                with open("txt_file/atf.txt", "r") as f:
                    lines = f.readlines()
                with open("txt_file/atf.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != T.__str__()[3:]:
                            f.write(line)
                    T.__numOfTickets = T.__numOfTickets - numOfTickets
                    f.write(T.__str__()[3:])
                break
        # User asked for a ticket that is not in the system
        if not exist:
            print("Ticket not found")


class addcredit:
    """
    Writes updates credit amount of a user to dtf.txt
    Priviledge action
    XX_UUUUUUUUUUUUUUU_TT_CCCCCCCCC

    @param user
    @return null
    """
    @staticmethod
    def add(user):
        f = open("txt_files/dtf.txt", "w")
        # Get amount of credit being added and to which account
        credit = input("Enter the amount of credit")
        uName = input("Enter the username for where to transfer credit")
        account = Login.getAccounts(uName)
        # Update amount of credit user has available
        account.credit = account.credit + credit
        # Record transaction in dtf.txt
        f.write("06 " + "{:<15}".format(user.username) + " AA " + "{:<9}".format(credit))
        f.close()
        # Update uaf.txt file with the users new available credit amount
        with open("txt_file/uaf.txt", "r") as f:
            lines = f.readlines()
        with open("txt_file/uaf.txt", "w") as f:
            for line in lines:
                if line[:15].strip() != account.username:
                    f.write(line)
            f.write("{:<15}".format(account.username) + " " + account.role + " " + "{:<9}".format(account.credit))
            f.close()
    
    '''
    Creates a request log in the dtf.txt 
    
    @param user
    @return null
    '''
    @staticmethod
    def request(user):
        f = open("txt_files/dtf.txt", "w")
        credit = input("Enter the amount of credit")
        f.write("07 " + "{:<15}".format(user.username) + " " + user.role + " " + "{:<9}".format(credit))
        f.close()


class User:
    
    '''
    Contructor class
    
    @param self
    @param username
    @param role
    @param credit
    @return
    '''
    def __init__(self, username, role, credit):
        self.username = username
        self.role = role
        self.credit = credit

    '''
    Logs the user action of logging out in dtf.txt
    
    @param self
    @return null
    '''
    @staticmethod
    def logout(self):
        f = open("txt_files/dtf.txt", "w")
        f.write("00 " + "{:<15}".format(self.username) + " " + self.role + " " + "{:<9}".format(self.credit))
        f.close()

    '''
    promts user for username, account type and credit amount
    checks if the user already exists
    creates and logs new user into dtf.txt and uaf.txt
    
    @param self
    @return null
    '''
    def create(self):
        name = input("Username: ")
        aType = input("Account Type: ")
        credit = input("Starting Credit")
        f = open("txt_files/uaf.txt", "w")
        exist = False
        for user in f:
            if user[0:15].strip() == name:
                exist = True
                print("User already exists.")
        if not exist:
            f.write("{:<15}".format(name) + " " + aType + " " + "{:<9}".format(credit))
            f.close()
            f = open("txt_files/dtf.txt", "w")
            f.write("01 " + "{:<15}".format(self.username) + " " + self.role + " " + "{:<9}".format(self.credit))
        f.close()
    
    '''
    Prompts user for an account username to delete
    updates uaf.txt to remove account from listing
    logs action in dtf.txt
    Can only be done from a priviledged account type
    
    @param null
    @return null
    '''
    def delete(self):
        name = input("Username: ")
        account = Login.getAccounts(name)
        if account != 0:
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
    
    '''
    Takes in user object as account processing transaction
    Prompts user for buyer and seller name to refund/ transfer credits between accounts
    
    @param user
    @return null
    '''
    @staticmethod
    def refund(user):
        file1 = open("txt_files/dtf.txt", "a")
        buyer = input("Enter the seller's username: ")
        seller = input("Enter the seller's username: ")
        userB = Login.getAccounts(buyer)
        userS = Login.getAccounts(seller)
        if not (userB == 0 or userS == 0):
            refundAmount = input("Enter the amount to refund: ")
            userS.credit = userS.credit - refundAmount
            userB.credit = userB.credit + refundAmount
            file1.write("05 " + "{:<15}".format(buyer) + "{:<15}".format(seller) + "{:<9}".format(refundAmount))
            file1.close()
            with open("txt_file/uaf.txt", "r") as f:
                lines = f.readlines()
            with open("txt_file/uaf.txt", "w") as f:
                for line in lines:
                    if line[:15].strip() != userB or line[:15].strip() != userS:
                        f.write(line)
                f.write("{:<15}".format(userB.username) + " " + userB.role + " " + "{:<9}".format(userB.credit))
                f.write("{:<15}".format(userS.username) + " " + userS.role + " " + "{:<9}".format(userS.credit))
                f.close()


class Login:
    """
    Initalizes login sequence, asking user for username as input and returing the current user as object
    
    @return current_user
    """
    @staticmethod
    def login():
        user = input("login: ")
        current_user = Login.getAccounts(user)
        while current_user == 0:
            user = input("Invalid username. Please login: ")
            current_user = Login.getAccounts(user)
        return current_user

    '''
    Given the username, this method will search through the uaf.txt to find and return 
    user account as an object
    
    @param user
    @return user1
    '''
    @staticmethod
    def getAccounts(user):
        f = open("txt_files/uaf.txt", "r")
        f1 = f.readlines()

        # reads uaf line by line and gets usernames
        for x in f1:
            if user == x[:15].strip():
                role = x[16:18]
                credit = x[19:]
                new_user = User(user, role, credit)
                f.close()
                return new_user

        print("User not found")
        f.close()
        return 0

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
        elif action == "refund":
            if current_user.role == "AA":
                User.refund(current_user)
            else:
                print("Access denied.")
        elif action == "addcredit":
            second_action = input("add or request: ")
            if second_action == "add" and current_user.role == "AA":
                addcredit.add(current_user)
            elif second_action == "request":
                addcredit.request(current_user)
            else:
                print("Access denied.")
        else:
            print("Invlaid option, try again.")

        action = input("Enter a command (logout, addcredit, createaccount, deleteaccount, buy, sell, refund)")


if __name__ == '__main__':
    main()
