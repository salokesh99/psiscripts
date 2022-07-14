
import pandas as pd    

def extract_data_with_marks_greater_than_500(file_location):
        
    # Read the file    
    data = pd.read_csv(file_location, low_memory=False)

        
    # Output the number of rows    
    print("Total rows: {0}".format(len(data)))   


    greater_than_500 = data[data['Marks'] > 500 ]

    return greater_than_500
