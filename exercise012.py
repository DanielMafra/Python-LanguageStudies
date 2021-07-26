price = float(input('What is the price of the product? U$'))
new = price - (price * 5 / 100)

print('The product that used to cost U${:.2f}, in the promotion with a discount 5%, will cost U${:.2f}.'.format(
    price, new))
