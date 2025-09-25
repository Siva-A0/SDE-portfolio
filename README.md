#  SDE Portfolio

This repository tracks my journey of learning **DSA, Python, and projects** step by step.  
Goal: Build problem-solving skills, Python proficiency, and maintain a professional portfolio.

---

##  Day 1

###  Goals Completed
- [x] Installed Python 3.13.7 and set up virtual environment
- [x] Set up VSCode + pip
- [x] Created GitHub repo + .gitignore
- [x] Solved 3 DSA problems on LeetCode: Two Sum (#1), Best Time to Buy and Sell Stock (#121), Merge Sorted Array (#88)

### 📝 DSA Problems Solved

1. **Two Sum (#1, Easy)**  
   - Approach: Use hash map to store seen numbers; check for complement  
   - Time Complexity: O(n), Space Complexity: O(n)  
   - Code: `/DSA/Day1/two_sum.py`

2. **Best Time to Buy and Sell Stock (#121, Easy)**  
   - Approach: Track minimum price while iterating; calculate max profit  
   - Time Complexity: O(n), Space Complexity: O(1)  
   - Code: `/DSA/Day1/best_time_to_buy_sell_stock.py`

3. **Merge Sorted Array (#88, Easy)**  
   - Approach:  
     1. Take both input arrays.  
     2. Compare elements from the start of each array.  
     3. Place the smaller element into the current index of the main array.  
     4. Move the pointer in the main array and the pointer in the array from which the element was taken.  
     5. Repeat until one array is exhausted.  
     6. Append any remaining elements from the non-empty array to the main array.  
   - Time Complexity: O(m + n), Space Complexity: O(1) — in-place merge  
   - Code: `/DSA/Day1/merge_sorted_array.py`

###  Python / Tools Learned
- Python 3.13.7 installed  
- Virtual environment setup (`venv`)  
- VSCode configuration  
- `requirements.txt` creation

###  Notes / Reflection
- Key learning: GitHub workflow, structuring repo, Python environment setup  
- Struggled with: None
- Next steps: Continue DSA problems, explore more Python concepts, start mini-projects


---


## Day 2

### Goals Completed

* [x] Solved 3 DSA problems on LeetCode: Move Zeroes (#283), Running Sum of 1d Array (#1480), Best Time to Buy and Sell Stock II (#122)
* [x] Learned Python list operations, in-place modification, and accumulation techniques

### 📝 DSA Problems Solved

1. **Move Zeroes (#283, Easy)**

   * Approach: Use a pointer `pos` to track where the next non-zero element should go. Iterate through the list, swapping non-zero elements to the position `pos` and increment `pos`. Moves all zeros to the end **in-place**.
   * Time Complexity: O(n)
   * Space Complexity: O(1)
   * Code: `/DSA/Day2/move_zeroes.py`

2. **Running Sum of 1d Array (#1480, Easy)**

   * Approach: Initialize `sum = 0` and an empty list `l`. Iterate through `nums`, adding each element to `sum` and appending it to `l`. Return `l` containing the running sums.
   * Time Complexity: O(n)
   * Space Complexity: O(n)
   * Code: `/DSA/Day2/running_sum.py`

3. **Best Time to Buy and Sell Stock II (#122, Easy)**

   * Approach: Track minimum price so far (`maxy`) and current transaction profit (`profit`). Iterate through `prices`, update `profit` if the current price minus `maxy` is higher. If the price drops below previous minimum, add current `profit` to `max_profit` and reset `profit`. Return total profit.
   * Time Complexity: O(n)
   * Space Complexity: O(1)
   * Code: `/DSA/Day2/best_time_to_buy_sell_stock2.py`

### Python / Tools Learned

* Reinforced list operations and **in-place modification**
* Practiced **accumulation patterns** using loops
* Learned to track variables to calculate running totals efficiently

### Notes / Reflection

* Key learning: Efficient **array manipulation** and **accumulation**
* Struggled with: Keeping track of **in-place changes** for Move Zeroes
* Next steps: Solve more array problems and start exploring **Python functions and dictionaries**


---


## Day 3

### Goals Completed

* [x] Solved 3 DSA problems on LeetCode: **Find Pivot Index (#724)**, **Majority Element (#169)**, **Fibonacci Number (#509)**
* [x] Learned Python techniques for array traversal, hash maps, and iterative computation

### 📝 DSA Problems Solved

1. **Find Pivot Index (#724, Easy)**

   * Approach: Calculate the total sum of the array `t`. Iterate through the array while maintaining a running left sum `l`. At each index, check if `l` equals `t - l - nums[x]` (i.e., left sum equals right sum). If so, return the index. Otherwise, add the current element to `l`. Returns `-1` if no pivot exists.
   * Time Complexity: O(n)
   * Space Complexity: O(1)
   * Code: `/DSA/Day3/pivot_index.py`

2. **Majority Element (#169, Easy)**

   * Approach: Use a hash map (`d`) to count occurrences of each element. Iterate through the map to find the element with a count greater than `len(nums)//2` and return it. (Alternative sorted array approach is commented out.)
   * Time Complexity: O(n)
   * Space Complexity: O(n)
   * Code: `/DSA/Day3/majority.py`

3. **Fibonacci Number (#509, Easy)**

   * Approach: Handle base cases (`n==0` returns 0, `n==1` returns 1). For `n>1`, use two variables `fib0` and `fib1` to iteratively calculate Fibonacci numbers up to `n` using a for-loop. Return `fib1` as the nth Fibonacci number.
   * Time Complexity: O(n)
   * Space Complexity: O(1)
   * Code: `/DSA/Day3/fibonacci.py`

### Python / Tools Learned

* Iterative computation for **Fibonacci sequence** (space-optimized)
* Using **hash maps** for frequency counting problems
* Array traversal techniques and prefix/running sums

### Notes / Reflection

* Key learning: Efficient array traversal and frequency counting; learned to replace recursion with **iterative approaches** for optimization
* Struggled with: Remembering the pivot condition formula for left/right sums
* Next steps: Solve more array and recursion problems, start exploring **Python sets and dictionary comprehensions**


---


## Day 4

### Goals Completed

* [x] Solved 3 DSA problems on LeetCode: **Remove Duplicates from Sorted Array (#26)**, **Squares of a Sorted Array (#977)**, **Pascal's Triangle (#118)**
* [x] Practiced in-place array modification, sorting after transformation, and constructing patterns with lists

### 📝 DSA Problems Solved

1. **Remove Duplicates from Sorted Array (#26, Easy)**

   * Approach: Use two pointers. Keep index `i` to mark the last unique element. Iterate through the array; if the current element is different from `nums[i]`, increment `i` and swap `nums[i]` with `nums[x]`. Finally, return `i+1` as the new length of the unique elements.
   * Time Complexity: O(n)
   * Space Complexity: O(1)
   * Code: `/DSA/Day4/remove_duplicates.py`

2. **Squares of a Sorted Array (#977, Easy)**

   * Approach: Iterate through the array, square each element, then sort the list before returning it. (Uses Python’s built-in sort for simplicity.)
   * Time Complexity: O(n log n)
   * Space Complexity: O(1) (ignoring sorting’s internal memory use)
   * Code: `/DSA/Day4/squares_of_sorted_array.py`

3. **Pascal's Triangle (#118, Easy)**

   * Approach: Start with base cases for 1 and 2 rows. For larger `numRows`, build each row iteratively by adding adjacent numbers from the previous row, with `1` at the start and end. Append each new row to the result until `numRows` is reached.
   * Time Complexity: O(n²) (due to nested iteration)
   * Space Complexity: O(n²) (to store the triangle)
   * Code: `/DSA/Day4/pascal_triangle.py`

### Python / Tools Learned

* learned **two-pointer technique** for in-place array updates
* Used Python’s **built-in sort** after transformations
* Practiced **nested loops and list appending** to generate patterns (Pascal’s Triangle)

### Notes / Reflection

* Key learning: Importance of **in-place modification** and when sorting is acceptable versus optimal
* Struggled with: Remembering how to correctly build inner elements of Pascal’s Triangle
* Next steps: Explore **two-pointer optimized solutions** (e.g., for sorted squares without sorting) and practice more pattern-based problems


---
