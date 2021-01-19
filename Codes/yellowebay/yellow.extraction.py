import bs4
import pandas as pd
for i in range(len(r"C:/Users/hp\Downloads\New foldersgoes/yellow")):
    # If any error will come, lets say at k=55, then change k1=i+55
    k1=i+1
    path="C:/Users/hp/Downloads/New foldersgoes/yellow/"+str(k1)+".html"        # source
    path1=r"C:\Users\hp/Downloads/New foldersgoes/yellowcsv/"+str(k1)+".csv"    #destination
    file=open(path,"r", encoding = 'utf-8')
    # using r in prefix u can use eithr / or \ etc
    #print(type(file))
    soup = bs4.BeautifulSoup(file,'html.parser')
    #print(type(soup))
    averagesalesprice="notdefined"
    for links in soup.find('title'):
        name = links
        #print("Name:   ", name)

    for links1 in soup.find('span', attrs={'class', 'sneak-score'}):
        condition = links1
        #print("Condition: ", condition)
    for links2 in soup.find('span', attrs={'class', 'soft-black'}):
        ticker = links2
        #print("Ticker: ", ticker)
    for links3 in soup.find('a', attrs={'class', 'sneak-score'}):
        authentic = links3
        #print("Authentic: ", authentic)
        mn = 0
    for links4 in soup.find_all('div', attrs={'class', 'detail'}):
        lm = links4.find_all('span')
        # print(lm)
        ll = pd.DataFrame(lm)
        # print(ll)
        x = pd.DataFrame(ll[0][2])
        xy = x[0][0]
        if mn == 0:
            style = xy
            #print("Style: ", style)
        if mn == 1:
            colourway = xy
            #print("Colourway", colourway)
        if mn == 2:
            reatailprice = xy
            #print("Retail Price: ", reatailprice)
        if mn == 3:
            releasedate = xy
            #print("Release Date: ", releasedate)
        mn = mn + 1;
    ab = 0
    for links5 in soup.find('div', attrs={'class', 'value-container'}):
        hl = pd.DataFrame(links5)[0][0]  # like in this line place [0][0] or [0][2] etc to get rid of index
        if ab == 0:
            weekhigh = hl[4:]
            #print("52 week High: ", weekhigh)
        if ab == 1:
            weeklow = hl[6:]
            #print("52 week Low:", weeklow)
        ab = ab + 1;
    i = 0
    j = 0
    for links6 in soup.find_all('span', attrs={'class', 'value'}):
        if i == 0:
            trlow = pd.DataFrame(links6)[0][0]
            trhigh = pd.DataFrame(links6)[0][2]
            #print("Trading Range", trlow, "-", trhigh)

        if j == 1:
            volatility = pd.DataFrame(links6)[0][0]
            #print("Volatility: ", volatility)
        i = i + 1
        j = j + 1
    df = 0
    for links7 in soup.find_all('div', attrs={'class', 'gauge-value'}):
        c = pd.DataFrame(links7)[0][0]
        if df == 0:
            noofsales = c
            #print("No of Sales: ", noofsales)
        if df == 1:
            pricepremium = c
            #print("Prive Premium: ", pricepremium)
        if df == 2:
            averagesalesprice = c
           # print("Average Sales Price: ", averagesalesprice)
        df = df + 1

    yellow = {'Name': [name], 'Condition': [condition], 'Ticker': [ticker], 'Authentic': [authentic], 'Style': [style],
              'Colourway': [colourway], 'Retail Price': [reatailprice], 'Release Date': [releasedate],
              '52week High': [weekhigh], '52week Low': [weeklow], 'TradingRange': [trlow + trhigh],
              'Volatility': [volatility], 'Nomof Sales': [noofsales], 'Price Premium': [pricepremium],
              'Average Sales Price': [averagesalesprice]}
    yellow1 = pd.DataFrame(yellow)
    #print(yellow1)
    print(k1)
    print('\n')

    yellow1.to_csv(path1)
