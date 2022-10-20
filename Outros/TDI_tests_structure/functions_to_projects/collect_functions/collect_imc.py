def collect_name(name):
    try:
        name = name.strip()
        name = name.split(' ')
        name = name[0]
        
        if len(name)<3:
            return None
        
        else:  
            if name.isalpha():
                name = name.lower()
                return name
            
            else:
                return None
        
    except AttributeError:
        return print('The input needs to be a string')
    

