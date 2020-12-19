#Same visual with results from rolling two differenct dice at once

#File to visualize results of dice roll
from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

#Create two dice, one has 10 sides
dice_1 = Dice()
dice_2 = Dice(10)

#Roll dice and store results in a list
results = []
for roll_num in range(50000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)
    
#Analyze results of dice roll
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#Put results into visual bar chart
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'Frequency of result'}

my_layout = Layout(title='Result of rolling a six sided and a ten sided dice', xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename ='d6d10.html')