import discord
import json
import requests

from config import apikey

def getvalue():
    pnwgql = f"https://api.politicsandwar.com/graphql?api_key={apikey}"
    query="{tradeprices(first:1){data{coal	oil	uranium	lead	iron	bauxite	gasoline	munitions	steel	aluminum	food}}}"
    tradereq = requests.post(pnwgql, json={"query": query})
    tradereq=tradereq.json()
    tradereqdata= tradereq["data"]
    tradereqtradprices= tradereqdata["tradeprices"]
    tradereqdata2 = tradereqtradprices["data"]
    tradreqvalues=tradereqdata2[0]

    return tradreqvalues
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
def getbuild(nationid):
    nationid=str(nationid)
    pnwgql = f"https://api.politicsandwar.com/graphql?api_key={apikey}"
    query ="{nations(id:"+nationid +"){data{cities{infrastructure,land coal_mine,oil_well,uranium_mine,lead_mine,iron_mine, bauxite_mine, farm, gasrefinery, aluminum_refinery,munitions_factory,steel_mill, police_station,hospital,recycling_center,subway,supermarket,bank, shopping_mall,stadium}}}}"
    buildreq = requests.post(pnwgql, json={"query": query})
    buildreq=buildreq.json()
    buildreqdata=buildreq["data"]
    buildreqnations=buildreqdata["nations"]
    buildreqdata2=buildreqnations["data"]
    buildreqcities=buildreqdata2[0]
    buildreqcities2=buildreqcities["cities"]
    buildreqvalues=buildreqcities2[0]

    return buildreqvalues
def radiation():
    pnwgql = f"https://api.politicsandwar.com/graphql?api_key={apikey}"
    query ="{game_info{radiation{global} }}"
    gamereq = requests.post(pnwgql, json={"query": query})
    gamereq=gamereq.json()
    gamereqdata=gamereq["data"]
    game_info=gamereqdata["game_info"]
    radiation=game_info["radiation"]
    globalrad=radiation["global"]
    globalradval=0.01*globalrad
    returnrd= 1-globalradval
    if returnrd<0:
        return 0
    else:
        return returnrd
def cities(nationid):
    nationid = str(nationid)
    pnwgql = f"https://api.politicsandwar.com/graphql?api_key={apikey}"
    query = "{nations(id:"+nationid+"){data{num_cities}}}"
    cityreq = requests.post(pnwgql, json={"query": query})
    cityreq=cityreq.json()
    data=cityreq["data"]
    nations = data["nations"]
    data2 = nations["data"]
    city=data2[0]
    numcities=city["num_cities"]
    return numcities

def productionbonus(imp,cap):
    if imp==0:
        return 0
    else:
        bonus = (0.5*(imp-1))/(cap-1)
        return round(bonus*100,2)
def revbaux(imp,price):
    if imp==0:
        return 0
    else:
        totalbaux= imp*3*(1+productionbonus(imp,10)/100)
        bauxval = price*totalbaux
        finbauxval = bauxval -(1600*imp)
        return finbauxval
def revcoal(imp,price):
    if imp==0:
        return 0
    else:
        totalcoal=imp*3*(1+productionbonus(imp,10)/100)
        val = price * totalcoal
        fincoalval = val-(400*imp)
        return fincoalval
def revoil(imp,price):
    if imp==0:
        return 0
    else:
        total=imp*3*(1+productionbonus(imp,10)/100)
        val = price * total
        finval = val-(600*imp)
        return finval
def reviron(imp,price):
    if imp==0:
        return 0
    else:
        total=imp*3*(1+productionbonus(imp,10)/100)
        val = price * total
        finval = val-(1600*imp)
        return finval
def revlead(imp,price):
    if imp==0:
        return 0
    else:
        total=imp*3*(1+productionbonus(imp,10)/100)
        val = price * total
        finval = val-(1500*imp)
        return finval
def revuri(imp, price, tf):
    if imp==0:
        return 0
    elif tf=="False":
        total = (imp * 3 * (1 + productionbonus(imp, 5) / 100))/2
        val = price * total
        finval = val - (1600 * imp)
        return finval
    else:
        total=imp*3*(1+productionbonus(imp,5)/100)
        val = price * total
        finval = val-(1600*imp)
        return finval
def revfarm(imp,price, land,rad, tf):
    if imp==0:
        return 0
    elif tf=="False":
        total = (imp*(1 + productionbonus(imp, 20))*(land/500)*10)
        val = price * total*rad
        finval= val -(300*imp)
        return finval
    else:
        total = (imp * (1 + productionbonus(imp, 20)) * (land / 400) * 10)
        val = price * total *rad
        finval = val - (300 * imp)
        return finval
def revalum(imp, alum, baux, tf):
    if imp==0:
        return 0
    elif tf=="False":
        total=imp*9*(1+productionbonus(imp, 5)/100)
        val= alum*total
        finval=val-((2500*imp)+(3*baux))
        return finval
    else:
        total = imp * 12.24 * (1 + productionbonus(imp, 5) / 100)
        val = baux * total
        finval=val-((2500*imp)+(4.08*baux))
        return finval
