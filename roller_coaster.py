import pandas as pd
import matplotlib.pyplot as plt


# Load rankings data:
wooden_coaster = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_coaster = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(wooden_coaster.head())
print(steel_coaster.head())

# Number of roller coasters on each dataset
print('Number of wooden roller coasters: ' + str(len(wooden_coaster)))
print('Number of steel roller coasters: ' + str(len(steel_coaster)))

# Suppliers list for each roller coaster DataFrame
suppliers_wood = wooden_coaster.Supplier.unique()
suppliers_steel = steel_coaster.Supplier.unique()
list_wood = suppliers_wood.tolist()
list_steel = suppliers_steel.tolist()

# Generate list with different suppliers from both roller coaster DataFrames
suppliers = []
for supplier in list_wood:
    suppliers.append(supplier)
for supplier in list_steel:
  if supplier not in suppliers:
    suppliers.append(supplier)

# Number of different suppliers included in the rankings
print('The number of different suppliers included in the rankings is ' + str(len(suppliers))) 

# Generate a DataFrame showing the number of rankings per year
rank_by_year_wood = wooden_coaster.groupby('Year of Rank').Name.count().reset_index()
print(rank_by_year_wood)

# Subset one of the roller coasters DataFrames for a chosen park to find if there is any ranked roller coaster
ranked_roller = steel_coaster.loc[steel_coaster.Park == 'Cedar Point']
print(ranked_roller)

# Write a function to plot rankings over time for 1 roller coaster:
def one_coaster_plot(name, coaster_df, park_name):
  df = coaster_df[(coaster_df.Name == name) &(coaster_df.Park == park_name)]
  x_values = df['Year of Rank']
  y_values = df['Rank']
  
  ax = plt.subplot()
  ax.plot(x_values, y_values, color='orange')
  ax.set_yticks(range(1,len(y_values)))
  ax.invert_yaxis()
  plt.ylabel('Ranking')
  plt.xlabel('Year')
  plt.title('Ranking of ' + name)
  plt.show()

one_coaster_plot('El Toro', wooden_coaster, 'Six Flags Great Adventure')

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def two_coasters_plot(coaster_name1, coaster_name2, coaster_df, park_name1, park_name2):
  df1 = coaster_df[(coaster_df.Name == coaster_name1) & (coaster_df.Park == park_name1)]
  df2 = coaster_df[(coaster_df.Name == coaster_name2) & (coaster_df.Park == park_name2)]
  x1 = df1['Year of Rank']
  y1 = df1['Rank']
  x2 = df2['Year of Rank']
  y2 = df2['Rank']
  
  ax = plt.subplot()
  plt.plot(x1, y1)
  ax.plot(x2, y2)
  ax.invert_yaxis()
  ax.set_yticks(range(1, len(y1)))
  plt.ylabel('Ranking')
  plt.xlabel('Year')
  plt.title('Rankings of ' + coaster_name1 + ' and ' + coaster_name2)
  plt.legend([coaster_name1, coaster_name2])
  plt.show()

two_coasters_plot('El Toro','Boulder Dash', wooden_coaster, 'Six Flags Great Adventure', 'Lake Compounce')

plt.clf()

# write function to plot top n rankings over time here:
def top_roller_coasters(n, coaster_df):
  df = coaster_df[coaster_df['Rank'] <= n]
  
  ax = plt.subplot()
  # Iterate through each unique roller_coaster
  for roller_coaster in set(df.Name):
    roller_df = df[df.Name == roller_coaster]
    ax.plot(roller_df['Year of Rank'], roller_df['Rank'], label=roller_coaster, marker='o')
  
  ax.invert_yaxis()
  ax.set_yticks(range(1, n+1))
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.title('Roller Coasters in Top ' + str(n)  + ' Rankings')
  plt.legend()
  plt.show()

top_roller_coasters(3, wooden_coaster)

plt.clf()

