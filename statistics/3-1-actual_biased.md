[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
```python

import chap01soln
import thinkstats2
import thinkplot

responses = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(responses.numkdhh)

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

biased_pmf = BiasPmf(pmf, 'biased_pmf')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='class size', ylabel='PMF')

print(pmf.Mean())
print(biased_pmf.Mean())
```
```
pmf mean: 1.02420515504
biased_pmf mean: 2.40367910066
```
