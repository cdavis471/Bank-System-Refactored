#Student Number: C20441826
#Name: Conor Davis
#Module: CMPU2016
#Course Code: TU856
#IDE: Visual Studio Code
#Language: Python 3.9.7 64-bit (system)
#Program Description: Bank Management System

#imports / important stuff
#needed to set current directory to location of files for assignment to use run code properly on VSC
import os
os.chdir('C:/Users/C20441826/OneDrive - Technological University Dublin/Desktop/College/Year 2/Semester 1/Object Oriented Programming/Assignment 2/Finished')
#used to generate iban
from random import randrange
#used for dates
from datetime import datetime, date

#Customer class
class Customer:
    """This class is used to store all information relevant to customers / users."""

    def __init__(self, cust_id, cust_acc, cust_pass, cust_name, cust_age, cust_email, cust_phone, cust_address):
        """Intializes Customer Attributes"""
        #variables for customer storage
        self.cust_id = cust_id
        self.cust_acc = cust_acc
        self.cust_pass = cust_pass
        self.cust_name = cust_name
        self.cust_age = cust_age
        self.cust_email = cust_email
        self.cust_phone = cust_phone
        self.cust_address = cust_address
    #end __init__ method
    
    def __str__(self):
        """Represent Customer Instance as String"""
        return "{} - ID: {}".format(self.cust_name, self.cust_id)
    #end __str__ method

    #login into existing customer account
    def login(self):
        """Display Login Message"""
        #return string
        return "\nWelcome back {}!".format(self.cust_name)
    #end login method

    #register new customer account
    def register(self, file="customers.txt"):
        """This adds a new customer record to the required file."""
        #opening and writing file
        try:
            #open customer file
            file_open = open(file, "a")
            #string for new customer record
            new_customer = "CustID:" + self.cust_id + "; - " + "CustAcc:" + self.cust_acc + "; - " + "CustPass:" + self.cust_pass + "; - " + "CustName:" + self.cust_name + "; - " + "CustAge:" + self.cust_age + "; - " + "CustEmail:" + self.cust_email + "; - " + "CustPhone:" + self.cust_phone + "; - " + "CustAddress:" + self.cust_address + ";ENDED;\n"
            #add new customer record
            file_open.write(new_customer)
            #close file
            file_open.close()
            #return string
            return "{}, your new customer account has been created.\n".format(self.cust_name)
        #end try
        #should the file fail to open
        except IOError:
            print("A critical error has occurred in the program - functionality has been crippled.\nThe program has to exit...")
            quit()
        #end IOError except 
    #end register method

#end Customer class

#Account class
class Account(object):
    """This class is used to store all information relevant to Bank Accounts - it has two subclasses: Checking & Saving"""
    
    def __init__(self, acc_id, acc_custName, acc_iban, acc_bal):
        """Intializes Account Attributes"""
        self.acc_id = acc_id
        self.acc_custName = acc_custName
        self.acc_iban = acc_iban
        self.acc_bal = acc_bal
    #end __init__ method

    def __str__(self):
        """Represent Account Instance as String"""
        return "Account ID: {} - IBAN: {} - Balance: {}".format(self.acc_id, self.acc_iban, self.acc_bal)
    #end __str__ method
    
    #balance - display money
    def balance(self):
        """Display balance of account."""
        return "Account Balance: {}".format(self.acc_bal)
    #end balance method

    #update balance
    def update_balance(self, value, type, file="accounts.txt"):
        """Update balance of account."""
        record_bal = self.acc_bal
        if(type == 0):
            new_bal = int(self.acc_bal) + int(value)
        elif(type == 1):
            new_bal = int(self.acc_bal) - int(value)
        self.acc_bal = str(new_bal)
        #search parameters
        start = "AccID:"
        middle = str(self.acc_id)
        end = ";"
        search = str(start + middle + end)
        #opening and writing file
        try:
            #open file to read
            file_open = open(file, "r")
            #save lines
            lines = file_open.readlines()
            #run through lines for specific record
            for line in lines:
                #will return 0 when a match is found
                result = line.find(search)
                #when match found
                if(result != -1):
                    #save line
                    save_line = line
                    #break loop
                    break
                #end if statement
            #end for loop
            #new record string
            old_bal_string = "BAL:" + record_bal + ";"
            new_bal_string = "BAL:" + str(self.acc_bal) + ";"
            #replace balance in old record to form new record
            new_record = save_line.replace(old_bal_string,new_bal_string)
            #opening and writing file
            #open file again to write
            file_open_two = open(file, "w")
            #run through each record to rewrite file
            for line in lines:
                #lines to keep the same
                if line != save_line:
                    #rewrite line
                    file_open_two.write(line)
                #end if statement
                #lines to edit
                else:
                    #rewrite line
                    file_open_two.write(new_record)
                #end else statement
            #close file
            file_open.close()
            file_open_two.close()
            #return new bal to edit instance
            return int(self.acc_bal)
        #should the file fail to open
        except IOError:
            print("A critical error has occurred in the program - functionality has been crippled.\nThe program has to exit...")
            quit()
        #end IOError except 
    #end update_balance method

    #deposit method - put money into account
    def deposit(self, value):
        """Deposit money into account."""
        new_bal = self.update_balance(value,0)
        return new_bal
    #end deposit method

    #transfer method - give money to another account
    def transfer(self, value):
        """Transfer money from account into another."""
        new_bal = self.update_balance(value,1)
        return new_bal
    #end transfer method

    #withdraw - take money from account
    def withdraw(self, value):
        """Withdraw money from account."""
        new_bal = self.update_balance(value,1)
        return new_bal
    #end withdraw method

