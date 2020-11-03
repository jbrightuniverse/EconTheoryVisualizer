import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111, projection='3d')
plt.xlabel("Output")
plt.ylabel("Quarter")
demands = []
years = []
rates = []
ycounter = 1
ybig = 1961
with open("demand.txt") as f1:
  with open("interest.txt") as f2:
    with open("investment.txt") as f3:
      for i in range(238):
        investment = f3.readline().replace("\n", "")
        interest = f2.readline().replace("\n", "")
        demand = f1.readline().replace("\n", "")
        interest = float(interest)/100
        slope = -1*(int(investment)/interest)
        ival = -1*slope*int(demand)+interest
        demands.append(0)
        rates.append(ival)
        for x in range(3):
          years.append(ybig + 0.1 * ycounter)
        ycounter += 1
        if ycounter == 5:
          ycounter = 1
          ybig+= 1
        demands.append(int(demand))
        rates.append(interest)
        yval = (-1*interest+slope*int(demand))/slope
        demands.append(yval)
        rates.append(0)

ax.plot(demands, years, zs = rates)

fig.show()

# https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610010401

# https://www150.statcan.gc.ca/n1/pub/11-210-x/2010000/t098-eng.htm#T098FN1

#https://wowa.ca/bank-of-canada-interest-rate#overnight-rate-changes


"""
How to cite: Statistics Canada. Table 36-10-0104-01 Gross domestic product, expenditure-based, Canada, quarterly (x 1,000,000)
DOI: https://doi.org/10.25318/3610010401-eng
"""