import math
import random

def ReplyHelloWorld():
    return "Hello world!"

print(ReplyHelloWorld())


def genDataTimeToMilliSeconds():
    return [random.randint(0,20),random.randint(0,20),random.randint(0,100),random.randint(0,100)]

def TimeToMilliSeconds(days,hours,minutes,seconds):
    secondInMilliSecondsFactor = 1000
    minuteInSecondsFactor = 60
    hourInMinutesFactor = 60
    dayInHoursFactor = 24

    timeInMilliSeconds = ((((days * dayInHoursFactor) + hours) * hourInMinutesFactor + minutes) * minuteInSecondsFactor + seconds) * secondInMilliSecondsFactor

    return timeInMilliSeconds

print(TimeToMilliSeconds(20,20,100,100))


def genTriangle():
    return([(random.randint(-50,50),random.randint(-50,50)),(random.randint(-50,50),random.randint(-50,50)),(random.randint(-50,50),random.randint(-50,50))])

def PointDistance(pointA,pointB):
    xDiff = abs(pointB[0]-pointA[0])
    yDiff = abs(pointB[1]-pointA[1])
    return math.sqrt( xDiff**2 + yDiff**2 )

def CircumferenceOfTriangle(pointList):    
    circumference = 0
    for i in range(0,len(pointList)-1):
        circumference += PointDistance(pointList[i],pointList[i+1])
    
    circumference += PointDistance(pointList[len(pointList)-1],pointList[0])

    return circumference
pointList = [(0,0),(4,0),(0,3)]
print(CircumferenceOfTriangle(pointList))


def AreaOfATriangle(pointList):
    sideA = PointDistance(pointList[0], pointList[1])
    sideB = PointDistance(pointList[1], pointList[2])
    sideC = PointDistance(pointList[2], pointList[0])
    semiPerimeter = (sideA + sideB + sideC)/2

    return math.sqrt(semiPerimeter*(semiPerimeter-sideA)*\
                                   (semiPerimeter-sideB)*\
                                   (semiPerimeter-sideC))
pointList = [(0,0),(4,0),(0,3)]
print(AreaOfATriangle(pointList))



def AreaOfATriangle2(pointList):
    sideList = []
    sideList.append(PointDistance(pointList[0], pointList[1]))
    sideList.append(PointDistance(pointList[1], pointList[2]))
    sideList.append(PointDistance(pointList[2], pointList[0]))

    sideList.sort(reverse=True)


pointList = [(0,0),(4,0),(0,3)]
print(AreaOfATriangle(pointList))



def LargestDistance(pointList):
    def PointDistance(pointA,pointB):
        xDiff = abs(pointB[0]-pointA[0])
        yDiff = abs(pointB[1]-pointA[1])
        return math.sqrt( xDiff**2 + yDiff**2 )

    largestDistance = 0
    for i in range(0,len(pointList)):
        for j in range(0,len(pointList)):
            distance = PointDistance(pointList[i],pointList[j])
            if distance > largestDistance:
                largestDistance = distance
    return largestDistance
pointList = [(0,0),(4,0),(0,3)]
print(LargestDistance(pointList))

def CalculateHammingDistance(string1,string2):
    numberOfDifferentSigns = 0
    for i in range(0,len(string1)):
        if string1[i] != string2[i]:
            numberOfDifferentSigns += 1    
    return numberOfDifferentSigns


def MinimalHammingDistance(string1, string2):
    minimalHammingDistance = len(string2)+1
    startIndexOfAlignment = 0
    shortestString = string1
    longestString = string2
    lengthShortestString = len(shortestString)
    if len(string2) < len(string1):
        shortestString = string2
        longestString = string1
        lengthShortestString = len(shortestString)

    for i in range(0,len(longestString)):
        hammingDistance = CalculateHammingDistance(shortestString,string2[i+lengthShortestString])
        if minimalHammingDistance < hammingDistance:
            minimalHammingDistance = hammingDistance
            startIndexOfAlignment = i

    return (minimalHammingDistance, startIndexOfAlignment)



def twoSum(nums: List[int], target: int):
    dict = {}
    dict[str(nums[0])] = (nums[0],0)
    for i in range(1,len(nums)):
        currentValue = nums[i]
        requiredNumber = target - currentValue

        if dict.get(str(requiredNumber),'missing') != 'missing':
            return [dict.get(str(requiredNumber))[1],i]
        
        dict[str(currentValue)] = (currentValue,i)
    
    return 0


def maxProfit(prices: List[int]):

    largestProfit = 0
    buyIndex = 0

    for sellIndex in range(1,len(prices)):
        profit = prices[sellIndex] - prices[buyIndex]

        if profit > largestProfit:
            largestProfit = profit
        
        if prices[sellIndex] < prices[buyIndex]:
            buyIndex = sellIndex

    return largestProfit



def cellularAutomaton(rule,initialState,n,zeroChar,oneChar,doPrint):
    ruleIndDict = {}

    ruleIndDict["111"] = 0
    ruleIndDict["110"] = 1
    ruleIndDict["101"] = 2
    ruleIndDict["100"] = 3
    ruleIndDict["011"] = 4
    ruleIndDict["010"] = 5
    ruleIndDict["001"] = 6
    ruleIndDict["000"] = 7

    def parsedBin(binStr,zeroChar,oneChar):
        result = []
        for i in binStr:
            if i == "1":
                result.append(oneChar)
            else:
                result.append(zeroChar)
        return "".join(result)

    def oneAutomatonEvolution(rule,state):
        resultArray = [0]*len(state)
        for i in range(1, len(state)-1):
            parentStateI = state[i-1:i+2]
            resultArray[i] = rule[ruleIndDict[parentStateI]]
        
        parentStateI = state[-1] + state[:2]
        resultArray[0] = rule[ruleIndDict[parentStateI]]

        parentStateI = state[-2:] + state[0]
        resultArray[-1] = rule[ruleIndDict[parentStateI]]

        strResult = "".join(resultArray)
        
        return strResult

    state = initialState
    doPrint and print(parsedBin(state,zeroChar,oneChar))
    for i in range(0,n):
        state = oneAutomatonEvolution(rule,state)
        doPrint and print(parsedBin(state,zeroChar,oneChar))
    
    return state



initialState = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
n = 70
rule = "01101110"


cellularAutomaton(rule,initialState,10000," ",".",True)

