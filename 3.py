import re
def isPythonId(id):    
    pattern = '(^\d{15}$)|(^\d{17}([0-9]|x)$)'    
    matchObject = re.search(pattern, id)    
    if matchObject is None:        
        print('%s is not Id' % id)    
    else:        
        print('%s is Id' % id)
isPythonId('340803200407162245') 
isPythonId('34082004071622i5') 
isPythonId('34082004071622452') 