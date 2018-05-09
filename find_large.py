//Jennifer Nguyen
from pprint import pprint
from web3 import Web3, HTTPProvider, IPCProvider
web3= Web3 (HTTPProvider ("http://localhost:8545"))

def findLarge():
	for n in range (100000, 200000):
		b= int(web3.eth.getBlock(n).transactions)

def test2():
	for i in range (100000, 100003):
		b= (web3.eth.getBlock(i).transactions)
		for j in b:
			val= web3.eth.getTransaction (b).value
			for k in val:
				print (k)

	#txhash = web3.eth.getBlock (1788439).transactions[0]


#txhash = web3.eth.getBlock (n).transactions[]
#web3.eth.getTransaction (txhash).value


def ugh():
	for i in range (100000, 100500):
		b= (web3.eth.getBlock(i).transactions)
		if b== []:
			i=i+1
		for j in range :
			val= web3.eth.getTransaction (i).value #change b to i?
			print (val)


//1788439

b= (web3.eth.getBlock(1788439).transactions)

val= web3.eth.getTransaction (1788439).value[]

def ugh():
	for i in range (100000, 100500):
		b= (web3.eth.getBlock (i).transactions)
		if (b != []):
			val= web3.eth.getTransaction (i).value #change b to i?
			print (val)

b= (web3.eth.getBlock (1788439).transactions)

txhash = web3.eth.getBlock (1788439)
web3.eth.getTransaction (txhash)
web3.eth.getTransaction (txhash).value

def test2():
	for i in range (100000, 100010):
		trans=(web3.eth.getBlock (i).transactions)
		print (trans)
		for j in range (0, (len(trans)-1)):
			block=trans[j]
			print (blocks)
			for k in block:
				val=web3.eth.getTransaction (block).value
				print (val)


'''		


		val= web3.eth.getTransaction (i).value


#web3.eth.getTransaction (1788439).value
b= (web3.eth.getBlock (1788439).transactions)
web3.eth.getTransaction (b).value


web3.eth.getBlock (1788439).transactions[0]
'0xb3aaa91e903af2fe7dbf1a88f9ec6ce8880978f40bf0dc37e22694c15e4353e3'

txhash = web3.eth.getBlock (1788439).transactions[0]
web3.eth.getTransaction (txhash)
>>> web3.eth.getTransaction (txhash).value
0

100137

trans=web3.eth.getBlock(100137).transactions
web3.eth.getBlock(199999).transactions


val=trans[0]

web3.eth.getTransaction (block).value

'''
