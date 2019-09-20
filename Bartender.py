# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}
ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def bartender():
    listAns = []
    for i in questions:
       ans = ""
       while ans.lower() not in ("yes","no"):
           ans = input(questions[i] + "\n")
       
       if (ans.lower() == "yes"):
           ran = np.random.randint(0,3)
           listAns.append(i + ": " + ingredients[i][ran])
       elif (ans.lower() == "no"):
           listAns.append(i + ": No")
       else:
           listAns.append("Error")
    return print(*listAns, sep ="\n")
       
bartender()

  
  
  
  
  
  
  