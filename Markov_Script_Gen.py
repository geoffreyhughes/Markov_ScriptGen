#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:45:27 2019

@author: Geoffrey Hughes & Murphy Studebaker
"""




import pandas as pd
from numpy.random import choice


def choose_word(current_word):
    return choice(unique_words, 1, p=first_order_matrix[unique_words.index(current_word)])




words = []
unique_words = []
starter_words = []


with open("The_Godfather.txt") as f:
    words = f.read().split()
    
with open("Inglourious_Basterds.txt") as f:
    words += f.read().split()
    
# May include as many .txt files as wanted; I like the sentences these movies make, though.




for word in words:
    if word in unique_words:
        n=0
        
    else:
        unique_words.append(word)
        
        

p_start = [0.0] * len(unique_words)
p_start_sum = 0





        
# Find words to begin sentence and store them in starter_words
for word in words:
    if "." or "!" or "?" in word:
        index = words.index(word) + 1
        
        if index < len(words):
            start_word = words[index]
        
            start_word_index = unique_words.index(start_word)
            p_start[start_word_index] += 1
            p_start_sum += 1
            
            
            
            
# Calculate Probabilities          
index = 0
while (index < len(p_start)):
    p_start[index] /= p_start_sum
    index += 1
    
    
    
    
num_unique_words = len(unique_words)    
first_order_matrix = [[0.0 for x in range(num_unique_words)] for y in range(num_unique_words)]
curr_word_index = 0
        



# Fill in matrix with counts of how many times a word occurs next after the given word
for word in words:
    row_index = unique_words.index(word)
    following_word_position = curr_word_index + 1
    
    if following_word_position < len(words):
        following_word = words[following_word_position]
    
    col_index = unique_words.index(following_word)
    first_order_matrix[row_index][col_index] += 1
    curr_word_index += 1
    
    
    
    
# Calculate Probabilities              
for row in range(num_unique_words):
    row_sum = sum(first_order_matrix[row])
    for column in range(num_unique_words):
        first_order_matrix[row][column] /= row_sum    




# 'the' is index 45
#print(first_order_matrix[45])




script = ""
first_word = choice(unique_words, 1, p=p_start)
curr_word = first_word




# Write the movie script!
word_count = 0
while (word_count < 1000):
    
    script += curr_word[0] + " " 
    curr_word = choose_word(curr_word)
    word_count += 1

print(script)



#print(starter_words)



