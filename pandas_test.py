import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


def pivot_table(data,head):
    df = pd.DataFrame(data, columns=head)  
    df['SNAP_ID'] = df['SNAP_ID'].astype(int)
    df['AVG_SESS'] = df['AVG_SESS'].astype(float)
    pivot = df.pivot(index='SNAP_ID', columns='WAIT_CLASS', values='AVG_SESS')
    print(df.to_string(index=False))
    return pivot

linebag=0
start="no"
arr_len = []
with open("awr-hist-1738933432-NAKULA-3366-3564.out") as f:
  for x in f:
    
    if "~~BEGIN-AVERAGE-ACTIVE-SESSIONS~~" in x:
      start="yes"
      linebag=linebag+1
    else: 
      if "~~END-AVERAGE-ACTIVE-SESSIONS~~" in x:
        start="no"
        linebag=0
        break 
      if start == "yes":
        if linebag == 1:
          linebag=linebag+1
        else:
          if linebag == 2:
            linebag=linebag+1
            head = re.split("\\s+", x)
            head = list(filter(None, head))
            data = np.empty(shape=(0,len(head)))
            #print(data)
            print(head)
          else:
            if linebag == 3:
              body = re.split("\\s+", x)
              body = list(filter(None, body))
              for i in range(len(body)):
                arr_len.append(len(body[i])+1)                              
              linebag=linebag+1
              #print(arr_len)
            else:
              if linebag > 3:
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
                linebag=linebag+1
#print(data)

#data = data.remove("")
table_pivot = pivot_table(data,head)
print("============================================")
print(table_pivot.to_string(index=True))
table_pivot.plot(kind='area',stacked=True)
plt.show()
#plotting(table_pivot,head)
       

    