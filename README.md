# Embedded-SE-Knowledge-Test

Hi, Chief Technology Officer,

Welcome to my answers for your knowledge test. I would first like to thank you and whoever constructed these problems, as I enjoyed working through them. I found them to be appropriately challenging, and solving the tricky puzzles you provided was ultimately fun. Parts 1 and 2 have been uploaded to this repository, where the c function in problem one and my answers for the function in problem two are posted.

1)Part one deals with a rectangular piece of paper of dimensions N by M. There are "scissors" that cut the paper to form a series of perfect squares until no more writing is left, optimizing for the most significant square size. The solution of my function "Square" uses the following algorithm:

  1. Find the largest square formable on the current piece of paper (the length and width are the shortest of N and M)
  2. Cut that piece of paper, print its dimensions, and reduce N or M accordingly
  3. While there is still paper left(N and M > 0 ), iterate steps 1 to three until there is no paper left


2)The solution to part two is a unique base 62 numbering system. At first, I found this question quite tricky as there seemed to be no correlation between the input and output. After following the hints and examining the dataset thoroughly with Python, I began to see patterns. Firstly, I noticed that every letter of the alphabet(uppercase and lowercase), as well as all numbers from 0-9(except 5), appear at least once; that means if there are 61 possible combinations for each output digit, the number of possible outcomes is 61^3. I also started noticing irregularities and patterns within the dataset. For one, the numbering system of the output does not follow the typical ordering of a standard base 61 numbering system. For example, input 49443 gives the output "yau", whereas input 49444(one higher) provides the outcome "yap"; however, "p" proceeds "u" in the alphabet and the standard base 61 numbering system. I tried using these discrepancies to map out an ordering system by hand but quickly realized it would be much more efficient to write a program to solve it algorithmically. With Python, I read the data into lists and created a function to figure out the ordering of the numbering system. The algorithm works similarly to how you would convert a base 10 number into a base 62 number by hand. The steps are:

  1. take input in base 10
  2. floor divide the value by 62^2, find the base 62 number/letter that would ordinarily represent that value, switch it with the number/letter of the first digit of the outcome and store it in a hashmap/dictionary
  3. subtract the input by the divided value multiplied by 62^2
  4. repeat steps 1 to 3 on the remainder of the input for 62^1 and 62^0, and their corresponding output places
  5. repeat steps 1 to 4 for all the inputs and corresponding outputs in the dataset
     
This resulted in a hash map with pairs of digits in regular base 62 and their swapped values in the hidden numbering system. Finally, I created a function to convert the input into regular base 62 and switch each number/letter into their paired value in the hashmap to create the desired outcome. I want to note that initially, I had made the mistake of thinking that the outcome was a base 61 numbering system; however, when I ran my program, I got the wrong results. After analyzing the dataset again and trial and error, I realized that no input could be divided by 62 without a remainder. Therefore, the presence of a "0" value would not be present. I then concluded that the missing 5 in the output had to represent that "0" value. I then placed 5 and 0 as pairs in the hashmap before I ran my program to get the correct answers.
