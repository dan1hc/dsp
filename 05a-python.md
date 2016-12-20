# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> They're similar in that they are visually similar data storage recepticles, and dissimilar in that tuples are immutable while lists are not. Resultantly, tuples work (and are often quite useful) as keys in a dictionary and lists will raise errors. On the other hand, lists can easily be modified, whereas tuples (afaik) can only be created or deleted. Should also be noted that tuples use less memory than lists as a result of immutability as well.
---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A set is an iterable with no repeating elements, a list can have repeating elements. Additionally, like dictionaries, sets are implemented using hash tables which for these purposes means that testing for membership is not affected by the size of the iterable- the computer does not have to iterate through each element in a set (unlike a list) to determine membership. Consequently, membership testing is significantly faster with sets than with lists.

[row for row in csv] is an example of a list, and set([row for row in csv]) would contain each element (row) while excluding any duplicate instances.
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is an anonymous function and it allows you to quickly pass a function as an argument without formally def(ining) it. Incidentally I have an example of a lambda fx on the keys of a sorted dictionary sitting in my IDE right now; here is what it looks like:
```python
[new_item(v, a) for a, v in collections.OrderedDict(sorted(k.items(), key=lambda x: x[0])).items()]
```
where new_item is a function I needed to apply on a dictionary I needed ordered on its values.

I would also like to note that lambda functions are particularly useful in conjunction with pandas' map and apply methods i.e. df.apply(lambda x: x*8-4+x**2).

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> Comprehensions are the pythonic (and usually fastest, I believe) way to create iterables. map allows you to pass a function to every element in an iterable (creating another iterable if desired) and filter creates an iterable with every element of another iterable for which the function passed to filter returns true. Both of these methods can be accomplished without using map or filter via comprehensions. Examples:

```python
dans_list = [x+2 for x in row]
dans_map = list(map(lambda x: x+2, row))

dans_list = [x for x in row if (x**3)%1==0]
dans_filter = filter(lambda x: (x**3)%1==0, row))

dans_extra_comprehensive_list = [x+2 for x in row if (x**3)%1==0]
dans_extra_comprehensive_set = {x+2 for x in row if (x**3)%1==0}
dans_extra_comprehsnive_dict = {x: x+2 for x in row if (x**3)%1==0}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