#end AccountClass

#AccountSaving class (subclass of Account)
class AccountSaving(Account):
    """Subclass of Account --> is account type of Saving"""

    def __init__(self, acc_id, acc_custName, acc_iban, acc_bal, acc_type="Saving"):
        """Intializes AccountSaving Attributes"""
        Account.__init__(self, acc_id, acc_custName, acc_iban, acc_bal)
        self.acc_type = acc_type
        pass
    #end __init__ method

    def __str__(self):
        """Represent Customer Instance as String"""
        return "Account ID: {} - IBAN: {} - Balance: {} - Type: {}".format(self.acc_id, self.acc_iban, self.acc_bal, self.acc_type)
    #end __str__ method

    #create saving account
    def account_s_create(self,file="accounts.txt"):
        """Creates record of saving account inside required file."""
        #opening and writing file
        try:
            #open accounts.txt
            file_open = open(file, "a")
            #string for new account record
            account_saving = "AccID:" + self.acc_id + "; - " + "CustAcc:" + self.acc_custName + "; - " + "IBAN:" + self.acc_iban + "; - " + "BAL:" + self.acc_bal + "; - " + "AccType:" + self.acc_type + ";ENDED;\n"
            #add new account record
            file_open.write(account_saving)
            #close file
            file_open.close()
        #should the file fail to open
        except IOError:
            print("A critical error has occurred in the program - functionality has been crippled.\nThe program has to exit...")
            quit()
        #end IOError except
    #end account_s_create method

    #delete saving account
    def account_s_delete(self,file="accounts.txt"):
        """Deletes record of saving account inside required file."""
        #search parameters
        start = "AccID:"
        middle = str(self.acc_id)
        end = ";"
        search = str(start + middle + end)
        #open and write to file
        try:
            #open file to read
            file_open = open(file, "r")
            #save lines
            lines = file_open.readlines()
            #run through lines for specific record
            for line in lines:
                #will return 0 when a match is found
                result = line.find(search)
                #when match found
                if(result == 0):
                    #save line
                    save_line = line
                    #break loop
                    break
                #end if statement
            #end for loop
            #open file to write
            file_open_two = open(file, "w")
            #run through saved lines
            for line in lines:
                #write back to line if it doesn't match the record being deleted
                if line != save_line:
                    #write line
                    file_open_two.write(line)
                #end if statement
            #end for loop
            #close files
            file_open.close()
            file_open_two.close()
            #tell user account has been deleted
            return "Account has been deleted.\n"
        #should the file fail to open
        except IOError:
            print("A critical error has occurred in the program - functionality has been crippled.\nThe program has to exit...")
            quit()
        #end IOError except
    #end account_s_delete method

#end AccountSaving class

#AccountChecking class (also subclass of Account)
class AccountChecking(Account):
    """Subclass of Account --> is account type of Checking"""

    def __init__(self, acc_id, acc_custName, acc_iban, acc_bal, acc_type="Checking"):
        """Intializes AccountChecking Attributes"""
        Account.__init__(self, acc_id, acc_custName, acc_iban, acc_bal)
        self.acc_type = acc_type
    #end __init__ method

    def __str__(self):
        """Represent Customer Instance as String"""
        return "Account ID: {} - IBAN: {} - Balance: {} - Type: {}".format(self.acc_id, self.acc_iban, self.acc_bal, self.acc_type)
    #end __str___ method

    #create checking account
    def account_c_create(self, file="accounts.txt"):
        """Creates record of account inside required file."""
        #open and write to file
        try:
            #open accounts.txt
            file_open = open(file, "a")
            #string for new account record
            account_checking = "AccID:" + self.acc_id + "; - " + "CustAcc:" + self.acc_custName + "; - " + "IBAN:" + self.acc_iban + "; - " + "BAL:" + self.acc_bal + "; - " + "AccType:" + self.acc_type + ";ENDED;\n"
            #add new account record
            file_open.write(account_checking)
            #close file
            file_open.close()
        #should the file fail to open
        except IOError:
            print("A critical error has occurred in the program - functionality has been crippled.\nThe program has to exit...")
            quit()
        #end IOError except
    #end account_c_create method

    #delete checking account
    def account_c_delete(self,file="accounts.txt"):
        """Deletes record of account inside required file."""
        #search parameters
        start = "AccID:"
        middle = str(self.acc_id)
        end = ";"
        search = str(start + middle + end)
        #open and write to file
        try:
            #open file to read
            file_open = open(file, "r")
            #save lines
            lines = file_open.readlines()
            #run through lines for specific record
            for line in lines:
                #will return 0 when a match is found
                result = line.find(search)
                #when match found
                if(result == 0):
                    #save line
                    save_line = line
                    #break loop
                    break
                #end if statement
            #end for loop
            #open file to write
            file_open_two = open(file, "w")
            #run through saved lines
            for line in lines:
                #write back to line if it doesn't match the record being deleted
                if line != save_line:
                    #write line
                    file_open_two.write(line)
                #end if statement
            #end for loop
            #tell user account has been deleted
            file_open.close()
            file_open_two.close()
            return "Account has been deleted.\n"
        #should the file fail to open
        except IOError:
            print("A critical error has occurred in the program - functionality has been crippled.\nThe program has to exit...")
            quit()
        #end IOError except
    #end account_s_delete method

#end AccountChecking class

