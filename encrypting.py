"""
Code to decript and encrypt a given string
"""

import math
from itertools import zip_longest as zl



def encrypt(txt, n_times):
    """
    This function enrypts the string puted as an argument
    to string with chars mixed up ---> [::2]. It mixes the elements in a string n times
    """
    if n_times<= 0:
        out_text = txt
    else:
        loop = 0
        l_txt = list(txt)
        end = l_txt[::2]
        beg = l_txt[1::2]
        new_string = beg + end
        while loop < (n_times - 1) and n_times>1:
            end = new_string[::2]               #every secound char
            beg = new_string[1::2]              #every secound char, starting from secound char
            new_string = beg+end                #creating new string for a loop
            loop = loop + 1
    out_text = "".join(new_string)
    return out_text




def decrypt(encrypted_text, n_times):
    """
    This function decrypt string puted as an argument.
    It restore the oryginal array
    and to do so it iter itself n times through while loop
    """
    if n_times<=0:
        l_enc = encrypted_text
    else:
        loop = 0
        j_list_tuple = []
        l_enc = list(encrypted_text)
        while loop<n_times:
            len_enc = len(l_enc)
            beg = l_enc[math.floor((len_enc/2)):]
            end = l_enc[:math.floor((len_enc/2))]
            zip_enc = tuple(zl(beg,end,fillvalue=""))
            loop += 1
            for elem in zip_enc:
                j_tuple = "".join(elem)
                j_list_tuple.append(j_tuple)
                l_enc = "".join(list("".join(j_list_tuple)))
            j_list_tuple = []

    return l_enc


