# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if not count > 9:
        return 'Number of donuts: '+str(count)
    else:
        return 'Number of donuts: many'
        
print(donuts(8))
print(donuts(15))


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) < 2:
        new_string = ''
    else:
        new_string = s[:2]+s[-2:]
    return new_string

print(both_ends('monty python'))


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    first_char = s[0]
    def char_change(x):
        if x == first_char:
            return '*'
        else:
            return x
            
    new_str = s[0]+''.join([char_change(x) for x in s[1:]])
    return new_str
    
print(fix_start('anagramS'))


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    a_firsts = [e for e in a[:2]]
    a_firsts.extend([e for e in b[2:]])
    b_firsts = [e for e in b[:2]]
    b_firsts.extend([e for e in a[2:]])
    
    return ' '.join([''.join(b_firsts), ''.join(a_firsts)])
    
print(mix_up('octo', 'cat'))

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) < 3:
        return s
    else:
        if s[-3:] == 'ing':
            return s+'ly'
        else:
            return s+'ing'

print(verbing('verbing'))
print(verbing('verbs'))

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    not_loc = s.find('not')
    bad_loc = s.find('bad')
    if not_loc > bad_loc:
        return s
    else:
        return s[:not_loc]+'good'+s[bad_loc+3:]

print(not_bad('this is not at all bad.'))

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    def get_halves(s):
        front_end = int(len(s)/2+len(s)%2)
        front = s[:front_end]
        back = s[front_end:]
        return front, back
    
    a_halves = (get_halves(a))
    b_halves = (get_halves(b))
    
    return a_halves[0]+b_halves[0]+a_halves[1]+b_halves[1]
    
print(front_back('kitten', 'donut'))
