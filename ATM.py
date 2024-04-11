import mysql.connector
class DepositError(Exception):pass
class WithdrawError(Exception):pass
class InSuffFundError(Exception):pass
#bal=500.00  Global Variable
def connection():
	con = mysql.connector.connect(host="localhost",
								  user="root",
								  passwd="vittal1234",
								  database="vittalpy")
	return con
def  deposit():
	pamt = int(input("Enter UR Pin_NUMBER:"))
	namt=int(input("Enter UR Account_Number :"))
	damt=float(input("Enter UR Deposit  amount :")) # Possibility of generating ValueError(pure strs,alnums, symbols)
	if(damt<=0):
		raise DepositError
	else:
		v = connection()
		cur = v.cursor()
		cur.execute("SELECT balance FROM accounts WHERE account_number = {} AND pin = {}".format(namt,pamt))
		records = cur.fetchone()
		bal=0
		for val in records:
			bal = float(val) + damt
		print("\tUrAccount Number {} Credited with INR:{}".format(namt,damt))
		print("\tNow Current Balance after deposit in ur Account Number  {}  INR:{}".format(namt,bal))
		cur.execute("UPDATE accounts SET balance = {} WHERE account_number = {}".format(bal, namt))
		v.commit()

def  withdraw():
	v = connection()
	cur = v.cursor()
	pamt = int(input("Enter UR Pin_NUMBER:"))
	namt = int(input("Enter UR Account_Number :"))
	wamt=float(input("Enter UR Withdraw  amount :")) # Possibility of generating ValueError(pure strs,alnums, symbols)
	cur.execute("SELECT balance FROM accounts WHERE account_number = {} AND pin = {}".format(namt, pamt))
	records = cur.fetchone()
	bal = 0
	for val in records:
		bal = val
	if(wamt<=0):
		raise WithdrawError
	elif((wamt+500)>bal):
		raise InSuffFundError
	else:
		bal=float(bal)-wamt
		print("\tUrAccount Number {} Debited with INR:{}".format(namt,wamt))
		print("\tNow Current Balance  after withdraw in ur Account Number {} INR:{}".format(namt,bal))
		cur.execute("UPDATE accounts SET balance = {} WHERE account_number = {}".format(bal, namt))
		v.commit()

def  balenq():
	v = connection()
	cur = v.cursor()
	pamt = int(input("Enter UR Pin_NUMBER:"))
	namt = int(input("Enter UR Account_Number :"))
	cur.execute("SELECT balance FROM accounts WHERE account_number = {} AND pin = {}".format(namt, pamt))
	records = cur.fetchone()
	bal = 0
	for val in records:
		bal = val
	print("\tUr Balance in Account Number {} INR:{}".format(namt,bal))
def createacc():
	v = connection()
	cur = v.cursor()
	pamt = int(input("Enter UR New  Pin_NUMBER:"))
	namt = int(input("Enter UR  New Account_Number :"))
	name=input("Enter ur New Account_Holder_Name : ")
	tame = input("Enter ur New Account_type (Savings OR Checking) : ")
	bamt=float(input("Enter UR 1ST Deposit amount Should be above 1000 :"))
	if bamt>=1000:
		cur.execute("INSERT INTO accounts (account_number, account_holder_name, balance, pin, account_type) VALUES ({}, '{}', {}, {}, '{}')".format(
				namt, name, bamt, pamt, tame))
		v.commit()
		print("Successfully your account is created. Thank you for choosing our bank.(sir/mam)")
	else:
		print("PLS UR 1ST Deposit amount Should be 1000 above...")
def alldetails():
	pas=input("Enter password : ")
	if pas=="sbi123":
		v = connection()
		cur = v.cursor()
		cur.execute("select * from accounts ")
		print("*" * 50)
		colnames = cur.description
		for colname in colnames:
			print("\t{}".format(colname[0]), end="\t")
		print()
		print("*" * 50)
		records = cur.fetchall()
		for record in records:
			for val in record:
				print("\t{}".format(val), end="\t")
			print()
		print("*" * 50)
	else:
		print("u entered wrong password...!!! ")

def menu():
	print("*"*50)
	print("\tATM Operations OR Funds Transfer Flow")
	print("*"*50)
	print("\t1.Deposit")
	print("\t2.Withdraw")
	print("\t3.Bal Enq")
	print("\t4.Create New Acc ")
	print("\t5.Exit")
	print("\t6.Show all accounts details (only for bank Manager) ")
	print("*"*50)


#MAin
while(True):
	print()
	print()
	menu()
	print()
	print()
	try:
		ch=int(input("Enter Ur Choice:"))
		match(ch):

			case 1:
				try:
					deposit()
				except ValueError:
					print("Don't try to Deposit alnums,strs and symbols-try again")
			case 2:
				try:
					withdraw()
				except ValueError:
					print("Don't try to Withdraw alnums,strs and symbols-try again")

			case 3:balenq()
			case 4:
				try:
					createacc()
				except ValueError:
					print("Don't try to give alnums,strs and symbols-try again")
			case 5:
				print("Thx for using this program")
				break
			case 6:
				alldetails()

			case _:
				print("Ur Selection of Operation is wrong--try again")
	except ValueError:
		print("Don't Enter alnums,strs and symbols for Bank Transaction-try again")
	except DepositError:
		print("Don't try deposit -ve  and zero amount ")
	except WithdrawError:
		print("Don't try Withdraw -ve  and zero amount ")
	except InSuffFundError:
		print("Ur Account does not have Suff Funds----Read Python Notes")