# From Captain Coaster site load roller coaster data:
coaster_data = pd.read_csv('roller_coasters.csv')
print(coaster_data.head())

# Write a function to plot histogram of column values here:
def plot_coaster_hist(data, column):

  x = data[column].dropna()
# Remove outliers that skew the data from height column
  if column == 'height':
    df = data[data['height'] <= 140]
    x_val = df['height'].dropna()
    plt.hist(x_val)
  else:
    plt.hist(x)
  
  plt.xlabel(column.capitalize())
  plt.ylabel('Frequency')
  plt.title('Roller Coasters ' + column.capitalize() + ' Distribution')
  plt.show()
  
plot_coaster_hist(coaster_data, 'height')


plt.clf()

# Write a function to plot inversions by coaster at a park here:
def coaster_inversions(data, park_name):
  park_coasters = data[data.park == park_name]
  park_coasters = park_coasters.sort_values('num_inversions', ascending=False)

  x_val = park_coasters.name
  y_val = park_coasters.num_inversions.dropna()

  ax = plt.subplot()
  ax.bar(range(len(x_val)), y_val, color='purple')
  ax.set_xticks(range(len(x_val)))
  ax.set_xticklabels(x_val, rotation=90)
  plt.xlabel('Roller Coasters')
  plt.ylabel('Number of Inversions')
  plt.title('Number of Inversions per Roller Coaster at ' + park_name)  

  plt.show()

coaster_inversions(coaster_data, 'Walygator Parc')

plt.clf()
    
# Write a function to plot pie chart of operating status:
def operating_coaster_status(data):
  operating_coasters = data[data.status == 'status.operating'].name.count()
  closed_coasters = data[data.status == 'status.closed.definitely'].name.count()
  
  coasters = [operating_coasters, closed_coasters]
  plt.pie(coasters, labels=['Operating', 'Closed'] , colors=['lightgreen', 'coral'], autopct='%0.1f%%', shadow=True, explode=[0.1,0])
  plt.title('Status of Roller Coasters')
  plt.axis('equal')

  plt.show()
  
operating_coaster_status(coaster_data)

plt.clf()
  
# Write a function to create a scatter plot of any two numeric columns:
def scatter_plot(data, col1, col2):

  # Remove outliers that skew the data from the height column
  if col1 == 'height':
    df = data[data['height'] < 140]
    x_val = df['height']
    y_val = df[col2]
    plt.scatter(x_val, y_val, color='salmon')
  elif col2 == 'height':
    df = data[data['height'] < 140]
    y_val = df['height']
    x_val = df[col1]
    plt.scatter(x_val, y_val, color='salmon')
  else:
    x_val = data[col1]
    y_val = data[col2]
    plt.scatter(x_val, y_val, color='salmon')
 
  plt.xlabel(col1.capitalize())
  plt.ylabel(col2.capitalize())
  plt.title(col1.capitalize() + ' vs ' 
  + col2.capitalize() + ' of Roller Coasters')

  plt.show()

scatter_plot(coaster_data, 'height', 'speed')

plt.clf()

# Most popular roller coaster seating type
def popular_seating_type(data):

  # Find the rows in which seating_type is equal to 'na' and drop them:
  indices = data[data.seating_type == 'na'].index
  data.drop(indices, inplace=True)

  coasters = data.groupby('seating_type').name.count().reset_index()
  coasters = coasters.sort_values('name', ascending=False).rename(columns={'seating_type': 'seating_type','name': 'Count'}).reset_index(drop=True)

  x_val = range(len(coasters.seating_type))
  y_val = coasters.Count
  
  ax = plt.subplot()
  ax.bar(x_val, y_val, color='teal')
  ax.set_xticks(x_val)
  ax.set_xticklabels(coasters.seating_type, rotation=90)
  plt.xlabel('Seating Types')
  plt.ylabel('Number of Roller Coasters')
  plt.title('Roller Coasters\' Seating Type Popularity')

  plt.show()

