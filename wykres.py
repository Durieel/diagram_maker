import matplotlib.pyplot as plt

# Define the macro nutrients ratios
labels = ['Białko', 'Tłuszcze', 'Węglowodany']
sizes = [20, 30, 50]  # These percentages are just examples and should be adjusted based on the specific diet.

# Create a pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#00A0A5','#EDE1DF','#EBACB7'])
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
