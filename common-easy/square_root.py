
  def mySqrt(self, x: int) -> int:
      if x == 0:
          return 0  # Edge case: sqrt(0) = 0
      
      left, right = 1, x  # Define search space
      
      while left <= right:
          mid = left + (right - left) // 2  # Avoid overflow
          square = mid * mid
          
          if square == x:
              return mid  # Found exact square root
          elif square < x:
              left = mid + 1  # Search in the right half
          else:
              right = mid - 1  # Search in the left half
      
      return right  # The integer square root
    
print(mysqrt(8)) # output:- 2

