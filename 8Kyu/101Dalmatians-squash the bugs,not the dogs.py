"""
Your friend has been out shopping for puppies (what a time to be alive!)... He arrives back with multiple dogs, and you simply do not know how to respond!

By repairing the function provided, you will find out exactly how you should respond, depending on the number of dogs he has.

The number of dogs will always be a number and there will always be at least 1 dog.

Good luck!

Bugs

Given code with bugs:

def how_many_dalmatians(n):
  dogs ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
  
  respond = if number <= 10 then dogs[0] else if (number <= 50 then dogs[1] else (number = 101  dogs[3] else dogs[2]
  
return respond
"""

def how_many_dalmatians(n):
    respond = ""
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
  
    if n <= 10:
        respond = dogs[0] 
    elif (n <= 50):
        respond = dogs[1] 
    elif (n == 101):
        respond =dogs[3] 
    else:
        respond = dogs[2]
  
    return respond
  