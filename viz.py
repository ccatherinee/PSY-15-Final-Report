from scipy.stats import linregress
import matplotlib.pyplot as plt
import pickle

with open("data",'rb') as f:
    data = pickle.load(f)

#data is now the list of 10000 (course mean, hour mean) pairs

filtered = [p for p in data if p[1]>10]
rating, hours = zip(*filtered)

linear = linregress(rating,hours)
#LinregressResult(slope=0.3918410122631133, intercept=11.022292874380613, rvalue=0.093788769861992, pvalue=0.0011932944679831944, stderr=0.12062840146076613, intercept_stderr=0.5085977704838651)

#visualize
plt.scatter(rating,hours)
#plt.show()


