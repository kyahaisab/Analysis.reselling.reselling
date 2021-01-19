import json
import pandas as pd
for j1 in range(len("C:/Users/hp/Downloads/New foldersgoes/green1-100")):
    # suppose error accour at 30 then write j1=j1+30 or j1=j1+30
    j1=j1+1
    print(j1)
    print("\n")
    pathjson = "C:/Users/hp/Downloads/New foldersgoes/green1-100/" + str(j1)
    pathcsv = "C:/Users/hp/Downloads/New foldersgoes/greencsv/" + str(j1)+".csv"
    myjsonfile = open(pathjson, 'r')
    jsondata = myjsonfile.read()
    obj13 = json.loads(jsondata)

    list = obj13['ProductActivity']


    df = pd.DataFrame(list)
    print(df)
    df.to_csv(pathcsv)