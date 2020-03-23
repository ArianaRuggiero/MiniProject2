from FileReader import readCSV
#from scipy.stats import sem, t

confidence = 0.95

dataSet = readCSV('CSV_files/test.csv')

def confidenceInterval(dataSet):
    n = len(dataSet)
    m = sum(dataSet) / n
    std = math.sqrt(sum([(val - m)**2 for val in dataSet])/(len(dataSet) - 1))
    std_err = std / math.sqrt(n)
    t = m / std_err
    h = std_err * t * ((1 + confidence) / 2, n - 1)

    start = m + h
    end = m - h
    
    return start, end

    print ("Confidence Interval is:", start, end)
