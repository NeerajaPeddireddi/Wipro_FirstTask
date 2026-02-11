import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles
from scipy.constants import pt

# plt.plot([1,2,3],[4,5,6])
# plt.show()
#
# x=[1,2,3]
# y=[10,15,20]
# plt.plot(x,y)
# plt.show()
x=[1,2,3,4]
y=[10,20,25,30]
#
# plt.plot(x,y,marker="o",linestyle="--")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("Plot Title")
# plt.grid(True)
# plt.show()
#
# names=["A","B","C","D"]
# scores=[80,90,98,99]
# plt.bar(names,scores)
# plt.title("Bar Chart Title")
# plt.xlabel("Name")
# plt.ylabel("Score")
# plt.show()
#
# plt.barh(names,scores)
# plt.title("Horizantal Bar Chart Title")
# plt.show()
#
# plt.hist(scores,bins=5)
# plt.title("Histogram Title")
# plt.show()
#
# plt.scatter(x,y)
# plt.show()

labels=["Chrome","Firefox","Edge"]
sizes=[60,25,15]
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title("Pie Chart Title")
plt.show()