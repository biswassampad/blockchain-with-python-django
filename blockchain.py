#initialize the blockchain list
blockchain = []

#Return the last value of the current blockchain
def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

#Returns the user input amont in float
def get_transaction_value():
    user_input = float(input('Your Transaction Amount Please : '))
    return user_input

#get the user choice of operation
def get_user_choice():
    user_input = input('Your Choice of Operation : ')
    return user_input

def print_blockchain_elements():
    #output the blockchain list to the console 
    for block in blockchain:
        print('outputting block')
        print(block)

def add_transaction(transaction_amount,last_transaction =[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

#loop for getting user choice and to choose operation
while True:
    print('Choose the Option carefully')
    print('1- Add a new transaction value')
    print('2- Print all the blockchain blocks')
    print('q- Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount,get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('You Input is invalid,Please pick a value from the list.')
    print('Choice Registered!!')
print('Done!!')