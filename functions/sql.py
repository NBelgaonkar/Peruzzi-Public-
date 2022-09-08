import psycopg2
from config import sqlhost, sqldatabase,sqlpassword
class database:
    def __init__(self):
    
        self.con = psycopg2.connect(
            host= sqlhost,
            database=sqldatabase,
            user=sqldatabase,
            password=sqlpassword
        )
        self.cur = self.con.cursor()
        
    def get(self, query):
        results = self.cur.execute(query)
        results = self.cur.fetchall()
        return results
    def addLoan(self,discord_id,loanname,loanamt):
        discord_id=str(discord_id)
        amt=int(loanamt)
        loanename=int(loanname)
        query=f"INSERT INTO Loans (discord_id, loanname, loanamt) VALUES ('{discord_id}','{amt}','{loanename}');"
        results = self.cur.execute(query)
        return results

    def close(self, commit=False) -> None:
        if commit == True:
            self.con.commit()
        self.cur.close()
        self.con.close()
