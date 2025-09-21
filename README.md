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