#Transaction class
class Transaction:
    """This class acts a template for transaction records / objects."""

    def __init__(self, trans_id, trans_iban, trans_date, trans_desc):
        """Intializes Transaction Attributes"""
        self.trans_id = trans_id
        self.trans_iban = trans_iban
        self.trans_date = trans_date
        self.trans_desc = trans_desc
    #end __init__ method

    def __str__(self):
        """Represent Customer Instance as String"""
        return "Transaction ID: {} - {} - Note: {}".format(self.trans_id,self.trans_date,self.trans_desc)
    #end __str__ method

    #takeNote - transaction records
    def take_note(self, file="accountsTransactions.txt"):
        """Writes new transaction record to the required file."""
        #open and write to file
        try:
            #open accounts.txt
            file_open = open(file, "a")
            #string for new transaction record
            trans_record = "TransID:" + self.trans_id + "; - " + "IBAN:" + self.trans_iban + "; - " + "Date:" + self.trans_date + "; - " + "Description:" + self.trans_desc + ";ENDED;\n"
            #add new account record
            file_open.write(trans_record)
            #close file
            file_open.close()
        #should the file fail to open
        except IOError:
            print("A critical error has occurred in the program - functionality has been crippled.\nThe program has to exit...")
            quit()
        #end IOError except
    #end takeNote method

#end Transaction class

