import discord
import json
import requests

from config import apikey


def getproject(nationid):
    nationid=str(nationid)
    pnwgql = f"https://api.politicsandwar.com/graphql?api_key={apikey}"
    query="{nations(id:"+nationid+"){data{uranium_enrichment_program bauxite_works iron_works emergency_gasoline_reserve arms_stockpile mass_irrigation}}}"
    projectreq= requests.post(pnwgql, json={"query": query})
    projectreq=projectreq.json()
    projectreqdata=projectreq["data"]
    projectreqnations=projectreqdata["nations"]
    projectreqdata2=projectreqnations["data"]
    projectvalues = projectreqdata2[0]
    return projectvalues
def taxcheck(taxid):
    taxid=str(taxid)
    pnwgql = f"https://api.politicsandwar.com/graphql?api_key={apikey}"
    query ="{nations(tax_id:"+taxid +" ){data{nation_name id cities{infrastructure,land coal_mine,oil_well,uranium_mine,lead_mine,iron_mine, bauxite_mine, farm, gasrefinery, aluminum_refinery,munitions_factory,steel_mill, police_station,hospital,recycling_center,subway,supermarket,bank, shopping_mall,stadium} }}}"
    taxreq = requests.post(pnwgql, json={"query": query})
    taxreq=taxreq.json()
    taxreq= taxreq["data"]
    taxreq = taxreq["nations"]
    taxreq = taxreq["data"]
    return taxreq
def needalum(imp, tf):
    if imp == 0:
        return 0
    elif tf == "False":
        finval = imp*3
        return finval
    else:
        finval=4.08*imp
        return finval
def needgas(imp, tf):
    if imp == 0:
        return 0
    elif tf == "False":
        finval = imp * 3
        return finval
    else:
        finval = 6 * imp
        return finval
def needmunitions(imp, tf):
    if imp == 0:
        return 0
    elif tf == "False":
        finval = imp * 6
        return finval
    else:
        finval = 8.04 * imp
        return finval
def needsteel(imp, tf):
    if imp == 0:
        return 0
    elif tf == "False":
        finval = imp * 3
        finval = imp * 3
        return finval
    else:
        finval = imp * 4.08
        finval = imp * 4.08
        return finval
def needs(taxbrack):
    taxbrack=int(taxbrack)
    taxreq = taxcheck(taxbrack)
    needs=[]
    for i in taxreq:
        nationid = i ["id"]
        i = i["cities"]
        i = i[0]
        bauxneeds = needalum(i["aluminum_refinery"], )
        oilneeds = needgas(i["gasrefinery"], )
        leadneeds =  needmunitions(i["munitions_factory"])
        ironneeds= needsteel(i["steel_mill"],)
        needs= [needs, [nationid, [f"iron: +{ironneeds}", f"baux: +{bauxneeds}", f"coal: +{ironneeds}", f"lead: +{leadneeds}",f"oil: +{oilneeds}"]]]
    print(needs)
needs(17040)
