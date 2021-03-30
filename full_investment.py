import datetime
import calendar
import math
import pandas as pd

x=int(input("Enter your package:"))

today=datetime.date.today()
print(today)
p=int(x/50)
print("the duplication need :{} cycles".format(p))
q=x*2+50
h=x+50

package=[]
daily_income=[]
n=[]
after=[]
today_s=[]

for i in range(h,q,50):
    package.append(i)
    y=(i*0.005)
    daily_income.append(y)
    z=(50/y)
    n.append(z)

for c in n:
    a=math.ceil(c)
    after.append(a)
    today+=datetime.timedelta(days=a)
    today_s.append(today)

g={'package':pd.Series(package),'daily_income':pd.Series(daily_income),'after':pd.Series(after),'On':pd.Series(today_s)}

df = pd.DataFrame(g)

print(df)