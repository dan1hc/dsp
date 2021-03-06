import pandas as pd
import collections
import sys

csv_path = '/home/ec2usr/ds/metis/mteisgh/prework/dsp/python/faculty.csv'

faculty_df = pd.read_csv(csv_path)

def dot_fix(w):
    if len(w)>2:
        if w != 'MPH':
            w = ''.join('.'.join([w[:2], w[2:], '']))
    return w
    
def re_dot(x):
    return ' '.join([dot_fix(w) for w in x.split()])

faculty_df[' degree'] = faculty_df[' degree'].apply(lambda x: str(x).replace('.', '').lstrip()).apply(re_dot)

def of_change(w):
    if w == 'is':
        w = 'of'
    return w
    
def is_fix(x):
    if 'is' in set(x.split()):
        x = ' '.join([of_change(w) for w in x.split()])
    return x

faculty_df[' title'] = faculty_df[' title'].apply(is_fix)

def get_first_name(x):
    new_x = str(x).rsplit(None, 2)[0]
    if '.' in new_x:
        new_x = str(x).rsplit(None, 1)[0]
    
    return new_x
    
def get_last_name(x):
    return str(x).rsplit(None, 1)[-1]

faculty_df['given_name'] = faculty_df['name'].map(get_first_name)
faculty_df['surname'] = faculty_df['name'].map(get_last_name)

#Q6 
faculty_dict = {}
for t in faculty_df.itertuples():
    k = t.surname
    v = [t._2, t._3, t._4]
    if k in faculty_dict:
        faculty_dict[k].append(v)
    else:
        faculty_dict[k] = [v]
        
#Q7
professor_dict = {(t.given_name, t.surname): [t._2, t._3, t._4] for t in faculty_df.itertuples()}

#Q8
surname_dict = collections.OrderedDict(sorted(professor_dict.items(), key=lambda x: x[0][1])).items()

q_dicts = {'q6': faculty_dict, 'q7': professor_dict, 'q8': surname_dict}

input_args = str(sys.argv[1])

br=0
for d in q_dicts[input_args]:
    try:
        print(d, q_dicts[input_args][d])
    except:
        print(d[0], d[1])
    br+=1
    if br>2:
        break

    
    