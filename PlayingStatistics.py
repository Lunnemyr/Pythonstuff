import statistics
example_list=[4,6,5,2,5,6,4,5,6,8,3,6,7,5,7,2,2,2,2,2,1]
x= statistics.mean(example_list)
print('Mean: ',x)

x= statistics.median(example_list)
print('Median: ',x)

x= statistics.stdev(example_list)
print('Standard deviation: ',x)


x= statistics.variance(example_list)
print('Variance: ',x)
