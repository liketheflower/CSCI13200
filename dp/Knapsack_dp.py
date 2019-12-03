# A naive recursive implementation (top down DP without memo) of 0-1 Knapsack Problem 
  
# Returns the maximum value that can be put in a knapsack of 
# capacity W
vals = [60, 100, 120] 
weights = [10, 20, 30] 
W = 50
def knapsack(W, i): 
  
    # Base Case 
    if i == -1 or W == 0 : 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (weights[i] > W): 
        return knapSack(W, i-1) 
  
    # return the maximum of two cases: 
    # (1) item[i] included 
    # (2) not included 
    else: 
        return max(vals[i] + knapsack(W-weights[i],  i-1), 
                   knapsack(W, i-1)) 
  
# end of function knapSack 
  
# To test above function 
print (knapsack(W, len(vals)-1))
