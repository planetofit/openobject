#import os
# importing mplot3d toolkits, numpy and matplotlib
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining all 3 axis
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
 
c = x + y
ax.scatter(x, y, z, c = c)

# plotting
#ax.plot3D(x, y, z, 'green')
ax.set_title('3D line plot geeks for geeks')
plt.show()


# define two objects
#def zelda(x,y,z):


"""
def print_subscriptions():
    subscription_client = SubscriptionClient(credential)
    sub_list = subscription_client.subscriptions.list()
    column_width = 40

    print("Subscription ID".ljust(column_width) + "Display name")
    print("-" * (column_width * 2))
    for group in list(sub_list):
        print(f'{group.subscription_id:<{column_width}}{group.display_name}')


# Print all the subscriptions
#print_subscriptions()

# Loop each subscription id and print resources
subscription_ids = get_subscriptions_ids()
for sub_id in subscription_ids:
    list_virtual_machines(sub_id)
"""

#sample notebook
#https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

#live plot
#https://pythonprogramming.net/live-graphs-matplotlib-tutorial/