def revgas(imp, gas,oil , tf):
    if imp==0:
        return 0
    elif tf=="False":
        total=imp*6*(1+productionbonus(imp, 5)/100)
        val= gas*total
        finval=val-((4000*imp)+(3*oil))
        return finval
    else:
        total = imp * 12 * (1 + productionbonus(imp, 5) / 100)
        val = gas * total
        finval=val-((4000*imp)+(6*oil))
        return finval

def revmunitions(imp, munis,lead , tf):
    if imp==0:
        return 0
    elif tf=="False":
        total=imp*18*(1+productionbonus(imp, 5)/100)
        val= munis*total
        finval=val-((3500*imp)+(6*lead))
        return finval
    else:
        total = imp * 24.12 * (1 + productionbonus(imp, 5) / 100)
        val = munis * total
        finval=val-((3500*imp)+(8.04*lead))
        return finval
def revsteel(imp, steel,coal, iron , tf):
    if imp==0:
        return 0
    elif tf=="False":
        total=imp*9*(1+productionbonus(imp, 5)/100)
        val= steel*total
        finval=val-((4000*imp)+(3*iron)+(3*coal))
        return finval
    else:
        total = imp * 12.24 * (1 + productionbonus(imp, 5) / 100)
        val = steel * total
        finval = val - ((4000*imp) + (4.08 * iron) + (4.08 * coal))
        return finval
def basepopulation(infra):
    basepop= infra*100
    return basepop
def population(basepop,disease,crime ):

    population=(basepop-((disease*basepop)/10)-max((crime/10)*basepop-25,0))
    return population
def populationden(basepop,land):
    popden = basepop/land
    return popden
def disease(build, popden,basepop):
    rawpolution = (build["coal_mine"]*12)+(build["oil_well"]*12)+(build["uranium_mine"]*12)+(build["lead_mine"]*12)+(build["iron_mine"]*12)+(build["bauxite_mine"]*12)+(build["farm"]*2)
    manupolution= (build["gasrefinery"]*32)+(build["aluminum_refinery"]*40)+(build["munitions_factory"]*32)+(build["steel_mill"]*40)
    civilpolution=(build["police_station"]*1)+(build["hospital"]*4)-((build["recycling_center"]*70)+(build["subway"]*45))
    compolution= (build["supermarket"]*0)+(build["bank"]*0)+(build["shopping_mall"]*5)+(build["stadium"]*5)
    polution=rawpolution+manupolution+civilpolution+compolution
    popden=int(popden)
    disease = ((((popden*popden) * 0.01) - 25) / 100) + (basepop / 100000) + (polution*0.5) - (build["hospital"]* 2.5)
    return disease
def com(build):
    com = (build["police_station"] * 3) + (build["hospital"] * 5) + ((build["recycling_center"] * 9) + (build["subway"] * 12))+(build["subway"]*8)
    return com
def crime(build,com, infra):
    t1=103 - com
    t2=int(t1)
    crime=(t2*t2 + (infra * 100))/(111111) -(build["police_station"]*2.5)
    return crime
def cityincome(build):
    comer = com(build)
    basepop = basepopulation(build["infrastructure"])
    build=build
    popden = populationden(basepop,build["land"])
    pop= population(basepop, disease(build,popden,basepop),crime(build,comer,build["infrastructure"]))
    Income = (((comer / 50) * 0.725) + 0.725) * pop
    return Income



def cityrevenue(nationid):
    prices=getvalue()
    projects=getproject(nationid)
    build=getbuild(nationid)
    baserev=cityincome(build)
    rawrev1= revcoal(build["coal_mine"],prices["coal"])+revoil(build["oil_well"],prices["oil"])+revuri(build["uranium_mine"],prices["uranium"],projects["uranium_enrichment_program"])
    rawrev2= revlead(build["lead_mine"],prices["lead"])+reviron(build["iron_mine"],prices["iron"])+revbaux(build["bauxite_mine"], prices["bauxite"])
    farmrev= revfarm(build["farm"],prices["food"],build["land"],radiation(),projects["mass_irrigation"])
    rawrev=rawrev1+rawrev2+farmrev
    manurev1= revgas(build["gasrefinery"],prices["gasoline"], prices["oil"],projects["emergency_gasoline_reserve"])+revalum(build["aluminum_refinery"],prices["aluminum"],prices["bauxite"],projects["bauxite_works"])
    manrev2= revmunitions(build["munitions_factory"],prices["munitions"],prices["lead"],projects["arms_stockpile"])+revsteel(build["steel_mill"],prices["steel"],prices["coal"],prices["iron"],projects["iron_works"])
    manrev= manrev2+manurev1
    totalcityrev= rawrev +manrev+baserev
    return totalcityrev

def nationrev(nationid):
    rev= cityrevenue(nationid)*cities(nationid)
    return rev
