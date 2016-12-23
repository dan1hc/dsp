import pandas as pd

csv_path = '/home/ec2usr/ds/metis/mteisgh/prework/dsp/python/faculty.csv'

faculty_df = pd.read_csv(csv_path)

emails = pd.Series(faculty_df[' email'])

csv_path = '/home/ec2usr/ds/metis/mteisgh/prework/dsp/python/emails.csv'

emails.to_csv(csv_path, index=False)