popular_seating_type(coaster_data)

# Do different seating types result in higher/faster/longer roller coasters?
def plot_seating_type_graphs(data, col1, col2, col3):
  
  # Find the rows in which seating_type is missing and drop them:
  indices = data[data.seating_type == 'na'].index
  data.drop(indices, inplace=True)

  x = range(data.seating_type.nunique())
  y1 = []
  y2 = []
  y3 = []
  labels = []

  for seat_type in set(data.seating_type):
     coasters = data[data.seating_type == seat_type]
     val_1 = coasters[col1].dropna().mean()
     val_2 = coasters[col2].dropna().mean()
     val_3 = coasters[col3].dropna().mean()
     y1.append(val_1)
     y2.append(val_2)
     y3.append(val_3)
     labels.append(seat_type)

  fig = plt.figure(figsize=(8,10), tight_layout=True)
  gs = fig.add_gridspec(4, 4)

  ax1 = fig.add_subplot(gs[:2,:2])
  ax1.bar(x, y1, color='forestgreen')
  ax1.set_xticks(range(data.seating_type.nunique()))
  ax1.set_xticklabels(labels, rotation=90)
  ax1.set_ylabel(col1.capitalize())
  ax1.set_title('Average ' + col1.capitalize() + ' of Different Seating Types')

  ax2 = fig.add_subplot(gs[:2,2:])
  ax2.bar(x, y2, color='firebrick')
  ax2.set_xticks(range(data.seating_type.nunique()))
  ax2.set_xticklabels(labels, rotation=90)
  ax2.set_ylabel(col2.capitalize())
  ax2.set_title('Average ' + col2.capitalize() + ' of Different Seating Types')

  ax3 = fig.add_subplot(gs[2:4, 1:3])
  ax3.bar(x, y3, color='indigo')
  ax3.set_xticks(range(data.seating_type.nunique()))
  ax3.set_xticklabels(labels, rotation=90)
  ax3.set_ylabel(col3.capitalize())
  ax3.set_title('Average ' + col3.capitalize() + ' of Different Seating Types')

  plt.show()
  

plot_seating_type_graphs(coaster_data, 'height', 'speed', 'length')  

#Do roller coaster manufacturers have any specialties (do they focus on speed, height, seating_type, or inversions)?
def manufacturer_specialty(data, height, speed, inversions, seat):
  
  y1 = []
  y2 = []
  y3 = []
  y4 = []
  labels_1 = []
  labels_2 = []
  labels_3 = []
  labels_4 = []

  for manufacturer in set(data.manufacturer):
     df = data[data.manufacturer == manufacturer]
     # Set a threshold to each column values to limit the number of manufacturers
     # and reveal possible specialties
     val_1 = df[height].dropna().mean()
     if val_1 > 40:
        y1.append(val_1)
        labels_1.append(manufacturer)

     val_2 = df[speed].dropna().mean()
     if val_2 > 90:
        y2.append(val_2)
        labels_2.append(manufacturer)   

     val_3 = df[inversions].dropna().mean()
     if val_3 > 1:
        y3.append(val_3)
        labels_3.append(manufacturer)   

     val_4= df[seat].nunique()
     if val_4 > 2:
        y4.append(val_4)
        labels_4.append(manufacturer)   

  x1 = range(len(y1))
  x2 = range(len(y2))
  x3 = range(len(y3))
  x4 = range(len(y4))
  
  fig = plt.figure(figsize=(10,10), tight_layout=True)

  ax1 = fig.add_subplot(221)
  ax1.bar(x1, y1, color='magenta')
  ax1.set_xticks(x1)
  ax1.set_xticklabels(labels_1, rotation=90)
  ax1.set_ylabel(height.capitalize())
  ax1.set_title('Average ' + height.capitalize() + ' vs Manufacturers')
  
  ax2 = fig.add_subplot(222)
  ax2.bar(x2, y2, color='darkorange')
  ax2.set_xticks(x2)
  ax2.set_xticklabels(labels_2, rotation=90)
  ax2.set_ylabel(speed.capitalize())
  ax2.set_title('Average ' + speed.capitalize() + ' vs Manufacturers')

  ax3 = fig.add_subplot(223)
  ax3.bar(x3, y3, color='gold')
  ax3.set_xticks(x3)
  ax3.set_yticks(range(5))
  ax3.set_xticklabels(labels_3, rotation=90)
  ax3.set_ylabel('# of Inversions')
  ax3.set_title('Average Inversions vs Manufacturers')

  ax4 = fig.add_subplot(224)
  ax4.bar(x4, y4, color='mediumspringgreen')
  ax4.set_xticks(x4)
  ax4.set_xticklabels(labels_4, rotation=90)
  ax4.set_ylabel('# of Seating Types')
  ax4.set_title('Seating Types vs Manufacturers')
  
  plt.show()