#bank management system class
def BankManagementSystem():

    ###############################
    # RECORD SEARCH FUNCTIONALITY #
    ###############################
    #searchSub - this is used to find a particular variable within the file
    def search_sub(data, index_begin, index_end, index_add):
        #where to start the search
        start = data.index(index_begin)
        #where to end the search
        end = data.index(index_end)
        #set where to start - example: CustID --> start is location of C and index_add is used to skip past D
        index_start = start + index_add
        #set where to end
        index_end = end
        #pull data (substring) from record
        final_result = data[index_start:index_end]
        #return result
        return final_result
    #end searchSub function
    #obtainRecord - this function obtains a record from the text files and splits the variables into a list
    def obtain_record(this_record, type):
        #customer record
        if(type == 0):
            #search parameters
            cust_param_begin = ["CustID:","CustAcc:","CustPass:","CustName:","CustAge:","CustEmail:","CustPhone:","CustAddress:"]
            cust_param_end = ["; - CustAcc:","; - CustPass:","; - CustName:","; - CustAge:","; - CustEmail","; - CustPhone:","; - CustAddress:",";ENDED;"]
            cust_param_length = [7,8,9,9,8,10,10,12]
            #record list template
            record = ["ID","Username","Password","Name","Age","Email","Phone","Address"]
            #run through columns
            for i in range(0,8):
                param_one = cust_param_begin[i]
                param_two = cust_param_end[i]
                param_three = cust_param_length[i]
                #search for variable in column
                record[i] = search_sub(this_record, param_one, param_two, param_three)
            #end for loop
            #return the list of variables from the record
            return record
        #end if statement
        #account record
        elif(type == 1):
            #search parameteres
            acc_param_begin = ["AccID:","CustAcc:","IBAN:","BAL:","AccType:"]
            acc_param_end = ["; - CustAcc:","; - IBAN:","; - BAL:","; - AccType:",";ENDED;"]
            acc_param_length = [6,8,5,4,8]
            #record list template
            record = ["ID","Username","IBAN","Balance","Type"]
            #run through columns
            for i in range(0,5):
                param_one = acc_param_begin[i]
                param_two = acc_param_end[i]
                param_three = acc_param_length[i]
                #search
                record[i] = search_sub(this_record, param_one, param_two, param_three)
            #end for loop
            #return the list of variables from the record
            return record
        #end else if statement
        #transaction record
        elif(type == 2):
            #search parameters
            trans_param_begin = ["TransID:","IBAN:","Date:","Description:"]
            trans_param_end = ["; - IBAN:","; - Date:","; - Description:",";ENDED;"]
            trans_param_length = [8,5,5,12]
            #record list template
            record = ["ID","IBAN","Date","Description"]
            for i in range(0,4):
                #search parameters
                param_one = trans_param_begin[i]
                param_two = trans_param_end[i]
                param_three = trans_param_length[i]
                #search
                record[i] = search_sub(this_record, param_one, param_two, param_three)
            #end for loop
            #return the list of variables from the record
            return record
        #end else if statement
        #unknown error
        else:
            #tell user an error has occurred
            print("\nAn error has occurred.\n")
        #end else statement
    #end obtainRecord

    #############################################
    # SYSTEM START - PART 1 - INSTANCE CREATION #
    #############################################
    #create instance for every customer
    def create_cust_instances():
        #list of instances
        cust_instances = []
        #read file
        try:
            #open file
            customers = open("customers.txt", "r")
            #run through list of customer records
            for line in customers:
                #obtain record variabes
                record = obtain_record(line,0)
                #create customer instance
                cust_instances.append(Customer(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]))
            #end for loop
            customers.close()
        #should the file fail to open
        except IOError:
            print("A critical error has occurred in the program - functionality has been crippled.\nThe program has to exit...")
            quit()
        #end IOError except
        #return list of customer instances
        return cust_instances
    #end create_cust_instances function
    #create instance for every account
    def create_acc_instances():
        #list of instances
        acc_instances = []
        #read file
        try:
            #open file
            accounts = open("accounts.txt", "r")
            #run through list of account records
            for line in accounts:
                #obtain record variables
                record = obtain_record(line,1)
                #check if saving account
                if(record[4] == "Saving"):
                    #create saving account instance
                    acc_instances.append(AccountSaving(record[0],record[1],record[2],record[3]))
                #end if statement
                #check if checking account
                if(record[4] == "Checking"):
                    #create checking account instance
                    acc_instances.append(AccountChecking(record[0],record[1],record[2],record[3]))
                #end if statement
            #end for loop
            #close file
            accounts.close()
        #should the file fail to open
        except IOError:
            print("A critical error has occurred in the program - functionality has been crippled.\nThe program has to exit...")
            quit()
        #end IOError except
        #return list of account instances
        return acc_instances
    #end create_acc_instances function
    #create instance for every transaction
    def create_trans_instances():
        #list of instances
        trans_instances = []
        #read file
        try:
            #open file
            transactions = open("accountsTransactions.txt", "r")
            #run through list of transaction records
            for line in transactions:
                #obtain record variables
                record = obtain_record(line,2)
                #create transaction instance
                trans_instances.append(Transaction(record[0],record[1],record[2],record[3]))
            #end for loop
            #close file
            transactions.close()
        #should the file fail to open
        except IOError:
            print("A critical error has occurred in the program - functionality has been crippled.\nThe program has to exit...")
            quit()
        #end IOError except
        #return list of transaction instances
        return trans_instances
    #end create_trans_instances function
    #persistent memory - create instances upon system start and store them in lists
    #these will be used throughout program instead of accessing the file for better security
    c_inst = create_cust_instances()
    a_inst = create_acc_instances()
    t_inst = create_trans_instances()

    #################
    # REQUIRED DATA #
    #################
    #generate_iban --> this is used to generate an iban for new accounts
    def generate_iban():
        #in real life --> this part of the iban is made up of a sort code and account number
        #will just randomly generate for the sake of simplicity
        code = randrange(10000000000000, 99999999999999)
        #(IE --> Ireland) @@@ (29 --> Check Code) @@@ (TUDG --> TUD Grangegorman Identifier)
        #IE29TUDG..............
        iban = "IE29TUDG" + str(code) 
        length = len(a_inst)
        #check to see if iban is already in use --> highly unlikely
        for i in range(0,length):
            #if it is
            if a_inst[i].acc_iban == iban:
                #restart the function and generate again
                generate_iban()
            #end if statement
        #end for loop
        #return iban number for account creation
        return iban
    #end generate_iban function
    #days_passed --> this is used to calculate how many days have passed for transaction requirements
    def days_passed(date_of_trans):
        #string for date format
        date_format = "%Y-%m-%d"
        #get todays date and store in string
        today_date = str(date.today())
        #datetime objects to be used in calculation
        x = datetime.strptime(today_date, date_format)
        y = datetime.strptime(date_of_trans, date_format)
        #calculate number of days
        result = x - y
        #return number of days since transaction occurred
        return result.days
    #end days_passed function
    
    #############
    # MAIN CODE #
    #############
    #customer_menu - this shows the user their options regarding their accounts once they have logged --> choosing an account allows for further options
    def customer_menu(user):
        #run menu until option chosen
        while True:
            #print options
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(
                #display current user as well
                "Logged in as:",
                c_inst[user].__str__(),
                "\n"
                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                "\n"
                "1: View Accounts\n"
                "2: Select Account\n"
                "3: Create Account\n"
                "4: Delete Account\n"
                "5: Log Out"
            )
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #take user input for option selection
            print("Enter Option: ")
            select_option = str(input())
            #view accounts - 1
            if(select_option == "1"):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #call account view function
                account_view(user)
            #end if statement
            #select account - 2
            if(select_option == "2"):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #call account select function
                account_select(user)
            #end if statement
            #create account - 3
            elif(select_option == "3"):
                #call account create function
                account_create(user)
            #end elif statement
            #delete account - 4
            elif(select_option == "4"):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #call account delete function
                account_delete(user)
            #end elif
            #logout - 5
            elif(select_option == "5"):
                #restart function
                BankManagementSystem()
            #end elif
            #invalid option
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #tell user they have entered an invalid option
                print("You have entered an invalid option. Please try again!\n")
            #end else
        #end while
    #end customer_menu function

    #account_view - user can view their accounts
    def account_view(user):
        #find number of account instances
        check = 1
        #display title for accounts
        print("Accounts:\n")
        #loop for running through accounts
        for i in range(0,len(a_inst)):
            #if saving account belongs to user
            if(a_inst[i].acc_custName == c_inst[user].cust_acc and a_inst[i].acc_type == "Saving"):
                #display info with method
                print(a_inst[i].__str__())
                check = 0
            #end if statement
            #if checking account belongs to user
            elif(a_inst[i].acc_custName == c_inst[user].cust_acc and a_inst[i].acc_type == "Checking"):
                #display info with method
                print(a_inst[i].__str__())
                check = 0
            #end elif statement
        #end for loop
        #no accounts yet associated with customer
        if(check == 1):
            #error message and return
            print("No accounts created yet.\nReturning to menu...")
            customer_menu(user)
        #end else statement
        customer_menu(user)
    #end account_view function

    #account_select - user can select account details to view from here
    def account_select(user):
        #check variable
        check = 0
        #find number of account instances
        length = len(a_inst)
        #display title for accounts
        print("Accounts:\n")
        #loop for running through accounts
        for i in range(0,length):
            #if saving account belongs to user
            if(a_inst[i].acc_custName == c_inst[user].cust_acc and a_inst[i].acc_type == "Saving"):
                #display info with method
                print(a_inst[i].__str__())
                #activate check
                check = 1
            #end if statement
            #if checking account belongs to user
            elif(a_inst[i].acc_custName == c_inst[user].cust_acc and a_inst[i].acc_type == "Checking"):
                #display info with method
                print(a_inst[i].__str__())
                #activate check
                check = 1
            #end elif statement
        #end for
        #if check completed
        if(check == 1):
            invalid = 0
            #prompt for user input for account selection
            print("Enter Account ID: ")
            option = str(input())
            #run through accounts again
            for i in range(0,len(a_inst)):
                if(a_inst[i].acc_id == option and a_inst[i].acc_custName == c_inst[user].cust_acc):
                    #call account menu function
                    account_menu(user, i)
                #end if statement
                #if an invalid option has been entered
                else:
                    invalid = 1
                #end else statement
            #end for look
            if(invalid == 1):
                #error message and return
                print("You have entered an invalid option.\nReturning to menu...")
                customer_menu(user)
        #end if statement
        #no accounts yet associated with customer
        else:
            #error message and return
            print("No accounts created yet.\nReturning to menu...")
            customer_menu(user)
        #end else statement
    #end account_select function
    #account_create - user can create new accounts from here
    def account_create(user):
        #ask the customer which account they wish to create
        print("Create:\n1: Savings?\n2: Checking?\n")
        print("Enter Option: ")
        #take user input for option
        option = str(input())
        #create savings account
        if(option == "1"):
            #latest account id
            acc_id_new = len(a_inst) + 1
            acc_id_new = str(acc_id_new)
            #generate iban
            iban = generate_iban()
            #create account instance
            a_inst.append(AccountSaving(acc_id_new,c_inst[user].cust_acc,iban,"0"))
            #find index in list of instances
            index_create = int(acc_id_new) - 1
            #call method to add record of saving account to file
            a_inst[index_create].account_s_create()
            #call account menu
            account_menu(user, index_create)
        #end if statement
        #create customer account
        elif(option == "2" and int(c_inst[user].cust_age) >= 18):
            #latest account id
            acc_id_new = len(a_inst) + 1
            acc_id_new = str(acc_id_new)
            #generate iban
            iban = generate_iban()
            #create account instance
            a_inst.append(AccountChecking(acc_id_new,c_inst[user].cust_acc,iban,"0"))
            #find index in list of instances
            index_create = int(acc_id_new) - 1
            #call method to add record of saving account to file
            a_inst[index_create].account_c_create()
            #call account menu
            account_menu(user, index_create)
        #end elif statement
        #if below eighteen and trying to create checking account
        elif(int(c_inst[user].cust_age) < 18):
            #error message and return
            print("\nYou must be eighteen years of age to create a Checking Account.\nReturning to menu...")
            customer_menu(user)
        #end elif statement
        #invalid option entered
        else:
            #error message and return
            print("\nYou have entered an invalid option.\nReturning to menu...")
            customer_menu(user)
        #end else statement        
    #end account_create function

    #account_delete - deletes account from records
    def account_delete(user):
        #check variable
        check = 0
        #find number of account instances
        length = len(a_inst)
        #display title for accounts
        print("Accounts:\n")
        #loop for running through accounts
        for i in range(0,length):
            #if saving account belongs to user
            if(a_inst[i].acc_custName == c_inst[user].cust_acc and a_inst[i].acc_type == "Saving"):
                #display info with method
                print(a_inst[i].__str__())
                #activate check
                check = 1
            #end if statement
            #if checking account belongs to user
            elif(a_inst[i].acc_custName == c_inst[user].cust_acc and a_inst[i].acc_type == "Checking"):
                #display info with method
                print(a_inst[i].__str__())
                #activate check
                check = 1
            #end elif statement
        #end for
        #if check completed
        if(check == 1):
            invalid = 0
            #prompt for user input for account selection
            print("Enter Account ID: ")
            option = str(input())
            #run through accounts again
            for i in range(0,len(a_inst)):
                if(a_inst[i].acc_id == option and a_inst[i].acc_custName == c_inst[user].cust_acc and a_inst[i].acc_type == "Saving"):
                    #delete record in file
                    a_inst[i].account_s_delete()
                    #drop from list
                    a_inst.pop(i)
                    #return to customer menu
                    customer_menu(user)
                #end if statement
                elif(a_inst[i].acc_id == option and a_inst[i].acc_custName == c_inst[user].cust_acc and a_inst[i].acc_type == "Checking"):
                    #delete record in file
                    a_inst[i].account_c_delete()
                    #drop from list
                    a_inst.pop(i)
                    #return to customer menu
                    customer_menu(user)
                    #end if statement
                    #if an invalid option has been entered
                #end elif statement
            #end for loop
            #error message and return
            #else statement
            else:
                #error message and return
                print("Make sure to enter a valid option.\nReturning to menu...")
                customer_menu(user)
            #end else statement
        #end if statement
        #no accounts yet associated with customer
        else:
            #error message and return
            print("No accounts created yet.\nReturning to menu...")
            customer_menu(user)
        #end else statement
    #end account_delete

    #account_menu - user options regarding their account will be displayed here to choose from
    def account_menu(user, acc):
        while True:
            #display iban and account type of current account instance
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("IBAN: ", a_inst[acc].acc_iban)
            print("Account Type: ", a_inst[acc].acc_type)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #display menu
            print(
                "1: View Balance\n"
                "2: Deposit Money\n"
                "3: Transfer Money\n"
                "4: Withdraw Money\n"
                "5: View Transactions\n"
                "6: Return"
            )
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #take user input for menu option
            print("Enter Option: ")
            select_option = str(input())
            #view balance - 1
            if(select_option == "1"):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #call view balance function
                view_balance(user, acc)
            #deposit money - 2
            elif(select_option == "2"):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #call deposit money function
                deposit_money(user, acc)
            #end elif statement
            #transfer money - 3
            elif(select_option == "3"):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #call transfer money function
                transfer_money(user, acc)
            #end elif statement
            #withdraw money - 4
            elif(select_option == "4"):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #call withdraw money function
                withdraw_money(user, acc)
            #end elif statement
            #view_transactions
            elif(select_option == "5"):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #call withdraw money function
                view_transactions(user, acc)
            #end elif statement
            #return - 6
            elif(select_option == "6"):
                #call customer menu function
                customer_menu(user)
            #end elif statement
            #invalid option
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #display error to user
                print("You have entered an invalid option. Please try again!\n")
                account_menu(user, acc)
            #end else statement
        #end while loop
    #end account_menu

    #viewBalance - user can view their balance
    def view_balance(user,acc):
        #print balance
        print(a_inst[acc].balance())
        #call account menu function
        account_menu(user,acc)
    #end view_balance function

    #deposit_money - user can deposit money into their account
    def deposit_money(user,acc):
        #take user input for amount to deposit
        print("Enter Deposit Amount:")
        amount = str(input())
        #check that amount is number and has been entered
        if(amount.isnumeric() == True and len(amount) > 0 and int(amount) > 0):
            #get result
            result = a_inst[acc].deposit(amount)
            #transaction string
            trans_string = str(amount) + "EUR was deposited into your account resulting in a new balance of " + str(result) + "EUR."
            #transaction date
            trans_date = str(date.today())
            #trans id
            index = int(len(t_inst))
            trans_id = index+1
            trans_id = str(trans_id)
            #create transaction instance
            t_inst.append(Transaction(trans_id,a_inst[acc].acc_iban,trans_date,trans_string))
            #add transaction to records
            t_inst[index].take_note()
            #call view balance function
            view_balance(user,acc)
        #tell user to enter a valid menu
        else:
            #display error
            print("Please enter a valid number for your amount.\nReturning to menu...")
            #call account menu function
            account_menu(user,acc)
        #end else statement
    #end deposit_money function

    #transfer_money - user can transfer money to another account via IBAN
    def transfer_money(user,acc):
        credit_limit = -1000
        #take user input for amount to transfer
        print("Enter Transfer Amount:")
        amount = str(input())
        #take user input for account to transfer to
        print("Enter IBAN:")
        target = str(input())
        #check to make sure that account exists
        check_iban = 0
        send = 0
        #run through each account instance
        for i in range(0,len(a_inst)):
            #check that account exists and is not the current account
            if(a_inst[i].acc_iban == target and a_inst[acc].acc_iban != target):
                #confirm check
                send = i
                check_iban = 1
                #break loop
                break
            #end if statement
        #end for loop
        #check that amount is number and has been entered
        if(amount.isnumeric() == True and len(amount) > 0 and int(amount) > 0 and len(target) > 0 and check_iban == 1):
            #run through each transaction instance
            for i in range(0,len(t_inst)):
                #take transaction date
                check_one = t_inst[i].trans_date
                check_two = t_inst[i].trans_desc
                calc = int(amount)
                #get required results for checks
                result_one = int(days_passed(check_one))
                result_two = check_two.find("deducted")
                #make sure only one withdrawal / transfer can be made per month
                if(t_inst[i].trans_iban == a_inst[acc].acc_iban and result_one < 30 and result_two != -1 and a_inst[acc].acc_type == "Saving"):
                    #display error
                    print("You can only make one withdrawal / transfer every thirty days.\nReturning to menu...")
                    #call account menu function
                    account_menu(user,acc)
                    #break
                    break
                #end if
                #make sure there is enough money to make the transaction
                elif(t_inst[i].trans_iban == a_inst[acc].acc_iban and a_inst[acc].acc_type == "Saving" and (int((a_inst[acc].acc_bal)) - (calc)) <= 0):
                    #display error
                    print("Please make sure you have enough money in your account to complete the transaction.\nReturning to menu...")
                    #call account menu function
                    account_menu(user,acc)
                    #break loop
                    break
                #end elif
                #make sure there is enough money to make the transaction - credit limit
                elif(t_inst[i].trans_iban == a_inst[acc].acc_iban and a_inst[acc].acc_type == "Saving" and (int((a_inst[acc].acc_bal)) - (calc)) <= credit_limit):
                    #display error
                    print("Please make sure you have enough money in your account to complete the transaction.\nReturning to menu...")
                    #call account menu function
                    account_menu(user,acc)
                    #break loop
                    break
                #end elif    
                #end if statement
            #end for loop
            #get result
            amount = int(amount)
            amount_two = abs(amount)
            result = a_inst[acc].transfer(str(amount))
            result_two = a_inst[send].deposit(str(amount_two))
            #transaction string
            trans_string = str(amount) + "EUR was deducted from your account resulting in a new balance of " + str(result) + "EUR."
            trans_string_two = str(amount_two) + "EUR was transferred into your account resulting in a new balance of " + str(result_two) + "EUR."
            #transaction date
            trans_date = str(date.today())
            #transaction one
            index = int(len(t_inst))
            trans_id = index+1
            trans_id = str(trans_id)
            t_inst.append(Transaction(trans_id,a_inst[acc].acc_iban,trans_date,trans_string))
            t_inst[index].take_note()
            #transaction two
            index = int(len(t_inst))
            trans_id = index+1
            trans_id = str(trans_id)
            t_inst.append(Transaction(trans_id,a_inst[send].acc_iban,trans_date,trans_string_two))
            t_inst[index].take_note()
            #call view balance function
            view_balance(user,acc)
        #end if statement
        #tell user to enter a valid menu
        else:
            #display error
            print("Please enter a valid IBAN and amount of money to transfer.\nReturning to menu...")
            #call account menu function
            account_menu(user,acc)
        #end else statement
    #end transfer_money function

    #withdraw_money - user can withdraw money from their account
    def withdraw_money(user,acc):
        credit_limit = -1000
        #take user input for amount to transfer
        print("Enter Withdraw Amount:")
        amount = str(input())
        #check that amount is number and has been entered
        if(amount.isnumeric() == True and len(amount) > 0 and int(amount) > 0):
            #run through each transaction instance
            for i in range(0,len(t_inst)):
                #take transaction date
                check_one = t_inst[i].trans_date
                check_two = t_inst[i].trans_desc
                calc = int(amount)
                #get required results for checks
                result_one = int(days_passed(check_one))
                result_two = check_two.find("deducted")
                #make sure only one withdrawal / transfer can be made per month
                if(t_inst[i].trans_iban == a_inst[acc].acc_iban and result_one < 30 and result_two != -1 and a_inst[acc].acc_type == "Saving"):
                    #display error
                    print("You can only make one withdrawal / transfer every thirty days.\nReturning to menu...")
                    #call account menu function
                    account_menu(user,acc)
                    #break
                    break
                #end if
                #make sure there is enough money to make the transaction
                elif(t_inst[i].trans_iban == a_inst[acc].acc_iban and a_inst[acc].acc_type == "Saving" and (int((a_inst[acc].acc_bal)) - (calc)) <= 0):
                    #display error
                    print("Please make sure you have enough money in your account to complete the transaction.\nReturning to menu...")
                    #call account menu function
                    account_menu(user,acc)
                    #break loop
                    break
                #end elif
                #make sure there is enough money to make the transaction - credit limit
                elif(t_inst[i].trans_iban == a_inst[acc].acc_iban and a_inst[acc].acc_type == "Checking" and (int((a_inst[acc].acc_bal)) - (calc)) <= credit_limit):
                    #display error
                    print("This transaction will go over your credit limit.\nReturning to menu...")
                    #call account menu function
                    account_menu(user,acc)
                    #break loop
                    break
                #end elif  
                #end if statement
            #end for loop
            #get result
            result = a_inst[acc].withdraw(amount)
            #transaction string
            trans_string = str(amount) + "EUR was deducted from your account resulting in a new balance of " + str(result) + "EUR."
            #transaction date
            trans_date = str(date.today())
            #transaction one
            index = int(len(t_inst))
            trans_id = index+1
            trans_id = str(trans_id)
            t_inst.append(Transaction(trans_id,a_inst[acc].acc_iban,trans_date,trans_string))
            t_inst[index].take_note()
            #call view balance function
            view_balance(user,acc)
        #end if statement
        #tell user to enter a valid menu
        else:
            #display error
            print("Please enter a valid number to withdraw.\nReturning to menu...")
            #call account menu function
            account_menu(user,acc)
        #end else statement
    #end withdraw_money
    
    #view transactions - user can view all transactions to related account
    def view_transactions(user,acc):
        check = 0
        #run through transaction instances
        for i in range(0,len(t_inst)):
            #if ibans match eachother
            if(t_inst[i].trans_iban == a_inst[acc].acc_iban):
                print(t_inst[i].__str__())
                check = 1
            #end if statement
        #end for loop
        #check if a record has been founds
        if(check == 0):
            #print error
            print("No transaction yet made with this account.\nReturning to menu...")
        #end if statement
        #call menu
        account_menu(user,acc)    
    #end view_transactions

    #exit_system - ends program
    def exit_system():
        #tell user the system is now exiting
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("The system will now exit.\nThank You!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #quit program
        quit()
    #end exit_system function

    #register - user can register so that they can open their own bank accounts
    def register():
        #check var
        check = 0
        #take user input for their account
        print("\nEnter Username:")
        username = str(input())
        print("Enter Password:")
        password = str(input())
        print("Enter Firstname & Surname:")
        name = str(input())
        print("Enter Age:")
        age = str(input())
        print("Enter Email:")
        email = str(input())
        print("Enter Phone:")
        phone = str(input())
        print("Enter Address:")
        address = str(input())
        #check to make sure all fields are entered
        if(len(username) != 0 and len(password) != 0 and len(name) != 0 and len(age) != 0 and len(email) != 0 and len(phone) != 0  and len(address) != 0):
            #find number of customer instances
            num_of_cust = int(len(c_inst))
            #run through each customer instance
            for i in range(0, num_of_cust):
                #if a record is found
                if(username == c_inst[i].cust_acc):
                    #change check variable to one
                    check = 1
                    break
                #end if statement
            #end for loop
            #if there is a record with the entered username already
            if(check == 1):
                #error message and display menu
                error_message = "This username already exists.\n"
                error_menu(error_message, 1, 0)
            #end if statement
            #if the username is unique
            else:
                #registration checks
                #check if entered age is numeric
                check_one = age.isnumeric()
                #check if age is greater than or equal to 14 - youngest age to open at least one account type sindependently
                check_two = int(age)
                #check if phone number is numeric
                check_three = phone.isnumeric()
                #check if username and password at least six characters
                check_four = len(username)
                check_five = len(password)
                #check if email valid
                check_six = email.find('@')
                #if everything is valid
                if(check_one == True and check_two >= 14 and check_three == True and check_four >= 6 and check_five >= 6 and check_six != -1):
                    #calculate customer id
                    cust_id = num_of_cust + 1
                    cust_id = str(cust_id)
                    #append new customer to list of instances and create record
                    c_inst.append(Customer(cust_id,username,password,name,age,email,phone,address))
                    #calculate index
                    index_create = int(cust_id)
                    c_inst[index_create-1].register()
                    #call customer menu function and pass the current user instance
                    customer_menu(index_create-1)
                #if invalid age
                elif(check_one == False or check_two < 14):
                    #error message and display menu
                    error_message = "You must enter a valid age above fourteen.\n"
                    error_menu(error_message, 1, 0)
                #end elif statement
                #if phone invalid
                elif(check_three == False):
                    #error message and display menu
                    error_message = "You must enter a valid phone number.\n"
                    error_menu(error_message, 1, 0)
                #end elif statement
                #if invalid email
                elif(check_six == -1):
                    #error message and display menu
                    error_message = "Please make sure you enter an email address domain.\n"
                    error_menu(error_message, 1, 0)
                #end elif statement
                #if invalid username or passwords
                elif(check_four >= 6 or check_five >= 6):
                    #error message and display menu
                    error_message = "Please make sure your username and password are at least six characters.\n"
                    error_menu(error_message, 1, 0)
                #end elif statement
        #end if statement
        #if username is already taken
        else:
            #error message and display menu
            error_message = "Please make sure you enter all fields.\n"
            error_menu(error_message, 1, 0)
        #end else statement
    #end register function

    #login function - user must log in to access their account
    def login():
        #check var
        check = 0
        #take user input for login
        print("\nEnter Username:")
        username = str(input())
        print("Enter Password:")
        password = str(input())
        if(len(username) > 0 and len(password) > 0):
            #find number of customer instances
            num_of_cust = int(len(c_inst))
            #run through each customer instance
            for i in range(0, num_of_cust):
                #if there is a instance with this username
                if(username == c_inst[i].cust_acc):
                    #check tells that there is an account
                    check = 1
                    #if the password is valid
                    if(password == c_inst[i].cust_pass):
                        #login customer
                        print(c_inst[i].login())
                        #call customer menu function and pass id / name
                        customer_menu(i)
                    #end if statement
                    #if password is invalid
                    else:
                        #error message and display menu
                        error_message = "This password does not match the system.\n"
                        error_menu(error_message, 0, 0)
                    #end else statement
                #end if statement
            #end for loop
            #no account check
            if(check == 0):
                #error message and display menu
                error_message = "This account does not exist.\n"
                error_menu(error_message, 0, 0)
            #end if statement
        #end if statement
        #if nothing entered
        else:
            #error message and display menu
            error_message = "Make sure you enter something when asked.\n"
            error_menu(error_message, 0, 0)
        #end else statement
    #end login function

    ######################
    # ERROR MENU DISPLAY #
    ######################
    def error_menu(message,type,extra_arg):
        #login
        if(type == 0):
            #run until option is chosen
            while True:
                #tell user error message and give them options
                print(message)
                print("1: Try Again?\n2: Return to Start Menu")
                #take user input for option
                print("Enter Option: ")
                select_option = str(input())
                #restart login function - 1
                if(select_option == "1"):
                    #call login function
                    login()
                    break
                #end if statement
                #return to start menu - 2
                elif(select_option == "2"):
                    #call main function to restart
                    BankManagementSystem()
                    break
                #end elif statement
                #invalid option
                else:
                    #tell user they have entered an invalid option
                    print("You have entered an invalid option. Please try again!\n")
                #end else statement
            #end while loop
        #end if statement

        #register - user can enter information to register as new customer
        elif(type == 1):
            #run options until one is chosen
            while True:
                #tell user error message and give them options
                print(message)
                print("1: Try Again?\n2: Return to Start Menu")
                #take user input for option
                select_option = str(input())
                #restart registration - 1
                if(select_option == "1"):
                    #call register function
                    register()
                    break
                #end if statement
                #return to start menu - 2
                elif(select_option == "2"):
                    #call main function
                    BankManagementSystem()
                    break
                #end elif statement
                #invalid option
                else:
                    print("You have entered an invalid option. Please try again!\n")
                #end else statement
            #end while loop
        #end elif statement
    #end error_menu function

    #########################################
    # SYSTEM START - PART 2 - RUN INTERFACE #
    #########################################
    #run start menu in loop
    while True:
        #current number of users
        #print("Custs: ",len(c_inst))
        #current number of accounts
        #print("Accounts: ",len(a_inst))
        #current number of transactions
        #print("Trans: ",len(t_inst))
        #display options to user
        print("~~~~~~~~~~~~~~")
        print("Select:\n\n1: Login\n2: Register\n3: Exit\n~~~~~~~~~~~~~~\nEnter Option: ")
        #take user input for option
        login_register = str(input())
        #login - option 1
        if(login_register == "1"):
            #call login function
            login()
            break
        #end if statement
        #register - option 2
        elif(login_register == "2"):
            #call register function
            register()
            break
        #end elif statement
        #exit - option 3
        elif(login_register == "3"):
            #call exit function
            exit_system()
        #end elif statement
        #invalid option
        else:
            #tell user they have entered an invalid option
            print("Invalid Option!\n")
        #end else statement
    #end start menu

#end bank system

#call functions
#start bank system - program starts
BankManagementSystem()