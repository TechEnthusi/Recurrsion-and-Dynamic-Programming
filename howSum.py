# create a function which takes two arguements first target_sum and 
# second list of numbers and if its is not possible to get the sum then just return None

# here we are using memoization
def howSum(target_sum, numbers, memo = {}):
      if target_sum in memo:
            print(memo)
            return memo[target_sum]
      if target_sum == 0:
            return []
      if target_sum < 0:
            return None
      
      for num in numbers:
            ans = target_sum - num
            ans_result = howSum(ans, numbers, memo)
            if ans_result is not None:
                  memo[target_sum] = ans_result[:] + [num]
                  return memo[target_sum]
      memo[target_sum] = None
      return memo[target_sum]
      

print(howSum(30, [10]))