manufacturer_specialty(coaster_data, 'height', 'speed', 'num_inversions', 'seating_type') 

# Do amusement parks have any specialties?
def park_specialty(data, height, speed, inversions, seat):

  y1 = []
  y2 = []
  y3 = []
  y4 = []
  labels_1 = []
  labels_2 = []
  labels_3 = []
  labels_4 = []

  for park in set(data.park):
     df = data[data.park == park]
     # Set a threshold to each column values to limit the number of parks
     # and reveal possible specialties
     val_1 = df[height].dropna().mean()
     if val_1 > 60:
        y1.append(val_1)
        labels_1.append(park)

     val_2 = df[speed].dropna().mean()
     if val_2 > 110:
        y2.append(val_2)
        labels_2.append(park)   

     val_3 = df[inversions].dropna().mean()
     if val_3 > 3:
        y3.append(val_3)
        labels_3.append(park)   

     val_4= df[seat].nunique()
     if val_4 > 4:
        y4.append(val_4)
        labels_4.append(park)   

  x1 = range(len(y1))
  x2 = range(len(y2))
  x3 = range(len(y3))
  x4 = range(len(y4))
  
  fig = plt.figure(figsize=(10,10), tight_layout=True)

  ax1 = fig.add_subplot(221)
  ax1.bar(x1, y1, color='tomato')
  ax1.set_xticks(x1)
  ax1.set_yticks(range(0,500,100))
  ax1.set_xticklabels(labels_1, rotation=90)
  ax1.set_ylabel(height.capitalize())
  ax1.set_title('Average ' + height.capitalize() + ' vs Parks')
  
  ax2 = fig.add_subplot(222)
  ax2.bar(x2, y2, color='darkgreen')
  ax2.set_xticks(x2)
  ax2.set_yticks(range(0,200,50))
  ax2.set_xticklabels(labels_2, rotation=90)
  ax2.set_ylabel(speed.capitalize())
  ax2.set_title('Average ' + speed.capitalize() + ' vs Parks')

  ax3 = fig.add_subplot(223)
  ax3.bar(x3, y3, color='navy')
  ax3.set_xticks(x3)
  ax3.set_yticks(range(0,10,3))
  ax3.set_xticklabels(labels_3, rotation=90)
  ax3.set_ylabel('# of Inversions')
  ax3.set_title('Average Inversions vs Parks')

  ax4 = fig.add_subplot(224)
  ax4.bar(x4, y4, color='slategrey')
  ax4.set_xticks(x4)
  ax4.set_yticks(range(0,8,2))
  ax4.set_xticklabels(labels_4, rotation=90)
  ax4.set_ylabel('# of Seating Types')
  ax4.set_title('Seating Types vs Parks')
  
  plt.show()
  plt.clf()

park_specialty(coaster_data, 'height', 'speed', 'num_inversions', 'seating_type')
