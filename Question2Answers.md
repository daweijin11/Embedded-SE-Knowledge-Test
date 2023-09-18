Q2 a) The function converts the input to a unique base 62 numbering system, swapping its values with those in the original base 62 numbering system. For example, the value "5" could represent "7", and "P" could mean "2".

The conversions are shown in the following hashmap, where the keys represent the value in base 62, and the values represent their corresponding value in the output's numbering system:

{'0': '5', '4': 'c', '7': 'G', 'U': 'p', 'H': 'm', 'Z': 'W', 'f': 'X', 'N': '3', 'O': 'B', 'u': 't', 'o': 'R', 'z': 'k', 'E': 'N', '5': 'P', 'K': 'V', 'q': 'g', 'M': 'D', 'g': '4', '6': 'M', 'h': 'Y', 'j': 'S', 'd': 'L', 'l': 'U', 'n': 'I', 'W': 'E', 'v': 'r', 'w': 'K', 'G': 'd', 'D': 'T', '8': 'v', '2': 'x', 'I': 'w', 'a': '9', '9': 'z', 'A': 'A', 'i': 'j', 'S': 'O', 'T': 'u', 'Y': '1', 't': 'F', 'Q': 'H', 'x': 'l', 'e': 'Q', 'b': 's', 'c': 'q', 'B': 'Z', 'C': 'y', 'm': 'h', 'X': '2', '3': 'i', 'r': 'a', '1': '7', 'V': '8', 'J': 'n', 's': 'f', 'k': 'e', 'F': 'o', 'R': '0', 'P': '6', 'p': 'J', 'y': 'b', 'L': 'L'}

A simple way to understand this function is to imagine a function that converts a base 10 number(input) to a regular base 62 number and then switches each number with its corresponding value in the hashmap above to produce the output.

Q2 b) f(30001) = "GIF",
      f(55555) = "NOi",
      f(77788) = "VNQ"

Q2 C) The upper bounds of the function depend on the system it is running on. For a 32-but system, the maximum integer possible is 2,147,483,647, which converts to "xLVqs7" through the function. For a 64-bit system, the maximum integer possible is 9,223,372,036,854,775,807, which converts to "AkLvI51PvhG". I also noticed that all outputs contain 3 "numbers." If numbers can only hold up to 3 spaces, then the maximum would be 62^3 - 1 = 238327, which converts to "kkk" through the function.




