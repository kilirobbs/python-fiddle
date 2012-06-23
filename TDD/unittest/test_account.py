from account import BankAccount
import unittest
 
class TestBankAccount (unittest.TestCase):
 
	def setUp(self):
		self.account = BankAccount (100)
 
	def testBankAccountDeposit(self):
		test_balance = 170
		self.account.deposit (70)	
		self.assertEqual(self.account.balance, test_balance)
 
	def testBankAccountWithdraw(self):
		test_balance = 30
		self.account.withdraw (70)
		self.assertEqual(self.account.balance, test_balance)
		self.account.withdraw (270)
		self.assertEqual(self.account.balance, 0)
 
	def testBankAccountInterest(self):
		test_balance = 108.5
		self.account.interest (8.5)
		self.assertEqual(self.account.balance, test_balance)
 
if __name__ == "__main__":
	unittest.main()