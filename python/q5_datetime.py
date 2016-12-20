# Hint:  use Google to find python function

####a) 

import datetime

date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_1 = datetime.datetime.strptime(date_start, '%m-%d-%Y')
print(date_1)
date_2 = datetime.datetime.strptime(date_stop, '%m-%d-%Y')
print(date_2)

difference = (date_2-date_1).days
print(difference)

####b)  
date_start = '12312013'  

date_1 = datetime.datetime.strptime(date_start, '%m%d%Y')
print(date_1)

date_stop = '05282015'  

date_2 = datetime.datetime.strptime(date_stop, '%m%d%Y')
print(date_2)

difference = (date_2-date_1).days
print(difference)

####c)  
date_start = '15-Jan-1994'  

date_1 = datetime.datetime.strptime(date_start, '%d-%b-%Y')
print(date_1)

date_stop = '14-Jul-2015'  

date_2 = datetime.datetime.strptime(date_stop, '%d-%b-%Y')
print(date_2)

difference = (date_2-date_1).days
print(difference)
