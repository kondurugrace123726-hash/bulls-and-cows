# bulls-and-cows
Clean and simple Python implementation of the Bulls and Cows problem.
# 🐂🐄 Bulls and Cows

## 📌 Overview
This repository contains a clean and beginner-friendly Python solution for a problem **Bulls and Cows**.

The goal is to generate a hint string that represents:
- Bulls → correct digit in the correct position
- Cows → correct digit in the wrong position

## 🧠 Approach
The solution follows a simple two-step method:

1. **Count Bulls**
   - Compare characters at the same index in both strings.

2. **Count Total Matches**
   - Count digit frequencies in both strings.
   - Cows = total matches − bulls.

This ensures correctness while keeping the implementation simple and readable.

## ⏱ Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
