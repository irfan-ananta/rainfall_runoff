#Import required libraries
import pandas as pd
import numpy as np

def F_test(file):
    # Set pandas to display all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    
    #Read a csv file
    df = pd.read_csv(file)
    rainfall = df.iloc[:,1]
    
    #Divide into 2 column
    mid_point = (len (rainfall) + 1) // 2
    Group_1 = rainfall.iloc[:mid_point].reset_index(drop=True)
    Group_2 = rainfall.iloc[mid_point:].reset_index(drop=True)
    
    #Count, sum, average, variance, and Standard Deviation
    n_1 = Group_1.count()
    n_2 = Group_2.count()
    average_1 = Group_1.mean().round(3)
    average_2 = Group_2.mean().round(3)
    variance_1 = (((Group_1 - average_1)**2).sum()/ (n_1-1)).round(3)
    variance_2 = (((Group_2 - average_2)**2).sum()/ (n_2-1)).round(3)
    st_dev_1 = (variance_1 ** 0.5).round(3)
    st_dev_2 = (variance_2 ** 0.5).round(3)
    df_1 = n_1 - 1
    df_2 = n_2 - 1
    alpha = 0.05
    F_Cal = (variance_1 / variance_2).round(2)

    #Create a group table
    Group_table_data = {
        'Group 1': Group_1,
        'Group 2': Group_2
    }
    Group_table = pd.DataFrame(Group_table_data)

    #F critis
    F_critis_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 40, 60, 120, 121]
    F_critis_data = {
        '1' : [161.45, 18.51, 10.13, 7.71, 6.61, 5.99, 5.59, 5.32, 5.12, 4.96, 4.84, 4.75, 4.67, 4.6, 4.54, 4.49, 4.45, 4.41, 4.38, 4.35, 4.32, 4.3, 4.28, 4.26, 4.24, 4.23, 4.21, 4.2, 4.18, 4.17, 4.08, 4, 3.92, 3.84],
        '2' : [199.5, 19, 9.55, 6.94, 5.79, 5.14, 4.74, 4.46, 4.26, 4.1, 3.98, 3.89, 3.81, 3.74, 3.68, 3.63, 3.59, 3.55, 3.52, 3.49, 3.47, 3.44, 3.42, 3.4, 3.39, 3.37, 3.35, 3.34, 3.33, 3.32, 3.23, 3.15, 3.07, 3],
        '3' : [215.71, 19.16, 9.28, 6.59, 5.41, 4.76, 4.35, 4.07, 3.86, 3.71, 3.59, 3.49, 3.41, 3.34, 3.29, 3.24, 3.2, 3.16, 3.13, 3.1, 3.07, 3.05, 3.03, 3.01, 2.99, 2.98, 2.96, 2.95, 2.93, 2.92, 2.84, 2.76, 2.68, 2.6],
        '4' : [224.58, 19.25, 9.12, 6.39, 5.19, 4.53, 4.12, 3.84, 3.63, 3.48, 3.36, 3.26, 3.18, 3.11, 3.06, 3.01, 2.96, 2.93, 2.9, 2.87, 2.84, 2.82, 2.8, 2.78, 2.76, 2.74, 2.73, 2.71, 2.7, 2.69, 2.61, 2.53, 2.45, 2.37],
        '5' : [230.16, 19.3, 9.01, 6.26, 5.06, 4.39, 3.97, 3.69, 3.48, 3.33, 3.2, 3.11, 3.03, 2.96, 2.9, 2.85, 2.81, 2.77, 2.74, 2.71, 2.68, 2.66, 2.64, 2.62, 2.6, 2.59, 2.57, 2.56, 2.55, 2.53, 2.45, 2.37, 2.29, 2.21],
        '6' : [233.99, 19.33, 8.94, 6.16, 4.95, 4.28, 3.87, 3.58, 3.37, 3.22, 3.09, 3, 2.92, 2.85, 2.79, 2.74, 2.7, 2.66, 2.63, 2.6, 2.57, 2.55, 2.53, 2.51, 2.49, 2.47, 2.46, 2.45, 2.43, 2.42, 2.34, 2.25, 2.17, 2.1],
        '7' : [236.77, 19.35, 8.89, 6.09, 4.88, 4.21, 3.79, 3.5, 3.29, 3.14, 3.01, 2.91, 2.83, 2.76, 2.71, 2.66, 2.61, 2.58, 2.54, 2.51, 2.49, 2.46, 2.44, 2.42, 2.4, 2.39, 2.37, 2.36, 2.35, 2.33, 2.25, 2.17, 2.09, 2.01],
        '8' : [238.88, 19.37, 8.85, 6.04, 4.82, 4.15, 3.37, 3.44, 3.23, 3.07, 2.95, 2.85, 2.77, 2.7, 2.64, 2.59, 2.55, 2.51, 2.48, 2.45, 2.42, 2.4, 2.44, 2.36, 2.34, 2.32, 2.31, 2.29, 2.28, 2.27, 2.18, 2.1, 2.02, 1.94],
        '9' : [240.54, 19.38, 8.81, 6, 4.77, 4.1, 3.68, 3.39, 3.18, 3.02, 2.9, 2.8, 2.71, 2.65, 2.59, 2.54, 2.49, 2.46, 2.42, 2.39, 2.37, 2.34, 2.32, 2.3, 2.28, 2.27, 2.25, 2.24, 2.22, 2.21, 2.12, 2.04, 1.96, 1.88],
        '10' : [241.88, 19.4, 8.79, 5.59, 4.74, 4.06, 3.64, 3.35, 3.14, 2.98, 2.85, 2.75, 2.67, 2.6, 2.54, 2.49, 2.45, 2.41, 2.38, 2.35, 2.32, 2.3, 2.27, 2.25, 2.24, 2.22, 2.2, 2.19, 2.18, 2.16, 2.08, 1.99, 1.91, 1.83],
        '12' : [243.9, 19.41, 8.74, 5.91, 4.68, 4, 3.57, 3.28, 3.07, 2.91, 2.79, 2.69, 2.6, 2.53, 2.48, 2.42, 2.38, 2.34, 2.31, 2.28, 2.25, 2.23, 2.2, 2.18, 2.16, 2.15, 2.13, 2.12, 2.1, 2.09, 2, 1.92, 1.83, 1.75],
        '15' : [245.95, 19.43, 8.7, 5.86, 4.62, 3.94, 3.51, 3.22, 3.01, 2.85, 2.72, 2.62, 2.53, 2.46, 2.4, 2.35, 2.31, 2.27, 2.23, 2.2, 2.18, 2.15, 2.13, 2.11, 2.09, 2.07, 2.06, 2.04, 2.03, 2.01, 1.92, 1.84, 1.75, 1.67],
        '20' : [248.01, 19.45, 8.66, 5.8, 4.56, 3.87, 3.44, 3.15, 2.94, 2.77, 2.65, 2.54, 2.46, 2.39, 2.33, 2.28, 2.23, 2.19, 2.16, 2.12, 2.1, 2.07, 2.05, 2.03, 2.01, 1.99, 1.97, 1.96, 1.95, 1.93, 1.84, 1.75, 1.66, 1.57],
        '24' : [249.05, 19.45, 8.64, 5.77, 4.53, 3.84, 3.41, 3.12, 2.9, 2.74, 2.61, 2.51, 2.42, 2.35, 2.29, 2.24, 2.19, 2.15, 2.11, 2.08, 2.05, 2.03, 2.01, 1.98, 1.96, 1.95, 1.93, 1.91, 1.9, 1.89, 1.79, 1.7, 1.61, 1.52],
        '30' : [250.1, 19.46, 8.62, 5.75, 4.5, 3.81, 3.38, 3.08, 2.86, 2.7, 2.57, 2.47, 2.38, 2.31, 2.25, 2.19, 2.15, 2.11, 2.07, 2.04, 2.01, 1.98, 1.96, 1.94, 1.92, 1.9, 1.88, 1.87, 1.85, 1.84, 1.74, 1.65, 1.55, 1.46],
        '40' : [250.14, 19.47, 8.59, 5.72, 4.46, 3.77, 3.34, 3.04, 2.83, 2.66, 2.53, 2.43, 2.34, 2.27, 2.2, 2.15, 2.1, 2.06, 2.03, 1.99, 1.96, 1.94, 1.91, 1.89, 1.87, 1.85, 1.84, 1.82, 1.81, 1.79, 1.69, 1.59, 1.5, 1.39],
        '60' : [252.2, 19.48, 8.57, 5.66, 4.43, 3.74, 3.3, 3.01, 2.79, 2.62, 2.49, 2.38, 2.3, 2.22, 2.16, 2.11, 2.06, 2.02, 1.98, 1.95, 1.92, 1.89, 1.86, 1.84, 1.82, 1.8, 1.79, 1.77, 1.75, 1.74, 1.64, 1.53, 1.43, 1.32],
        '120' : [253.25, 19.49, 8.55, 5.66, 4.4, 3.7, 3.27, 2.97, 2.75, 2.58, 2.45, 2.34, 2.25, 2.18, 2.11, 2.06, 2.01, 1.97, 1.93, 1.9, 1.87, 1.84, 1.81, 1.79, 1.77, 1.75, 1.73, 1.71, 1.7, 1.68, 1.58, 1.47, 1.35, 1.22],
        '121' : [254.31, 19.5, 8.53, 5.63, 4.36, 3.67, 3.23, 2.93, 2.71, 2.54, 2.4, 2.3, 2.21, 2.13, 2.07, 2.01, 1.96, 1.92, 1.88, 1.84, 1.81, 1.78, 1.76, 1.73, 1.71, 1.69, 1.67, 1.65, 1.64, 1.62, 1.51, 1.39, 1.25, 1]

    }
    F_critis_table = pd.DataFrame(F_critis_data, index=F_critis_index)
    
    # Interpolate rows based on dk1
    interpolated_values = F_critis_table.reindex(F_critis_table.index.union([df_1])).sort_index().interpolate(method='index')

    # Interpolate column based on dk2
    interpolated_values [df_2] = np.nan
    sorted_columns = sorted([col for col in interpolated_values.columns], key=lambda x: float(x)) #Sorting columns
    interpolated_values = interpolated_values.reindex(columns=sorted_columns) # Reindex columns 
    interpolated_values = interpolated_values.interpolate(axis=1).round(3) #interpolating columns

     #adjust the index and columns manually
    F_critis_table.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 40, 60, 120, 'inf.']
    F_critis_table.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '12', '15', '20', '24','30', '40', '60', '120', 'inf']
    
    #Interpolate Q/(n^0.5) and R/(n^0.5) theoretical
    #test = str(df_2)
    F5_Theoretical = interpolated_values.loc[df_1, df_2].round(3)
    F1_Theoretical = 2
    
    #Helper function to create conclusion table
    def create_conclusion_table(calculated, theoretical_values):
        conclusion = {'α': ['1%', '5%']}
        table = pd.DataFrame(conclusion)
        table['F calculated'] = calculated
        table.at[0, 'F theoretical'] = theoretical_values[0]
        table.at[1, 'F theoretical'] = theoretical_values[1]
        table['Conclusion'] = ['Ok' if calculated < theoretical else 'Tidak Ok' for theoretical in theoretical_values]
        return table
    
    # Create conclusion tables
    F5_conclusion = create_conclusion_table(F_Cal, [F1_Theoretical, F5_Theoretical])
    #R_conclusion = create_conclusion_table(R_calculated, [R99, R95, R90], 'R/√n')
    
    #printing
    print(f"n1: {n_1}")
    print(f"n2: {n_2}")
    print(f"Average1: {average_1}")
    print(f"Average2: {average_2}")
    print(f"SD1: {st_dev_1}")
    print(f"SD2: {st_dev_2}")
    print(f"Variance1: {variance_1}")
    print(f"Variance2: {variance_2}")
    print(f"df1: {df_1}")
    print(f"df2: {df_2}")
    print(f"F Calculated: {F_Cal}\n")
    print(f"Group Data \n{Group_table}\n")
    #print(test)
    #print(f"F critis table \n{F_critis_table}\n")
    #print(f"F critical: {F5_Theoretical}\n")
    print(f"Conclusion: \n{F5_conclusion}")
    #print(f"F critis table interpolated \n{interpolated_values}\n")
    
F_test('rainfall.csv')
