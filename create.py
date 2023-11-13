# installed library mysql-connector-python
import mysql.connector

# creating class
class insert:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Akshu@mysql1",
                database = "bank"
                )

    def personal_details(self,cid,fname,lname,addr,phn,adhar,pan):
        cur=self.conn.cursor() # creating cursor
        cur.execute(f"INSERT INTO PERSONAL_DETAILS VALUES({cid},'{fname}','{lname}','{addr}',{phn},'{adhar}','{pan}')")
        self.conn.commit()
        print("-----------------Personal information has been saved successfully-------------------")   
    
    def bank_details(self,acn,cid,ifsc,actype):
        cur=self.conn.cursor()
        cur.execute(f"INSERT INTO BANK_DETAILS VALUES({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("------------------Bank details has been saved successfully----------------------------")

    def transaction_details(self,trnscnid,sen_acc,rec_acc,amount,method):
        cur=self.conn.cursor()
        cur.execute(f"INSERT INTO TRANSACTION_DETAILS VALUES({trnscnid},{sen_acc},{rec_acc},{amount},'{method}')")
        self.conn.commit()
        print("-------------------Transaction details has been saved successfully------------------")

    def account_details(self,acn,amount,closing_bal,trnscnid,trnscntype):
        cur=self.conn.cursor()
        cur.execute(f"INSERT INTO ACCOUNT_DETAILS VALUES({acn},{amount},{closing_bal},{trnscnid},'{trnscntype}')")
        self.conn.commit()
        print("--------------------Account details has been saved successfully-----------------")
