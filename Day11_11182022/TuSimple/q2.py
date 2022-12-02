price = [1,2,3,4,5]
pos = [1,3]
amount = [4,14]
res = []
for i in range(0, len(pos)):
    z = pos[i]-1
    A = amount[i]
    count = 0
    sum = 0
    maxvar = 0
    for j in range(z, len(price)):
        print("j = ", j)
        sum = price[j]
        count = count + 1
        # if(sum>A):
        #     res.append(count)
        #     continue
        # else:
        #     A = A - sum
        #     count  = count + 1
        for k in range(j+1, len(price)):
            print("sum + price[k] = ",sum, " ",price[k])
            sum =  sum + price[k]
            print("sum = ",sum)

            if(sum<=A):
                A = A - sum
                count  = count + 1
          
            else:
                print("Count= ",count)
                maxvar = max(count,maxvar)
                print("Break = ", price[j])
                break
    res.append(maxvar)
    
print("Result= ",res)




# int count = 0;
#     if (pos < 0 || pos >= n)
#         return 0;
#     for (int i = pos; i < n; i++) {
#         if (arr[i] <= val) {
#             val = val - arr[i];
#             count++;
#         }
#         else {
#             break;
#         }
#     }
#     return count;