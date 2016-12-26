import pandas as pd
import collections

csv_path = '/home/ec2usr/ds/metis/mteisgh/prework/dsp/python/faculty.csv'

faculty_df = pd.read_csv(csv_path)

# Q1 unique degrees and frequencies
def dot_fix(w):
    if len(w)>2:
        if w != 'MPH':
            w = ''.join('.'.join([w[:2], w[2:], '']))
    return w
    
def re_dot(x):
    return ' '.join([dot_fix(w) for w in x.split()])

faculty_df[' degree'] = faculty_df[' degree'].apply(lambda x: str(x).replace('.', '').lstrip()).apply(re_dot)

degrees = []
for d in faculty_df[' degree']:
    for w in d.split():
        degrees.append(w)
        
print(collections.Counter(degrees))

#Q2 titles
def of_change(w):
    if w == 'is':
        w = 'of'
    return w
    
def is_fix(x):
    if 'is' in set(x.split()):
        x = ' '.join([of_change(w) for w in x.split()])
    return x

faculty_df[' title'] = faculty_df[' title'].apply(is_fix)
print(collections.Counter(faculty_df[' title'].tolist()))

#Q3 emails list
emails = faculty_df[' email']

print(emails.tolist())

#Q4 domains
def get_domain(x):
    start_loc = x.find('@')
    domain = x[start_loc+1:]
    return domain

unique_domains = set(emails.map(get_domain).tolist())

print(unique_domains)

domain_count = len(unique_domains)

print(domain_count)




