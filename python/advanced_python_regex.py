import pandas as pd

csv_path = '/home/ec2usr/ds/metis/mteisgh/prework/dsp/python/faculty.csv'

faculty_df = pd.read_csv(csv_path)


# Q1 unique degrees and frequencies
def degree_fix(x):
    x = str(x)
    # drop .'s
    x = x.replace('.', '')
    
    if 'Ph' in x:
        ph_loc = x.find('Ph')
        ph_str = x[ph_loc:]
        d_loc = ph_str.find('D')
        new_x = ''.join([x[:ph_loc], 'PhD', x[d_loc+ph_loc+1:]])
    
    else:
        pass
    
    return x
    
faculty_df[' degree'] = faculty_df[' degree'].apply(degree_fix)

faculty_df['degree freq'] = faculty_df.groupby(' degree')[' degree'].transform('count')

uniques_df = faculty_df[[' degree', 'degree freq']].drop_duplicates(' degree')

print(uniques_df)

#Q2 titles
faculty_df['title freq'] = faculty_df.groupby(' title')[' title'].transform('count')

unique_titles_df = faculty_df[[' title', 'title freq']].drop_duplicates(' title')

print(unique_titles_df)

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




