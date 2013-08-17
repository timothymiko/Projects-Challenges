Vigenere/Vernam/Caesar Ciphers
------------------------------
Solution: Ciphers.py

Difficulty: 5

Description: Want to get into the basics of encryption? Well a great place to start is with these three ciphers. Create a program which implements these three encryption methods. Ask the user for a string, or file to read, and have the text run through each of these ciphers. Let the use choose whether to output the data to the screen or back to another file.

Tips: First stop, Wikipedia to learn how these ciphers work. Start with the Caesar cipher which is essentially a shifting of the alphabet. Take the letter “a” and shift it down 4 and you have “e” and a “b” becomes the letter “f”. Once you have this program working, then you can move onto the Vigenere cipher which uses shifts to come up with a more elaborate system of encryption.

Count Vowels
------------
Solution: CountVowels.py

Difficulty: 2

Description: Make a program which asks the user to enter in a string and then prints out how many vowels are in that string. For example, the user enters “hello world” and it returns “There are 3 vowels in ‘hello world’”.

Tips: Strings are typically thought of and used as an array of characters. If you can loop through these characters one by one, you can compare them to a list of vowels. If you find one that matches, increment a counter variable. After the loop is done, the counter will then contain your count.

Added Difficulty: Count the consonants as well as spaces. Provide a mini report of all these counts.

Check if Palindrome
-------------------
Solution: Palindrome.py

Difficulty: 2

Description: A palindrome is a string of characters when read from left to right and right to left is exactly the same (ignoring any spaces usually). One of the most well known palindromes is “race car”. No matter which direction you read it, it still reads “race car”. Create a program which checks if a string entered is a palindrome. If it is, print “The string ‘_____’ is a palindrome” where the blank is the string they entered.

Tips: Simple approach, take the string, reverse it and compare. Depending on the language, you might want to take special precautions in first making sure things like spaces are stripped out. Also make sure you are comparing the strings value, not if two strings are the same object! (This goes for you Java users)

Added Difficulty: If you hadn’t done it already, write the reversing function yourself. Don’t rely on a version provided by the language.

Pig Latin - Simple
------------------
Solution: PigLatin.py

Difficulty: 4
Description: Ask the user to enter in a string which will then be printed back to screen in Pig Latin. If the user enters “hello world” it will be printed back to them as “ello-hay orld-way”.

Tips: First break the string into words. This can usually be accomplished by some sort of split function. Validate the first character of each word and simply apply the rules of Pig Latin. If it is a consonant, strip it off the word and append it to the end with “ay”. If it is a vowel, simply attach “way” or “ay” (depending on the variant you wish to use). Be sure to also check for consonant clusters like “qu” and move them both if need to. Validate the word first and then decide what approach to take to that word. Join the words back together after all transformations have been made. I would ignore analyzing compound words for syllables.

Added Difficulty: Analyze words to see if they are compound words and then apply the appropriate rule to those types of words.

Reverse a String
----------------
Solutions: Reverse.py, ReverseString.java

Difficulty: 1

Description: Create a program that asks the user for a string of input and simply returns it in reverse order. For instance they enter “Hello” and it returns “olleH”.

Tips: Keep in mind that a string is often treated as an array of individual characters. In C/C++ based languages this list ends with a terminating character ‘\0’. One of the fastest ways to reverse a string is simply to swap each character as you work your way inward. So for instance, you would swap “H” with “o” and then “e” with “l” etc. To do this, use a loop that continues until the start meets or surpasses the end. Make sure not to swap the terminator itself!

Added Difficulty: None

Count Words in a String
-----------------------
Solution: WordCount.py

Difficulty: 2

Description: Write a program which asks the user for a string and then counts how many words are in that string. For example if they write “This is my first program” the program would print out “There are 5 words”.

Tips: Depending on the language you are using, this can be wickedly simple or a bit more difficult. For languages that have a built in split function, you can split the string on the spaces and then simply count the pieces in the resulting array. If the language doesn’t support a split, you will need to loop through the string and when a space (or end of the string) is encountered, you know you are at the end of a word. For each word you can increment a counter.

Added Difficulty: Along with word counter, count the number of sentences and paragraphs.
