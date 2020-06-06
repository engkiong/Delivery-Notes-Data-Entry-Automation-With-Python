

import os

def getfiles(folder,f_type):
    '''
    folder = the name of the interested folder within the current working directory
    f_type = the type of file example '.pdf' etc
    
    '''
    current_dir = os.getcwd()
    dir = '\\'.join([current_dir, folder])
    result = [item[2] for item in list(os.walk(dir)) if item[2]]
    final = [item for each in result for item in each]
    return [file for file in final if file.find(f_type) != -1]
print(getfiles('formats','.pdf'))

