#import modules
import pandas  # for dataframes
import matplotlib.pyplot as plt # for plotting graphs
import seaborn as sns # for plotting graphs
#% matplotlib inline
data=pandas.read_csv('HR_comma_sep.csv')
# print(data.tail())
left = data.groupby('left')
fulldata = data
# print(left.mean())

left_count=data.groupby('left').count()

# plt.bar(left_count.index.values, left_count['satisfaction_level'])
# plt.xlabel('Employees Left Company')
# plt.ylabel('Number of Employees')
# plt.show()

# print(left_count)
# print(left_count.index.values)
# print(fulldata.index.values.tolist()) 
# print(list(fulldata.index.values))
# print(data.left.value_counts())

# print(fulldata['satisfaction_level'])

# num_projects=data.groupby('number_project').count()
# plt.bar(num_projects.index.values, num_projects['satisfaction_level'])
# plt.xlabel('Number of Projects')
# plt.ylabel('Number of Employees')
# plt.show()



# plt.bar(fulldata.index.values, fulldata['number_project'])
# plt.xlabel('full of Projects')
# plt.ylabel('full of Employees')
# plt.show()

features=['number_project','time_spend_company','Work_accident','left', 'promotion_last_5years','Departments ','salary']
fig=plt.subplots(figsize=(10,15))
for i, j in enumerate(features):
    plt.subplot(4, 2, i+1)
    plt.subplots_adjust(hspace = 1.0)
    sns.countplot(x=j,data = data)
    plt.xticks(rotation=90)
    plt.title("No. of employee")


plt.show()