# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import pandas as pd

csv_path = '/home/ec2usr/ds/metis/mteisgh/prework/dsp/python/football.csv'

football_df = pd.read_csv(csv_path)

#print(football_df)

football_df['+/-'] = football_df['Goals']-football_df['Goals Allowed']

print(football_df['Team'][football_df['+/-'].map(lambda x: abs(x)) == min(football_df['+/-'].map(lambda x: abs(x)))].tolist()[0])

