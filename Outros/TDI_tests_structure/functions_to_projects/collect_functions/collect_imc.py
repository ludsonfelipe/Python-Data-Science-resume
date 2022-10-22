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
    
def collect_metrics(weight, height):
    try:
        weight = float(weight)
        height = float(height)

        if weight > 1000 or weight < 0.1:
            return 'O peso inserido na calculadora não pode ser maior que 1000 ou menor que 0.1'
        if height > 3 or height <0.1:
            return 'A altura inserida na calculadora não pode ser maior que 3 metros ou menor que 0.1'
    
        return weight,height

    except:
        return None

def others():
    pass