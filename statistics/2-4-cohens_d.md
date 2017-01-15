[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> ```python

import nsfg
import numpy as np

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

first_borns = live[live.birthord == 1]
siblings = live[live.birthord != 1]

def cohen(s1, s2):
    d = (s1.mean()-s2.mean()) / np.sqrt( (s1.count()*s1.var()+s2.count()*s2.var()) / (s1.count()+s2.count())  )
    return d
    
wgt_d = cohen(first_borns.totalwgt_lb, siblings.totalwgt_lb)
prg_d = cohen(first_borns.prglngth, siblings.prglngth)
print(wgt_d, prg_d)
```
