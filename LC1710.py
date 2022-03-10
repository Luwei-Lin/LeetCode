def main():
    boxTypes = [[1,3],[2,2],[3,1]]
    truckSize = 4
    #maximumUnits(boxTypes, truckSize)
    print(maximumUnits2(boxTypes, truckSize))
    boxTypes_2 = [[5,10],[2,5],[4,7],[3,9]]
    truckSize_2 = 10
    print(maximumUnits2(boxTypes_2, truckSize_2))
    
def maximumUnits2(boxTypes, truckSize) -> int:
    boxTypes.sort(reverse = True, key = lambda x: (x[1], x[0]))
    unitsCount = 0
    for i in range(len(boxTypes)):
        boxCount = min(boxTypes[i][0], truckSize)
        unitsCount = unitsCount + boxTypes[i][1] * boxCount
        truckSize = truckSize - boxCount
        if truckSize == 0:
            break
    return unitsCount


        
def maximumUnits(boxTypes, truckSize) -> int:

    boxTypes.sort(reverse = True, key=lambda x: (x[1], x[0]))
    maxUnits = 0
    numberOfBoxesLoaded = 0
    leftSize = truckSize
    print(boxTypes)
    for i in range(len(boxTypes)):

        if numberOfBoxesLoaded < truckSize and leftSize >= boxTypes[i][0]:
            numberOfBoxesLoaded = numberOfBoxesLoaded + boxTypes[i][0]
            maxUnits = maxUnits + boxTypes[i][1] * boxTypes[i][0] #all boxes load on the truck
            leftSize = leftSize - boxTypes[i][0]

        elif numberOfBoxesLoaded < truckSize and leftSize < boxTypes[i][0]:
            numberOfBoxesLoaded = numberOfBoxesLoaded + leftSize
            maxUnits = maxUnits + boxTypes[i][1] * leftSize #left box and units
            leftSize = 0
        else:
            break

    print(maxUnits, numberOfBoxesLoaded)            
    
    return maxUnits

main()