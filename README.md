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
- Struggled with: (write if any)  
- Next steps: Continue DSA problems, explore more Python concepts, start mini-projects


Day 2

Goals Completed

Solved 3 DSA problems on LeetCode: Move Zeroes (#283), Running Sum of 1d Array (#1480), Best Time to Buy and Sell Stock II (#122)

Learned Python list operations, in-place modification, and accumulation techniques

📝 DSA Problems Solved

Move Zeroes (#283, Easy)

Approach: Use a pointer pos to track where the next non-zero element should go. Iterate through the list, swapping non-zero elements to the position pos and increment pos. Moves all zeros to the end in-place.

Time Complexity: O(n)

Space Complexity: O(1)

Code: /DSA/Day2/move_zeroes.py

Running Sum of 1d Array (#1480, Easy)

Approach: Initialize sum = 0 and an empty list l. Iterate through nums, adding each element to sum and appending it to l. Return l containing the running sums.

Time Complexity: O(n)

Space Complexity: O(n)

Code: /DSA/Day2/running_sum.py

Best Time to Buy and Sell Stock II (#122, Easy)

Approach: Track minimum price so far (maxy) and current transaction profit (profit). Iterate through prices, update profit if the current price minus maxy is higher. If the price drops below previous minimum, add current profit to max_profit and reset profit. Return total profit.

Time Complexity: O(n)

Space Complexity: O(1)

Code: /DSA/Day2/max_profit.py

Python / Tools Learned

Reinforced list operations and in-place modification

Practiced accumulation patterns using loops

Learned to track variables to calculate running totals efficiently

Notes / Reflection

Key learning: Efficient array manipulation and accumulation

Struggled with: Keeping track of in-place changes for Move Zeroes

Next steps: Solve more array problems and start exploring Python functions and dictionaries