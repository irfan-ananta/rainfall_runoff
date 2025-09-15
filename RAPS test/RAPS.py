#import required module
import pandas as pd

def RAPS_test(file):
    """
    Perform RAPS test on rainfall data from a CSV file.
    
    Parameters:
    file (str): Path to the CSV file containing rainfall data.
    """
    # Load the CSV file
    df = pd.read_csv(file)
    
    # Prepare a summary dictionary
    summary = {}
    conclusion_rows = []
    
    # Drop any unnamed columns (e.g., index columns)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Iterate over each station column (excluding 'Tahun')
    for station in df.columns[1:]:
        # Count, sum, average, variance, and Standard Deviation
        name = station[0:]
        values = df[station]
        count = values.count()
        average = values.mean()
        deviation = values - average
        squared_deviation = deviation ** 2
        variance = squared_deviation.sum() / (count-1)
        st_dev = variance ** 0.5

        # Sk*, sk**, sk** max, sk** min, Q, R, Q/(n^0.5, and R/(n^0.5)
        sk = deviation.cumsum()
        sk2 = sk / st_dev
        max_sk = sk2.max()
        min_sk = sk2.min()
        Q = max_sk
        R = max_sk - min_sk
        Q_calculated = Q / count ** 0.5
        R_calculated = R / count ** 0.5
    
        # Q/(n^0.5) and R/(n^0.5)
        i = [10,20,35,40,50,100,101]
        data = {
            'Q/√n (90%)': [1.050, 1.100, 1.120, 1.130, 1.140, 1.170, 1.220],
            'Q/√n (95%)': [1.140, 1.220, 1.240, 1.260, 1.270, 1.290, 1.360],
            'Q/√n (99%)': [1.290, 1.420, 1.460, 1.500, 1.520, 1.550, 1.630],
            'R/√n (90%)': [1.210, 1.340, 1.400, 1.420, 1.440, 1.500, 1.620],
            'R/√n (95%)': [1.280, 1.430, 1.500, 1.530, 1.550, 1.620, 1.750],
            'R/√n (99%)': [1.380, 1.600, 1.700, 1.740, 1.780, 1.860, 2.000]
        }
        dp = pd.DataFrame(data, index=i)
    
        #Interpolate Q/(n^0.5) and R/(n^0.5) theoretical
        interpolated_values = dp.reindex(dp.index.union([count])).sort_index().interpolate(method='index')
        Q90 = interpolated_values.loc[count, 'Q/√n (90%)'].round(3)
        Q95 = interpolated_values.loc[count, 'Q/√n (95%)'].round(3)
        Q99 = interpolated_values.loc[count, 'Q/√n (99%)'].round(3)
        R90 = interpolated_values.loc[count, 'R/√n (90%)'].round(3)
        R95 = interpolated_values.loc[count, 'R/√n (95%)'].round(3)
        R99 = interpolated_values.loc[count, 'R/√n (99%)'].round(3)
        dp.index = [10,20,35,40,50,100,'>100'] #adjust the index manually

        #Helper function to create conclusion table
        def create_conclusion_table(calculated, theoretical_values, label):
            conclusion = {'Alpha': ['1%', '5%', '10%']}
            table = pd.DataFrame(conclusion)
            table[f'{label} calculated'] = calculated
            table.at[0, f'{label} theoretical'] = theoretical_values[0]
            table.at[1, f'{label} theoretical'] = theoretical_values[1]
            table.at[2, f'{label} theoretical'] = theoretical_values[2]
            table['Conclusion'] = ['Ok' if calculated < theoretical else 'Tidak Ok' for theoretical in theoretical_values]
            return table
    
        # Create conclusion tables
        Q_conclusion = create_conclusion_table(Q_calculated, [Q99, Q95, Q90], 'Q/(n^0.5)')
        R_conclusion = create_conclusion_table(R_calculated, [R99, R95, R90], 'R/(n^0.5)')
    
        # Store the results in the summary dictionary
        summary[station] = {
            'Count' : count,
            'Mean' : round(average, 3),
            'Variance' : round(variance, 3),
            'St dev' : round(st_dev, 3),
            'sk* max' : round(max_sk,3),
            'sk* min' : round(min_sk,3),
            'Q' : round(Q, 3),
            'R' : round(R, 3),
            'Q/(n^0.5)' : round(Q_calculated, 3),
            'R/(n^0.5)' : round(R_calculated, 3),
            'Q_conclusion' : Q_conclusion,
            'R_conclusion' : R_conclusion
        }

        conclusion_rows = {
            'Q conclusion' : Q_conclusion,
            'R conclusion' : R_conclusion
        }

    # Convert the summary dictionary to a DataFrame
    summary_df = pd.DataFrame({k: {kk: vv for kk, vv in v.items() if not isinstance(vv, pd.DataFrame)} for k, v in summary.items()})     
    
    #Printing
    print(summary_df)
    #print(f"\n Qy/√n and Ry/√n theoretical value")
    #print(f"{dp}")
    for station in df.columns[1:]:
        print(f"\n{station}")
        print('Q Conclusion')
        print(summary[station]['Q_conclusion'])
        print('R Conclusion')
        print(summary[station]['R_conclusion'])
    
    # Create summary DataFrame
    #summary_df = pd.DataFrame(summary)
    #conclusion = pd.DataFrame(conclusion_rows)
    
    #print (f"\n{conclusion_rows}")
    # Combine all conclusion tables
    #conclusion_df = pd.concat([summary_df. conclusion], ignore_index=True)
    #print(conclusion_df)
    
    # Export both to a single CSV
    #with open("result.csv", "w", encoding="utf-8") as f:
        #summary_df.to_csv(f)
        #f.write("\nConclusion Tables\n")
        #conclusion_df.to_csv(f, index=False)
    #summary_df.to_csv('result.csv')
RAPS_test('Rainfall 2.csv')
