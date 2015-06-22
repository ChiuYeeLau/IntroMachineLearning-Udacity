#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    error = (predictions - net_worths)*(predictions - net_worths)
    cleaned_data = zip (ages, net_worths, error)
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2], reverse = True)
    
    return cleaned_data [int(len(cleaned_data) * 0.1):]
