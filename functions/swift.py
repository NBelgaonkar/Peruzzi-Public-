import requests, json

from config import DUsername, DPassword

class swift_api:
    def __init__(self):
        self.log = requests.Session()
        self.log.post("https://swifttechnologies.tomsw.uk/login-send", {'username': DUsername,'password': DPassword,'submit': "Login"})
    
    def balance(self) -> str:
        data: dict = self.log.get("https://swifttechnologies.tomsw.uk/siteapis/vault?req=bal&type=personal").json()
        return "${:,.2f}".format(data['data']['cash'])
    
    def send(self, aaid: str, rss: str) -> str:
        data: dict = self.log.get(f"https://swifttechnologies.tomsw.uk/siteapis/vault?req=external&type=personal&recipient={aaid}&status=alliance&cash={rss}&food=0&aluminum=0&steel=0&munitions=0&gasoline=0&bauxite=0&iron=0&lead=0&uranium=0&oil=0&coal=0").json()
        return data["data"]

    def depositcode(self) -> str:
        data: dict = self.log.get("https://swifttechnologies.tomsw.uk/siteapis/vault?req=newdepcode&type=personal").json()
        return data['newcode']
    
    def transactions(self) -> str:
        data: dict = self.log.get('https://swifttechnologies.tomsw.uk/siteapis/vault?req=transactions&type=personal&max=12').json()['data']
        returndata: str = ''
        for i in range(0, len(data)):
            returndata += f'__**{data[i][2]}**__ ({"${:,.2f}".format(data[i][4])}) ({data[i][16]})\n'
        return returndata
    
    def logout(self):
        self.log.get("https://swifttechnologies.tomsw.uk/logout")