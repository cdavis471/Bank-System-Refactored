# Bank System Refactored

A bank management system created using Python using three external files to store all bank information. Initially created for an assignment, I was not happy with the final product overall. Having learned more since then, I now am better equipped to design this program better in line with the principles of object-oriented design. I will be refactoring the code to make it more efficient and clean in how it is designed, without affecting the current functionality while also fixing a couple of bugs that have been found.

# User Manual

Starting the program, you will be given the options to Login, Register or Exit:

###### Login: You must enter your credentials to access the program, meaning you enter your username and password before being let in.  
###### Register: If you do not have an account, you can enter your own details but there are requirements you must meet for the account to be created – enter all fields, username / password must be six characters long, email must include an @ symbol for the domain, phone number must be valid, you must be fourteen (at least) and your username has to be unique.  
###### Exit: This is to stop the program.  

After you login or register, you will be brought to your customer menu, which will display your name and id. From here you can select from five options:

###### View Accounts: This will display all bank accounts associated with your person.  
###### Select Account: Here you will be asked to select one account to continue forward with by selection of account id. If successful, you will be brought to a further menu.  
###### Create Account: Here you can create another bank account (only a savings account if you are below eighteen) that you can perform multiple actions with. There are two types: checking and saving.  
###### Delete Account: This will delete the instance (pop from list) and the record from the file depending on the account id you select.  
###### Log Out: This will log you out and you will be returned to the starting menu.  

After you have created or selected an account to move forward with, you have even more options to choose from. This menu will also display the account IBAN and type in case you forget. There is a credit limit of a thousand euro for checking accounts on transactions regarding their balance:

###### View Balance: This will allow the user to see the balance of their selected account.  
###### Deposit Money: This will take user input in order to input money into their selected account.  
###### Transfer Money: The user can enter an IBAN of another user on the system, alongside an amount, in order to transfer money to them. You can only do this or withdraw once every thirty days if on a saving account. You must also have enough money for it.  
###### Withdraw Money: The user can enter an amount to subtract from their current balance. You can only do this or transfer once every thirty days if on a saving account. You must also have enough money for it.  
###### Transaction Records: The user can select this and view all transaction records associated with the currently selected account.  
###### Return: This returns to the customer menu to allow the user to select another account.  

Every record has a unique ID regarding their respective information, be it a customer, bank account, or transaction. Search functions and other functions have been created to enhance the quality of the program, like the generate_iban function.
