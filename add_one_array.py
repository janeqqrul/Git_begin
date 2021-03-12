"""
This code make matemathical operations on given array
if elem in array is_numeric
"""
def up_array(arr):
    """Function adds 1 to numeric array"""
    if arr == []:
        fin =  None
    else:
        global string_one
        arrs = []
        fin = []
        for elem in arr:
            if arr == [] or elem<0 or len(str(elem))!=1:
                fin =  None
            else:
                elem = str(elem)
                arrs.append(elem)
                joine = "".join(arrs)
                add_one = int(joine) +1
                string_one = str(add_one)
        for elem in string_one:
            elem = int(elem)
            fin.append(elem)
    return fin

