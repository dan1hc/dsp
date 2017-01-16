[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)
```python
from scipy import stats

avg = 178
dev = 7.7

norm_dist = stats.norm(loc=avg, scale=dev)
lower_bound = norm_dist.cdf(70*2.54)
upper_bound = norm_dist.cdf(73*2.54)

print(upper_bound-lower_bound)
```
```
This percentage: 0.342746837631
```
