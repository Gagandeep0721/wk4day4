   # Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.
    # example, if this array were passed as an argument:
    #["Telescopes", "Glasses", "Eyes", "Monocles"]

    #All of the strings in the array passed to your function will be different lengths, so you will not have to decide how to order multiple strings of the same length.

def sort_by_length(arr):
    
    new_list = []
    new_dict = {}
    for word in arr:
        new_dict[word] = len(word)
    sorted_new_dict = sorted(new_dict.items(), key = lambda x:x[1])
    for pair in sorted_new_dict:
        new_list.append(pair[0])
    new_dict_items = ["Telescopes", "Glasses", "Eyes", "Monocles"]
    return new_list

#Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
#Write a function which takes a list of strings and returns each line prepended by the correct number.
#The numbering starts at 1. The format is n: string. Notice the colon and space in between.
#Examples: (Input --> Output)
#[] --> []
#a", "b", "c"] --> ["1: a", "2: b", "3: c"]

def number(lines):
    new_list = []
    for i, ch in enumerate(lines, start=1):
        new_list.append(f"{i}: {ch}")
    return new_list

#In this kata, your goal is to write a function which will reverse the vowels in a string. 
# Any characters which are not vowels should remain in their original position. Here are some examples:
#"Hello!" => "Holle!"
#"Tomatoes" => "Temotaos"
#"Reverse Vowels In A String" => "RivArsI Vewols en e Streng"
#For simplicity, you can treat the letter y as a consonant, not a vowel.
#Good luck!

def reverse_vowels(s):
    empty_list=[]
    original_vowels = 'aeiouAEIOU'
    final=''
    for letter in s:
        if letter in original_vowels:
            empty_list.append(letter)
    for x in s:
        if x in original_vowels:
            final += empty_list.pop()
        else:
            final += x
    return final