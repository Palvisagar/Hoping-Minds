def statistics(samples):

    N = len(samples)
    mean = sum(samples) / N
    sum_squares = sum((mean-x)**2 for x in samples)
    stan_dev = (sum_squares/(N-1))**0.5
    
    if N % 2 == 1:
        median =  sorted(samples)[N//2]  #odd case for median
    if N % 2 == 0:
        median = sum(sorted(samples)[N//2-1:N//2 + 1]) / 2 #even case for median

    minimum = min(samples)
    maximum = max(samples)
    data_range = maximum - minimum
    
    print("Mean:", mean)
    print("Standard deviation:", stan_dev)
    print("Minimum:", minimum)
    print("Median:", median)
    print("Maximum:", maximum)
    print("Data range:", data_range)
    print("Sample Size:", N)

'''Test'''
samples = [40,40,60,80,90] 

statistics(samples)