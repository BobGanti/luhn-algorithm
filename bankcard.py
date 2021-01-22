from authentication import Authentication


class BankCard:
    def __init__(self, card_num):
        self.card_num = card_num
        self.vendor = self.get_vendor(self.card_num)

    def get_vendor(self, card_num):
        validity = Authentication().verify_card(card_num)
        if validity == 'Valid':
            first_digit = str(card_num)[0]
            industry = ''

            if first_digit == '1' or first_digit == '2':
                industry = 'Airline'
            elif first_digit == '3':
                industry = 'Travel & Entertainment'
                issuer = 'American Express'
            elif first_digit == '4' or first_digit == '5' or first_digit == '6':
                industry = 'Banking'
                if first_digit == '4':
                    issuer = 'Visa'
                elif first_digit == '5':
                    issuer = 'MasterCard'
                else:
                    issuer = 'Discover'
            return '\tIndustry: {0} \n\tIssuer: {1}'.format(industry, issuer)
        else:
            return "Invalid card has no Vendor"

    def get_card_details(self):
        return "CARD DETAILS\nCard No.: {0} \nVendor Info: \n{1}".format(self.card_num, self.vendor)

