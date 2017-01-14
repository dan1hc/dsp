# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    new_words = [w for w in words if len(w)>=2 and w[0]==w[-1]]
    word_count = len(new_words)
    return word_count
    
print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    x_strings = sorted([w for w in words if w[0]=='x'])
    other_strings = sorted([w for w in words if w[0]!='x'])
    x_strings.extend(other_strings)
    return x_strings

print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    sorted_tuples = sorted(tuples, key=lambda x: x[-1])
    return sorted_tuples

print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))

def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    new_nums = []
    last_num = None
    for num in nums:
        if num == last_num:
            pass
        else:
            new_nums.append(num)
        last_num = num
        
    return new_nums

print(remove_adjacent([3, 2, 3, 3, 3]))

import string
def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    output = []
    count = int((len(list1)+len(list2))/2)+1
    i=0
    while i < count:
        try:
            entry1 = list1[i]
            entry2 = list2[i]
            if string.ascii_lowercase.index(entry1[0]) < string.ascii_lowercase.index(entry2[0]):
                output.append(entry1)
                output.append(entry2)
            else:
                output.append(entry2)
                output.append(entry1)
        except:
            try:
                output.append(list1[i])
            except:
                output.append(list2[i])
        i+=1	
    
    return output
#    list1.extend(list2)
#    return sorted(list1)
    
print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
