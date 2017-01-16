[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)
```python
import thinkstats2
import thinkplot
from random import random

random_nums = [random() for r in range(1000)]
random_pdf = thinkstats2.Pmf(random_nums)
thinkplot.Pmf(random_pdf)
thinkplot.Show(xlabel='num', ylabel='PDF')
random_cdf = thinkstats2.Cdf(random_nums)
thinkplot.Cdf(random_cdf)
thinkplot.Show(xlabel='num', ylabel='CDF')
```
```
Short answer: yes, the distribution is uniform.
```
