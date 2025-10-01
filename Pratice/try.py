# import matplotlib.pyplot as plt
# import numpy as np
# x = np.arange( 0, 3 * np.pi, 1)
# y = np.sin(x)
# plt.plot(x,y,color = 'green',linestyle = 'dashed',linewidth = 3,
#          marker = 'o',markerfacecolor = 'blue',markersize = 12)
# plt.ylabel('y-axis')
# plt.xlabel('x-axis')
# plt.plot(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# x =[1,2,3,4]
# y= [1,2,3,4]
# plt.plot(x,y,color = 'green',linestyle = 'dashed',linewidth = 3,
#          marker = 'o',markerfacecolor = 'blue',markersize = 12)
# plt.ylabel('y-axis',fontsize = 16)
# plt.xlabel('x-axis',fontsize = 16)
# # plt.plot(x,y)
# plt.title('my first graph')
# plt.show()

# a  = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# c = max(a,b)
# print(c)


a = int(input("Enter a number:"))
fact = 1
for i in range(1,a+1):
    fact = fact*i
print(f"Factorial of {a} is {fact}")


