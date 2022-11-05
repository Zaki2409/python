#COMPUND INTEREST
def compound_interest(principle,rate,time):

	
	Amount = principle * (pow((1 + rate / 100), time))
	CI = Amount
	print("Compound interest is", CI)

compound_interest(1, 10.25, 5)

