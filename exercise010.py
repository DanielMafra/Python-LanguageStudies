wallet = float(input('How much money do you have in your wallet? U$'))
real = wallet / 0.19

print('With U${:.2f} you can buy R${:.2f}'.format(wallet, real))
