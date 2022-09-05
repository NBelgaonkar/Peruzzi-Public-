import requests
from typing import Union

from config import apikey, botkey

class pnw_api:
    def pnwdepo(self, amt: Union[float, str]) -> str:
        note='"CDP"'
        pnwgql=f"https://api.politicsandwar.com/graphql?api_key={apikey}"
        headers= {

            'x-api-key': apikey,
            'x-bot-key': botkey

        }
        query='mutation{bankDeposit(money:'+str(amt)+',note:'+note+'){money}}'
        r = requests.post(pnwgql, json={"query": query}, headers=headers)
        r = r.json()
        if 'data' in r:
            rdata = r["data"]
            rbankdepo = rdata["bankDeposit"]
            money = rbankdepo["money"]
            return "Sucess"
        else:
            if 'errors' in r:
                return f"Failure: {r['errors'][0]['message']}"
            else:
                return "Failure: Unknown"

    def pnwsendswift(self, amt: Union[float, str], note: str) -> str:
        pnwgql=f"https://api.politicsandwar.com/graphql?api_key={apikey}"
        headers= {

            'x-api-key': apikey,
            'x-bot-key': botkey

        }
        query='mutation{bankWithdraw(receiver:7433, receiver_type:2,money:'+str(amt)+',note:"'+note+'"){money}}'
        r = requests.post(pnwgql, json={"query": query}, headers=headers)
        r=r.json()
        if 'data' in r:
            rdata=r["data"]
            rbankdepo=rdata["bankWithdraw"]
            money=rbankdepo["money"]
            return "Sucess"
        else:
            if 'errors' in r:
                return f"Failure: {r['errors'][0]['message']}"
            else:
                return "Failure: Unknown"

    def pnwsendnation(self, rec: Union[int, str], amt: Union[float, str], note: str) -> str:
        pnwgql=f"https://api.politicsandwar.com/graphql?api_key={apikey}"
        headers= {

            'x-api-key': apikey,
            'x-bot-key': botkey

        }
        query='mutation{bankWithdraw(receiver_type:1, receiver:'+str(rec)+',money:'+str(amt)+',note:"'+note+'"){money}}'
        r = requests.post(pnwgql, json={"query": query}, headers=headers)
        r=r.json()
        if 'data' in r:
            rdata=r["data"]
            rbankdepo=rdata["bankWithdraw"]
            money=rbankdepo["money"]
            return "Sucess"
        else:
            if 'errors' in r:
                return f"Failure: {r['errors'][0]['message']}"
            else:
                return "Failure: Unknown"