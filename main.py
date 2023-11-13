from create import insert
from read import read
from update import update
from delete import delete

ob=insert()
objread=read()
objupdate=update()
objdelete=delete()

print("-------------Bank Management System----------------")
print("For inserting data press 1:")
print("For reading data press 2:")
print("For updating data press 3:")
print("For deleting data press 4:")

opr=int(input("Please enter your operation:"))

def myopr():
    print("-----for personal details press 1------")
    print("-----for bank details press 2------    ")
    print("-----for transaction details press 3---")
    print("-----for account details press 4-------")
    var=int(input("Please select your table:"))
    if var==1:
        return 'personal_details'
    elif var==2:
        return 'bank_details'
    elif var==3:
        return 'transaction_details'
    elif var==4:
        return 'account_details'
    

if opr==1:
    h=myopr()
    if h=='personal_details':
        cid=int(input("Enter customer id:"))
        fname=input("Enter customer first name:")
        lname=input("Enter customer last name:")
        addr=input("Enter customer address:")
        phn=int(input("Enter customer phone number:"))
        adhar=input("Enter customer aadhar number:")
        pan=input("Enter customer pan number:")
        ob.personal_details(cid,fname,lname,addr,phn,adhar,pan)
    elif h=='bank_details':
        acn=int(input("Enter account number:"))
        cid=int(input("Enter customer id:"))
        ifsc=input("Enter ifsc code:")
        actype=input("Enter account type:")
        ob.bank_details(acn,cid,ifsc,actype)
    elif h=='account_details':
        acn=int(input("Enter account number:"))
        amount=int(input("Enter amount:"))
        closing_bal=int(input("Enter closing_bal:"))
        trnscnid=int(input("Enter transaction id:"))
        trnscntype=input("Enter transaction type:")
        ob.account_details(acn,amount,closing_bal,trnscnid,trnscntype)
    elif h=='transaction_details':
        trnscnid=int(input("Enter transaction id:"))
        sen_acc=int(input("Enter sender account number:"))
        rec_acc=int(input("Enter receiver account number:"))
        amount=int(input("Enter amount:"))
        method=input("Enter method of transaction:")
        ob.transaction_details(trnscnid,sen_acc,rec_acc,amount,method)

if opr==2: # user wanted to read the data
    j=myopr()
    cusid=int(input("Please enter customer id for fetching data:"))
    objread.specific_info(cusid,j)

if opr==3:
    j=myopr()
    cusid=int(input("Please enter customer id:"))
    colname=input("Please enter column name:")
    newvalue=input("Please enter new values:")
    objupdate.myupdate(j,colname,newvalue,cusid)

if opr==4:
    k=myopr()
    cusid=int(input("Enter the customer id to delete:"))
    objdelete.specific_del(k,cusid)






