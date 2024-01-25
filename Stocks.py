#Christopher Buzaid
#CS 175L
#stocks

Purchase_Commission = float(input('Enter commission rate percentage (ex 0.03) on stock purchase: '))
Selling_Commission = float(input('Enter commission rate percentage (ex. 0.03) on stock sale: '))
Num_Shares = float(input('Enter number of shares purchased: '))
Sold_Shares = float(input('Enter number of shares sold: '))
Purchase_Price = float(input('Enter purchase price per share: '))
Sell_Price = float(input('Enter sell price per share: '))

Amount_Paid = Purchase_Price * Num_Shares
paidCommission = Purchase_Commission * Amount_Paid
Amount_Sold = Sell_Price * Sold_Shares
saleCommission =  Selling_Commission * Amount_Sold
totalCommission = paidCommission + saleCommission
Profit = ((Amount_Sold - Amount_Paid) - totalCommission)

print('')
print(f'Amount paid for the stock: ${Amount_Paid:,.2f} ')
print(f'Commission paid on the purchase: ${paidCommission:,.2f}')
print(f'Amount the stock sold for: ${Amount_Sold:,.2f}')
print(f'Commission paid on the sale: ${saleCommission:,.2f}')
print(f'Profit (or loss if negative): ${Profit:,.2f}')
      
