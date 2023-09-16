# Embedded-SE-Knowledge-Test

Hi Chief Technology Officer,

Welcome to my answers for your knowledge test. I would first like to thank you and whoever constructed these problems as I enjoyed working through them. I found them to be appropriately challenging and it was ultimately fun to solve these tricky puzzles that you provided. Part 1 and 2 have been uploaded to this repository, where the c function in problem 1 and my answers for the hidden function in problem 2 are posted.

1)Part one deals with a rectangular piece of paper of dimensions N by M. There are "scissors" that are used to cut the paper to form a series of perfect squares untill there is no more paper left, with the goal of optimizing for largest square size. The solution of my function "Square" uses the following algorithm:

  1. Find the largest square formable on the current piece of paper (the dimensions are the shortest of N and M)
  2. Cut that piece of paper, print its dimensions, and reduce N or M accordingly
  3. While there is still paper left(N and M > 0 ), iterate steps 1 to three until there is no paper left

2) The solution to part two is a unique base 62 numbering system. At first I found this question to be quite tricky as there seemed to be no correlation between the input output. After folowing the hints and examining the dataset thoroughly with Python, I began to see patterns. Firstly, I noticed that every letter of the alphabet(uppercase and lower case), aswell as all numbers from 0-9(except 5) appear atleast once, that means, if there are 61 possible combinations for each slot of digit of output, the number of possible outcomes is 61^3. I also started noticing irregularities and patterns within the dataset. For one, the numbering system of the output does not follow the typical ordering of normal base 10 numbering system. For example, the input 49443 gives the ouput "yau" whereas the input 49444(one higher) gives the output "yap", however "p" proceeds "u" in the alphabet and in the normal base 61 numbering system. I tried to find other adjacent inputs and analysze their output to try and form an ordering map by hand, but decided to program
