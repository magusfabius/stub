# pip install psutil

import psutil

def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username', 'cpu_percent', ])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           print("EXCEPTION: ", proc)
           pass


    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects


#process_list = getListOfProcessSortedByMemory()


# Iterate over all running process
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        #pinfo = proc.as_dict(attrs=['pid', 'name', 'username', 'cpu_percent', ])
        pinfo = proc.as_dict()
        processName = proc.name()
        #processID = proc.pid
        #print(processName , ' ::: ', processID)

        print(processName, " -> ", pinfo)
        print()
    except Exception as e:
        print("EXCEPTION: ", e)


