from bankcard import *
from authentication import *

#card_num_list = [4319153440215460, 4319550212629259, 4319327412228129]

#card_num = card_num_list[0]
auth = Authentication()
#card = BankCard(card_num)


# 1) Verify
def run_verify_card():
    card_num = input('Q.1\nEnter Card to verify validity: ')
    verify = auth.verify_card(card_num)
    print('\n(Q.1)\nCard No.: ', card_num)
    print("Validity: ", verify)

# 2) Vendor: Displaying Vendor information
def run_vendor():
    card_num = input('\nQ.2\nEnter card to display Vendor: ')
    card = BankCard(card_num)
    details = card.get_card_details()
    print('\n(Q.2)\n', details)

# 3) Calculate checksum
def run_checksum():
    first_portion = input('\nEnter first part of Card to determine Checksum: ')
    checksum = auth.get_checksum(first_portion)
    print('\n(Q.3)\nFirst card portion: ', first_portion)
    print("Checksum: ", checksum)

# 4) Generate random valid card
def run_generate_card():
    vendor = input('\nQ.4\nEnter Vendor to generate full card (eg: Visa, Mastercard, Discover, American Express: ')
    new_card = auth.generate_card(vendor)
    print("\n(Q.4)\nNew Card: ", new_card)
    print("Validity: ", auth.verify_card(new_card))
    print("Vendor Info: \n", BankCard(new_card).get_vendor(new_card))

def main():

    #1
    #run_verify_card()

    #2
   # run_vendor()

    #3
    #run_checksum()

    #4
    run_generate_card()

if __name__ == '__main__':
    main()