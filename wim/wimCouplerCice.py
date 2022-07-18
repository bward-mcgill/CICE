#import numpy as np
#import xarray as xr
from datetime import datetime, timedelta

def createListTs(year_init, month_init, day_init, sec_init, ts, nts):
   list_ts=""
   start_day=datetime(year=int(year_init), month=int(month_init), day=int(day_init), second=int(sec_init))

   for i in range(nts):
      new_day=start_day+timedelta(seconds=sec_init+i*ts)
      if i == 0:
         list_ts=list_ts+" "+str(new_day.year).zfill(4)+str(new_day.month).zfill(2)+str(new_day.day).zfill(2)+str(new_day.hour*3600).zfill(5)+" "+str(new_day.year).zfill(4)+str(new_day.month).zfill(2)+str(new_day.day).zfill(2)+str(new_day.hour*3600).zfill(5)
      else:
         list_ts=list_ts+" "+str(new_day.year).zfill(4)+str(new_day.month).zfill(2)+str(new_day.day).zfill(2)+str(new_day.hour*3600).zfill(5)   
   print(list_ts)


def createTimeCice(yyyy, mm, dd, sssss):
   day=datetime(year=yyyy, month=mm, day=dd)
   dayTs=day+timedelta(seconds=sssss)
   print(str(dayTs.year).zfill(4)+'-'+str(dayTs.month).zfill(2)+'-'+str(dayTs.day).zfill(2)+"-"+str(dayTs.hour*3600).zfill(5))

