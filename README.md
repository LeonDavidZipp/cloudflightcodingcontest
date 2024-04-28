# Cloudflight Coding Contest
The coding contest took place on the **19th of April, 2024 at 42 Heilbronn**. I joined as a one-man-team and **completed 3 levels** (as many as my location's 1. place, but in a longer timespan), **finishing 13th out of 26**. My programming language of choice was **Python**, since code efficiency and performance were less important than typing speed. 

## Levels
All levels consisted of 5 subleveles, which could all be solved using the same codebase. Every exercise was split into 3 parts:
### 1. Input Parsing
The input had to be first read from the file. Afterwards it had to be passed to the functions correctly.
### 2. Program Logic 
The main challenge.
### 3. Writing Solution to File
For each Sublevel, the result had to be formatted accordingly and written to a file, which then was uploaded to the solution page.

## [Level 1](https://github.com/LeonDavidZipp/cloudflightcodingcontest/tree/main/lvl_1): ✅ Passed
The 1. level's challenge was **calculating how many times each character (W, A, S, D) was inside the input**.

## [Level 20](https://github.com/LeonDavidZipp/cloudflightcodingcontest/tree/main/lvl_2): ✅ Passed
The 2. level was more complicated: The task was now to **calculate the minimum size of the rectangle of a device's travel path**. This path was determined by how many times each character (W, A, S, D) was inside the input.

## [Level 3](https://github.com/LeonDavidZipp/cloudflightcodingcontest/tree/main/lvl_3): ✅ Passed
The 3rd level required checking **whether a given path** (again determined by how many times each character (W, A, S, D) was inside the input) **could solve a given map** (passed in the input file as well). For this I chose a simple **brute force algorithm**, trying out the path from every field of the map.

## [Level 4](https://github.com/LeonDavidZipp/cloudflightcodingcontest/tree/main/lvl_4): ❌ Tried but failed
The 4th level was by far the most difficult. The **challenge was to find a valid path given a map**. A possible solution can be found using backtracking, but I was not able to implement it during the contest.
