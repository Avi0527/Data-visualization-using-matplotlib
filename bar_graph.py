#A bar graph respresents data in the from of vertical or horizontal bars.it is useful to compare the quantities.
import matplotlib.pyplot as plt #for drawing the graph
import pandas as pd # for creating dataframe

empdata = {"empid":[1001,1002,1003,1004,1005,1006],
           "ename":["Ganesh Rao","Anil Kumar","Gaurav Gupta","Hema Chandra","Laxmi Prasanna","Anant Nag"],
           "sal":[10000,23000.50,18000.33,16500.50,12000.75,9999.99],
           "doj":["10-10-2000","3-20-2002","3-3-2002","9-10-2002","10-08-2000","9-9-1999"]}

#let us convert the empdata object into a dataframe object df
df = pd.DataFrame(empdata)
x = df['empid']
y = df['sal']

#we can draw the bar graph by calling bar() function of pyplot module
plt.bar(x,y,label='Employee data',color='red')

#we can display a label (or title) on X-axis and Y-axis using xlabel() and ylable) function 
plt.xlabel('Employee ids')
plt.ylabel('Employee salaries')

#we can provide company's title using title() function
plt.title('MICROSOFT INS')

plt.lagend()
plt.show()


