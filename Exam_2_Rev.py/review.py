import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Exam_2_Rev.py/cars_dataset(1).csv')

# print(df.columns)
#pd.set_option('display.max_columns',None)

brands = ['BMW','Audi','Mercedes']
newdf = df.query('Identification_Make == @brands')
newdf1 = newdf[['Identification_Make','Fuel_City_mpg','Fuel_Highway_mpg','Engine_Horsepower','Engine_Torque']]

agg_df = newdf1.groupby(by='Identification_Make').agg('describe')

# newdf1.plot.box(column='Fuel_Highway_mpg',by='Identification_Make')
# newdf1.plot.box(column='Engine_Torque',by='Identification_Make')
# newdf1.plot.box(column='Engine_Horsepower',by='Identification_Make')
# plt.show()

# correlation = df.corr(numeric_only=True)
# print(correlation)

describe = df['Identification_Make'].describe()
print(type(describe))