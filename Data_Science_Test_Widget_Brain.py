# -*- coding: utf-8 -*-
"""
Widget Brain Data Science Test

Each day, many vessels arrive in the Port of Rotterdam, served by some 
stevedore(s). For reporting purposes, local stakeholders require a monthly 
estimate of all transshipments (load & discharge activities) broken out into 
cargo types. Four cargo types have been identified (ore, coal, oil and 
petroleum), and vessels often carry a mixture of cargo types. For each vessel,
we would like a prediction of how much it carries of each cargo type. The data 
for this case is stored in ‘VesselData.csv’.

We'd like you to provide us with a Python script (or notebook) with the results
of your endeavors, well enriched with comments elaborating on the steps taken, 
even if they did not lead you anywhere, and try to motivate your actions as 
much as possible. We would like to understand the approach you have taken and 
your line of thought.
"""

# Importing the packages I need
import pandas as pd #dataframes
import numpy as np  #arrays
import csv #reading from cs files

# Creating a dataframe containing the information in VesselData.csv
vessel_data = pd.read_csv('VesselData.csv', index_col = 0)
# Printed the first 5 rows of the dataframe to check if all information is there
#print(vessel_data.head(5))

# For every vessel, we want a predicition of how much of each of the four loads is carrying in a month.
# It is difficult to come up with a predictive model, since data is not available for all months of the year;
# Entries for ata/atd cover from May to November. So to get a rough idea of what is the load in these months, 
# we create an Excel table that shows for every vessel how much of the four types of cargo has carried in a given month. 

# Output to the desired Excel
writer = pd.ExcelWriter('vessel_overview.xlsx')
writer.save()
writer.close()

# Collect all vesselIDs in a list
vessels = vessel_data['vesselid'].tolist()

# Removing duplicates from this list 
vessels = list(set(vessels))

# sheet 1: vessel loads in May (shown per vessel)
# These are the names of the columns we want to put into the dataframe corresponding the May loads
cols = [ 'May:ore', 'May:coal','May:oil', 'May:petroleum'] 
# We create the dataframe taking as index the unique vesselID and as columns the list of names above
vessels_May = pd.DataFrame(index = vessels, columns =cols) 

# We compute the total loads of ore, oil, coal and petroleum carried by every vessel in May

# We create boolean dataframe whose entries take value True if the date corresponds to May and False otherwise
vessel_data['may'] = '2017-05'== vessel_data['ata'].str[0:7] 

# Then we compute the total amount of oil/coal/ore/petoleum loaded or discharged by a given vessel in May
loads_ore_may = vessel_data[vessel_data['may']==True].groupby(['vesselid'])['discharge1','load1'].sum()
loads_coal_may = vessel_data[vessel_data['may']==True].groupby(['vesselid'])['discharge2','load2'].sum()
loads_oil_may = vessel_data[vessel_data['may']==True].groupby(['vesselid'])['discharge3','load3'].sum()
loads_petroleum_may = vessel_data[vessel_data['may']==True].groupby(['vesselid'])['discharge4','load4'].sum()



