import re
import pandas as pd
import numpy as np


def split_string_by_lengths(text, lengths):
    """
    Splits a string into chunks based on a list of specified lengths.

    Args:
        text (str): The input string to be split.
        lengths (list): A list of integers representing the desired lengths
                        of the chunks.

    Returns:
        list: A list of substrings, each corresponding to a length in 'lengths'.
              If the total length of 'lengths' exceeds the 'text' length,
              the last chunk might be shorter than specified.
    """
    
    result = []
    current_index = 0
    for length in lengths:
        if current_index + length <= len(text):
            result.append(text[current_index : current_index + length])
            current_index += length
        else:
            # Handle cases where the remaining string is shorter than the requested length
            result.append(text[current_index:])
            break  # No more characters to split
    return result


linebag=0
start="no"
arr_len = []
dbinfo = []
kolom = []
with open("awr-hist-1738933432-NAKULA-3366-3564.out") as f:
  for x in f:
    
    if "~~BEGIN-OS-INFORMATION~~" in x:
      start="yes"
      linebag=linebag+1
    else: 
      if "~~END-OS-INFORMATION~~" in x:
        start="no"
        linebag=0
        break 
      if start == "yes":
          if linebag == 1:
            linebag=linebag+1
            head = re.split("\\s+", x)
            head = list(filter(None, head))
            data = np.empty(shape=(0,len(head)))
            #print(data)
            print(head)
          else:
            if linebag == 2:
              body = re.split("\\s+", x)
              body = list(filter(None, body))
              for i in range(len(body)):
                arr_len.append(len(body[i])+1)                              
              linebag=linebag+1
              #print(arr_len)
            else:
              if linebag > 2:
                #print(body)
                #body_float = [float(s) for s in body]
                #body_float = np.array(body_float) 
                #body = np.vstack((body))
                #data = np.vstack((data,body_float))
                body = split_string_by_lengths(x, arr_len)
                body = [s.strip() for s in body]
                #print(body)
                if len(body) == len(head):
                  data = np.vstack((data,body))
                #print(data)
                try:
                   value = int(body[1])
                   body[1] = value
                except ValueError:
                   body[1] = body[1]
                
                
                
                dbinfo.append(body[1])
                kolom.append(body[0])
                linebag=linebag+1
dbinfo.append("awr-hist-1738933432-NAKULA-3366-3564.out")
converted_data = np.zeros_like(data, dtype=object) # Use object dtype to allow mixed types

# Iterate through the array and convert numeric strings to integers
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        try:
            # Attempt to convert the element to an integer
            converted_data[i, j] = int(data[i, j])
        except ValueError:
            # If conversion fails (e.g., it's not a valid number), keep the original value
            converted_data[i, j] = data[i, j].strip()
print(data)
print(converted_data)
print(kolom)
print(dbinfo)