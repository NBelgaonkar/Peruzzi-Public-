import datetime

class checktime:
  def turncheck():
    current_time= datetime.datetime.now()
    minuite= current_time.minuite
    if minuite in [58,59,0,1,2]:
      return ("Failuire: TurnChange")
    else:
      return("Success")
    
  
    
