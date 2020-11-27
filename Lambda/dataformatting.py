from datetime import date

today = date.today()
print("Today's date:", today.strftime("%Y%m%d"))

todaydate=today.strftime("%Y%m%d")

x = 'data/raw/marketdata/stockprice.csv'
filename =todaydate+'/'+x.split('/')[-1]
print(filename)



