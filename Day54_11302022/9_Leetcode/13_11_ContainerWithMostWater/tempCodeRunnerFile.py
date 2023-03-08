maxFromLeft = [0] * len(height)
    maxFromRight = [0] * len(height)
    n = len(height)
    maxFromLeft[0] = height[0]
    for i in range(1,n):
        maxFromLeft[i] = max(maxFromLeft[i-1], height[i])
    print(maxFromLeft)

    maxFromRight[n - 1] = height[n-1]
    for j in range(n-2,-1,-1):
        maxFromRight[j] = max(maxFromRight[j+1], height[j])
    print(maxFromRight)

    waterArea = [0] * n
    for k in range(n):
        waterArea[k] = min(maxFromLeft[k],maxFromRight[k])-height[k]
    
        
    print("WaterArea: ",sum(waterArea))