from brownie import *
def main():
	dic={
		"from":'0x086EeB6CC95f7473dE475BC50b166264E65BD662',
		"to":'0xC1bCBe44ABBB1E2C8Ff793006a681C1b2C6b3E0e',
		"amount":"1"
		}
	def txn(dic):
		s=dic['from'].transfer(dic['to'],dic['amount']+' ether')
	# print("gas Price = {}".format(s.gas_price))
	# print("gas Limit = {}".format(s.gas_limit))
		return({"gas Price":s.gas_price,"gas Limit":s.gas_limit })
	print(txn(dic))