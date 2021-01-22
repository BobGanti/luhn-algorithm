import random


class Authentication:
    def __init__(self):
        self.sum = 0

    def verify_card(self, card_num):
        total_even_i = 0
        total_odd_i = 0
        str_list = str(card_num)
        for i in range((len(str_list) - 1), -1, -1):
            if i % 2 == 0:
                num_even_i = int(str_list[i])
                num_even_i = num_even_i * 2
                if num_even_i > 9:
                    num_even_i = (num_even_i - 9)
                total_even_i += num_even_i
            else:
                total_odd_i += int(str_list[i])

        self.sum = total_even_i + total_odd_i
        if self.sum % 10 == 0:
            return "Valid"
        else:
            return "Invalid"

    def get_checksum(self, first_portion):
        first_portion = str(first_portion)
        valid_card_lenght = 16
        temp_card = self.generate_random((valid_card_lenght-1) - len(first_portion), first_portion)
        self.verify_card(int(temp_card))
        if self.sum % 10 == 0:
            checksum = 0
        else:
            checksum = 10 - (self.sum % 10)
        return checksum

    def generate_card(self, vendor):
        vendor = vendor.lower()
        print(vendor)
        if vendor == 'visa':
            first_digit = '4'
        elif vendor == 'mastercard':
            first_digit = '5'
        elif vendor == 'discover':
            first_digit = '6'
        count = 14
        if vendor == 'american express':
            first_digit = str(random.randint(1, 2))
            count = 13

        temp_card = self.generate_random(count, first_digit)
        checksum = self.get_checksum(temp_card)
        full_card = temp_card + str(checksum)
        return full_card

    def generate_random(self, count, first_digit):
        for x in range(count):
            other_digit = str(random.randint(0, 9))
            first_digit += other_digit
        return first_digit

