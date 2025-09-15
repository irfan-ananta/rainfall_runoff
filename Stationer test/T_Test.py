def T_test(file):
    #import required module
    import pandas as pd
    
    #Read a csv file
    df = pd.read_csv(file)
    rainfall = df.iloc[:,1]
    
    #Divide into 2 column
    mid_point = (len (rainfall) + 1) // 2
    Group_1 = rainfall.iloc[:mid_point]
    Group_2 = rainfall.iloc[mid_point:]
    
    #Count, sum, average, variance, and Standard Deviation
    n_1 = Group_1.count()
    n_2 = Group_2.count()
    average_1 = Group_1.mean().round(3)
    average_2 = Group_2.mean().round(3)
    variance_1 = (((Group_1 - average_1)**2).sum()/ (n_1-1)).round(3)
    variance_2 = (((Group_2 - average_2)**2).sum()/ (n_2-1)).round(3)
    st_dev_1 = (variance_1 ** 0.5).round(3)
    st_dev_2 = (variance_2 ** 0.5).round(3)
    sigma = (((n_1 * st_dev_1**2 + n_2 * st_dev_2**2)/(n_1+n_2-2))**0.5).round(3)

    #printing
    print(f"n1: {n_1}")
    print(f"n2: {n_2}")
    print(f"Average1: {average_1}")
    print(f"Average2: {average_2}")
    print(f"SD1: {st_dev_1}")
    print(f"SD2: {st_dev_2}")
    print(f"Variance1: {variance_1}")
    print(f"Variance2: {variance_2}")
    print(f"sigma: {sigma}")
    #print(table)
T_test('rainfall.csv')
