"""
the method to calculate the value after one year
"""
def calculate_apr(principal, interest_rate, years):
    i = 1
    value = 0.0
    while i <= years:
        value = value + principal * (1 + interest_rate)
        i+=1
    return value

while True:
#if the user enter invalid output then turn False, otherwise calculate the value after one year 
    try:
        principal = int(input('Enter principal: '))
        interest_rate = float(input('Enter interest rate: '))
        years = int(input('Enter years: '))
        break
    except ValueError:
        print('False')
print ('Value: ', calculate_apr(principal, interest_rate, years))    
  


      

