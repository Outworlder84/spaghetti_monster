def check_numbers(plate):
    #invalid_strings = ["LNL","LNNL","LNNNL","LNNNNL"]
    code_list = []
    if len(plate) == 2:
        return True
    elif len(plate) >= 3:
        for i in range(len(plate)):
            if plate[i].isalpha():
                code_list.append("L")
            else:
                code_list.append("N")
        code_list_string = "".join(code_list)
        #print(code_list_string)
        if code_list_string.count("LNL"):
            #print("LNL fail")
            return False
        elif code_list_string.count("LNNL"):
            #print("LNNL fail")
            return False
        elif code_list_string.count("LNNNL"):
            #print("LNNNL fail")
            return False
        elif code_list_string.count("LNNNNL"):
            #print("LNNNNL fail")
            return False
        else:
            return True
