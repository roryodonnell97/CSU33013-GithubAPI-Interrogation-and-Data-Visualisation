import sqlite3 
import csv

connection = sqlite3.connect("table1.db") 
    
crsr = connection.cursor() 
   

sql_command = """SELECT * FROM table1"""  
crsr.execute(sql_command)
  
ans= crsr.fetchall()  
  

# Day Bar Chart
weekday = [['Country', 'Value'],
['Monday', 0],
['Tuesday', 0],
['Wednesday', 0],
['Thursday', 0],
['Friday', 0],
['Saturday', 0],
['Sunday', 0]]

x = 0
for i in ans:
    current_row = ans[x]
    current_weekday_int = current_row[3]
    weekday[int(current_weekday_int) + 1][1] += 1
    x += 1

csv.register_dialect('myDialect',
)
with open('C:/Users/Rory/Desktop/bar_chart_weekday_data.csv', 'wb') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in weekday:
        writer.writerow(row)

f.close()

# Hour Bar Chart

hour = [['Country', 'Value'],
['00:00', 0],
['01:00', 0],
['02:00', 0],
['03:00', 0],
['04:00', 0],
['05:00', 0],
['06:00', 0],
['07:00', 0],
['08:00', 0],
['09:00', 0],
['10:00', 0],
['11:00', 0],
['12:00', 0],
['13:00', 0],
['14:00', 0],
['15:00', 0],
['16:00', 0],
['17:00', 0],
['18:00', 0],
['19:00', 0],
['20:00', 0],
['21:00', 0],
['22:00', 0],
['23:00', 0]]

x = 0
for i in ans:
    current_row = ans[x]
    current_hour = current_row[4][0:2]
    if(current_hour[0] == '0'):
        current_hour = current_hour[1]
    hour[int(current_hour) + 1][1] += 1
    x += 1

csv.register_dialect('myDialect',
)
with open('C:/Users/Rory/Desktop/bar_chart_hour_data.csv', 'wb') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in hour:
        writer.writerow(row)

f.close()

# Day Histogram CSV 
csv.register_dialect('myDialect',
)
with open('C:/Users/Rory/Desktop/weekday_histogram_data.csv', 'wb') as f:
    writer = csv.writer(f, dialect='myDialect')
    writer.writerow(['price'])
    x = 0
    for row in ans:
        current_row = ans[x]
        current_weekday_int = current_row[3]
        writer.writerow([current_weekday_int])
        x += 1

f.close()



# All Scatter Plot CSV 

#                  Mon      Tues        Wed      Thurs      Fri       Sat       Sun
day = [['time', 'valueA', 'valueB' , 'valueC', 'valueD', 'valueE', 'valueF', 'valueG'],
[0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[2,0,0,0,0,0,0,0],
[3,0,0,0,0,0,0,0],
[4,0,0,0,0,0,0,0],
[5,0,0,0,0,0,0,0],
[6,0,0,0,0,0,0,0],
[7,0,0,0,0,0,0,0],
[8,0,0,0,0,0,0,0],
[9,0,0,0,0,0,0,0],
[10,0,0,0,0,0,0,0],
[11,0,0,0,0,0,0,0],
[12,0,0,0,0,0,0,0],
[13,0,0,0,0,0,0,0],
[14,0,0,0,0,0,0,0],
[15,0,0,0,0,0,0,0],
[16,0,0,0,0,0,0,0],
[17,0,0,0,0,0,0,0],
[18,0,0,0,0,0,0,0],
[19,0,0,0,0,0,0,0],
[20,0,0,0,0,0,0,0],
[21,0,0,0,0,0,0,0],
[22,0,0,0,0,0,0,0],
[23,0,0,0,0,0,0,0]]

x = 0
for i in ans:
    current_row = ans[x]
    current_weekday_int = current_row[3]
    current_hour = current_row[4][0:2]
    if(current_hour[0] == '0'):
        current_hour = current_hour[1]
    day[int(current_hour) + 1][int(current_weekday_int) + 1] += 1
    
    x +=1

csv.register_dialect('myDialect',
)
with open('C:/Users/Rory/Desktop/scatter_plot_data.csv', 'wb') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in day:
        writer.writerow(row)

f.close()

# 1st half Weekday Scatter plot

#                               Mon      Tues        Wed      Thurs  
weekday_1st_half = [['time', 'valueA', 'valueB' , 'valueC', 'valueD'],
[0,0,0,0,0],
[1,0,0,0,0],
[2,0,0,0,0],
[3,0,0,0,0],
[4,0,0,0,0],
[5,0,0,0,0],
[6,0,0,0,0],
[7,0,0,0,0],
[8,0,0,0,0],
[9,0,0,0,0],
[10,0,0,0,0],
[11,0,0,0,0],
[12,0,0,0,0],
[13,0,0,0,0],
[14,0,0,0,0],
[15,0,0,0,0],
[16,0,0,0,0],
[17,0,0,0,0],
[18,0,0,0,0],
[19,0,0,0,0],
[20,0,0,0,0],
[21,0,0,0,0],
[22,0,0,0,0],
[23,0,0,0,0]]

for i in range(25):
    for j in range(5):
        weekday_1st_half[i][j] = day[i][j]


csv.register_dialect('myDialect',
)
with open('C:/Users/Rory/Desktop/scatter_plot_weekday_1st_half.csv', 'wb') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in weekday_1st_half:
        writer.writerow(row)

f.close()

# 2nd half Weekday Scatter plot 

#                               Fri      Sat        Sun        
weekday_2nd_half = [['time', 'valueA', 'valueB' , 'valueC'],
[0,0,0,0],
[1,0,0,0],
[2,0,0,0],
[3,0,0,0],
[4,0,0,0],
[5,0,0,0],
[6,0,0,0],
[7,0,0,0],
[8,0,0,0],
[9,0,0,0],
[10,0,0,0],
[11,0,0,0],
[12,0,0,0],
[13,0,0,0],
[14,0,0,0],
[15,0,0,0],
[16,0,0,0],
[17,0,0,0],
[18,0,0,0],
[19,0,0,0],
[20,0,0,0],
[21,0,0,0],
[22,0,0,0],
[23,0,0,0]]

for i in range(1,25):
    for j in range(1,4):
        weekday_2nd_half[i][j] = day[i][j+4]


csv.register_dialect('myDialect',
)
with open('C:/Users/Rory/Desktop/scatter_plot_weekday_2nd_half.csv', 'wb') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in weekday_2nd_half:
        writer.writerow(row)

f.close()


    
connection.commit() 
   
connection.close() 



