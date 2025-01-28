# کارت های بانکی

cards = []
class Card :
    def __init__(self, card_number, expiry_date, cvv2, card_holder, card_balance):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv2 = cvv2
        self.card_holder = card_holder
        self.card_balance = card_balance
        cards.append(self)

# ساخت چند شیء
card1 = Card("1234 5678 9101 1121", "07/05", "123", "Ali Hassanzadeh", 10000)
card2 = Card("2345 6789 1011 1213", "04/03", "456", "Amir Rooholamini", 3000)
card3 = Card("3456 7890 1121 3141", "08/11", "789", "Maryam Bagheri", 7500)
card4 = Card("4567 8901 1213 4151", "03/06", "101", "zahra khodadadi", 2000)

# حلقه برای چاپ اطلاعات کارت‌های بانکی که موجودی آن‌ها از 5000 تومان بیشتر است
for card in cards:
    if card.card_balance > 5000:
        print(f"Card Holder: {card.card_holder} , Card Number: {card.card_number} , Balance: {card.card_balance} Toman ")