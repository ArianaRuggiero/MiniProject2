from FileReader import readCSV
import math

dataSet = readCSV('CSV_files/test.csv')

#1 Population Mean
def populationMean(dataSet):
        mean = sum(dataSet) / len(dataSet)
        return mean

# print("Population mean: ", str(populationMean(dataSet)))

#2 Median
def median(dataSet):
    listLength = len(dataSet)
    sortedList = sorted(dataSet)
    index = (listLength - 1) // 2
    if (listLength % 2):
        return sortedList[index]
    else:
        return (sortedList[index] + sortedList[index + 1])/2.0

# print('Mode: ', str(median(dataSet)))

#3 Mode 
def mode(dataSet):
    n = len(dataSet)
    getMode = {}

    for l in dataSet:
        getMode[l] = getMode.get(l,0) + 1

    maxValue = max(list(getMode.values()))
    modeValue = [a for a, v in getMode.items() if v == maxValue]

    if len(modeValue) == n:
        return("No mode within given dataset")
    else:
        return("Mode is / are: " + ', '.join(map(str, modeValue)))

# print(str(mode(dataSet)))

#4 Population Variance
def variance(dataSet):
    mean = sum(dataSet) / len(dataSet)

    variance = sum((xi - mean) ** 2 for xi in dataSet) / len(dataSet)
    return variance

# print('Population Variance: ', str(variance(dataSet)))

#5 Variance of population proportion
def variancePopulationProportion(dataSet):
    mean = sum(dataSet) / len(dataSet)
    populationProportion = 1 / len(dataSet)
    variance = sum((xi - mean) ** 2 for xi in dataSet) / (1 / len(dataSet))

    return variance

# print('Variance of Population Proportion: ', str(variancePopulationProportion(dataSet)))

#6 Z-Score
def zScore(dataSet):
    mean = sum(dataSet) / len(dataSet)
    std = math.sqrt(sum([(val - mean)**2 for val in dataSet])/(len(dataSet) - 1))

    for num in dataSet:
        # calculates the z-score of each number in the dataset
        zScore = (num - mean)/std
        print("z-score of", num, "=", zScore)

# zScore(dataSet)
#7 Standardized Score 

#8 Population Correlation Coefficient 

#9 Confidence Interval
def confidenceInterval(dataSet):
    from scipy.stats import sem, t
    n = len(dataSet)
    confidence = .95
    m = sum(dataSet) / n
    std_err = sem(dataSet)
    h = std_err * t.ppf((1 + confidence) / 2, n - 1)

    start = m + h
    end = m - h

    return start, end

# print ("Confidence Interval:", confidenceInterval(dataSet))

#10 Population Variance

#11 P Value

#12 Proportion

#13 Sample Mean
def sampleMean(dataSet):
    smean = sum(dataSet) / len(dataSet)

    return smean
# print ("Sample Mean:", sampleMean(dataSet))

#14 Sample Standard Deviation
def standardDeviation(dataSet):
    mean = sum(dataSet) / len(dataSet)
    std = math.sqrt(sum([(val - mean)**2 for val in dataSet])/(len(dataSet) - 1))

    return std
#15 Variance of sample proportion


