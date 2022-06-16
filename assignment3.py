import pandas as pd
from csv import writer
#The table data can  scrape like this
df = pd.read_html('https://www.census.gov/quickfacts/losangelescitycalifornia')
#To save the scraped data as csv file
with open ('new.csv','w',encoding='utf8',newline='') as file:
    the_writer = writer(file)
    header = ('Estimated date','population')
    the_writer.writerow(header)
    the_writer.writerow(df)