import matplotlib.pyplot as plt
import seaborn as sns
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.title('Monthly Sales - Line Chart')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)
plt.savefig('AssImg1_Q1.png')
plt.show()

sns.barplot(x=months,y=sales)
plt.title('Monthly Sales - Bar Plot')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)
plt.savefig('AssImg2_Q1.png')
plt.show()
