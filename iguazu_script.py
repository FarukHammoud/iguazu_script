import urllib.request
import re
import ssl


def getSimeparData():

    contents = str(urllib.request.urlopen("http://www.simepar.br/prognozweb/simepar/forecast_by_counties/4106902").read())

    #Script temperaturas
    result = re.search('data: \[(.*?)],', contents)
    max_list = str(result.group(1))
    pos_0 = contents.find(result.group(0))
    new_contents = contents[pos_0+1:]
    result_2 = re.search('data: \[(.*?)],', new_contents)
    min_list = str(result_2.group(1))

    min_list = min_list.partition(',')[2].partition(',')
    max_list = max_list.partition(',')[2].partition(',')

    max_1 = max_list[0]
    min_1 = min_list[0]

    max_list = max_list[2].partition(',')[2].partition(',')
    min_list = min_list[2].partition(',')[2].partition(',')

    max_3 = max_list[0]
    min_3 = min_list[0]

    max_list = max_list[2].partition(',')[2].partition(',')
    min_list = min_list[2].partition(',')[2].partition(',')

    max_5 = max_list[0]
    min_5 = min_list[0]

    #Script pluviosidade

    p1 = contents.find('mm')
    contents = contents[p1+1:]

    p2 = contents.find('mm')
    contents = contents[p2+1:]

    p3 = contents.find('mm')
    plu_1_ = contents[p3-5:p3-1]
    plu_1 = ''
    for i in plu_1_:
        if i in '0123456789.':
            plu_1 += i
    contents = contents[p3 + 1:]

    p4 = contents.find('mm')
    contents = contents[p4 + 1:]

    p5 = contents.find('mm')
    plu_3_ = contents[p5-5:p5 - 1]
    plu_3 = ''
    for i in plu_3_:
        if i in '0123456789.':
            plu_3 += i
    contents = contents[p5 + 1:]

    p6 = contents.find('mm')
    contents = contents[p6 + 1:]

    p7 = contents.find('mm')
    plu_5_ = contents[p7 - 5:p7 - 1]
    plu_5 = ''
    for i in plu_5_:
        if i in '0123456789.':
            plu_5 += i


    return [float(min_1),float(max_1),float(plu_1),float(min_3),float(max_3),float(plu_3),float(min_5),float(max_5),float(plu_5)]

def getClimatempoData():

    context = ssl._create_unverified_context()
    contents = str(urllib.request.urlopen("https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/271/curitiba-pr", context=context).read())

    #Script temperaturas
    max_1_ = str(re.search('tempMax1\">(.*?)<\/p>', contents).group(1))
    max_3_ = str(re.search('tempMax3\">(.*?)<\/p>', contents).group(1))
    max_5_ = str(re.search('tempMax5\">(.*?)<\/p>', contents).group(1))
    min_1_ = str(re.search('tempMin1\">(.*?)<\/p>', contents).group(1))
    min_3_ = str(re.search('tempMin3\">(.*?)<\/p>', contents).group(1))
    min_5_ = str(re.search('tempMin5\">(.*?)<\/p>', contents).group(1))

    max_1,max_3,max_5,min_1,min_3,min_5,plu_1,plu_3,plu_5 = '','','','','','','','',''

    for letra in max_1_:
        if letra in '0123456789.':
            max_1 += letra

    for letra in max_3_:
        if letra in '0123456789.':
            max_3 += letra

    for letra in max_5_:
        if letra in '0123456789.':
            max_5 += letra

    for letra in min_1_:
        if letra in '0123456789.':
            min_1 += letra

    for letra in min_3_:
        if letra in '0123456789.':
            min_3 += letra

    for letra in min_5_:
        if letra in '0123456789.':
            min_5 += letra



    cut = contents.find('forecastRollingChart')
    contents = contents[cut+1:]

    p1 = contents.find('mm')
    plu_1_ = contents[p1-4:p1]

    cut = contents.find('forecastRollingChart')
    contents = contents[cut + 1:]
    cut = contents.find('forecastRollingChart')
    contents = contents[cut + 1:]

    p3 = contents.find('mm')
    plu_3_ = contents[p3 - 4: p3 ]

    cut = contents.find('forecastRollingChart')
    contents = contents[cut + 1:]
    cut = contents.find('forecastRollingChart')
    contents = contents[cut + 1:]

    p5 = contents.find('mm')
    plu_5_ = contents[p5 - 4: p5]

    for letra in plu_1_:
        if letra in '0123456789.':
            plu_1 += letra

    for letra in plu_3_:
        if letra in '0123456789.':
            plu_3 += letra

    for letra in plu_5_:
        if letra in '0123456789.':
            plu_5 += letra

    return [float(min_1), float(max_1), float(plu_1), float(min_3), float(max_3), float(plu_3), float(min_5),float(max_5), float(plu_5)]
def getAccuWeatherData():
    context = ssl._create_unverified_context()
    contents = str(urllib.request.urlopen("https://www.accuweather.com/pt/br/curitiba/44944/daily-weather-forecast/44944?day=2",context=context).read())
def getFreeMeteoData():
    context = ssl._create_unverified_context()
    contents = str(urllib.request.urlopen("https://freemeteo.com.br/clima/curitiba/7-dias/lista/?gid=3464975&language=portuguesebr&country=brazil",context=context).read())

    cut = contents.find('o<br><b>')
    contents = contents[cut + 1:]

    cut = contents.find('o<br><b>')
    plu_1_ = contents[cut:cut + 12]
    contents = contents[cut + 1:]
    cut = contents.find('x.:')
    max_1_ = contents[cut:cut+6]
    cut = contents.find('n.:')
    min_1_ = contents[cut:cut + 6]


    contents = contents[cut + 1:]
    cut = contents.find('o<br><b>')
    contents = contents[cut + 1:]

    cut = contents.find('o<br><b>')
    plu_3_ = contents[cut:cut + 12]
    contents = contents[cut + 1:]
    cut = contents.find('x.:')
    max_3_ = contents[cut:cut + 6]
    cut = contents.find('n.:')
    min_3_ = contents[cut:cut + 6]

    contents = contents[cut + 1:]
    cut = contents.find('o<br><b>')
    contents = contents[cut + 1:]

    cut = contents.find('o<br><b>')
    plu_5_ = contents[cut:cut + 12]
    contents = contents[cut + 1:]
    cut = contents.find('x.:')
    max_5_ = contents[cut:cut + 6]
    cut = contents.find('n.:')
    min_5_ = contents[cut:cut + 6]

    max_1, max_3, max_5, min_1, min_3, min_5, plu_1, plu_3, plu_5 = '', '', '', '', '', '', '', '', ''

    for letra in max_1_:
        if letra in '0123456789,':
            if letra == ',':
                max_1 += '.'
            else:
                max_1 += letra

    for letra in max_3_:
        if letra in '0123456789,':
            if letra == ',':
                max_3 += '.'
            else:
                max_3 += letra

    for letra in max_5_:
        if letra in '0123456789,':
            if letra == ',':
                max_5 += '.'
            else:
                max_5 += letra

    for letra in min_1_:
        if letra in '0123456789,':
            if letra == ',':
                min_1 += '.'
            else:
                min_1 += letra

    for letra in min_3_:
        if letra in '0123456789,':
            if letra == ',':
                min_3 += '.'
            else:
                min_3 += letra

    for letra in min_5_:
        if letra in '0123456789,':
            if letra == ',':
                min_5 += '.'
            else:
                min_5 += letra
    for letra in plu_1_:
        if letra in '0123456789,':
            if letra == ',':
                plu_1 += '.'
            else:
                plu_1 += letra

    for letra in plu_3_:
        if letra in '0123456789,':
            if letra == ',':
                plu_3 += '.'
            else:
                plu_3 += letra

    for letra in plu_5_:
        if letra in '0123456789,':
            if letra == ',':
                plu_5 += '.'
            else:
                plu_5 += letra

    return [float(min_1), float(max_1), float(plu_1), float(min_3), float(max_3), float(plu_3), float(min_5),float(max_5), float(plu_5)]

def getTempoAgoraData():

    contents = str(urllib.request.urlopen("http://www.tempoagora.com.br/previsao-do-tempo/pr/Curitiba/").read())

    #Script todos
    result = re.search('\"icon-weather-1\"></i>(.*?)<small>', contents)

    contents = contents[contents.find(result.group(0))+150:]

    result = re.search('\"icon-weather-1\"></i>(.*?)<small>', contents)
    result_2 = re.search('\"icon-weather-2\"></i>(.*?)<sup>', contents)
    result_3 = re.search('\"icon-weather-3\"></i>(.*?)<sup>', contents)
    plu_1 = str(result.group(1))
    min_1 = str(result_2.group(1))
    max_1 = str(result_3.group(1))

    contents = contents[contents.find(result.group(0)) + 150:]
    result = re.search('\"icon-weather-1\"></i>(.*?)<small>', contents)
    contents = contents[contents.find(result.group(0)) + 150:]

    result = re.search('\"icon-weather-1\"></i>(.*?)<small>', contents)
    result_2 = re.search('\"icon-weather-2\"></i>(.*?)<sup>', contents)
    result_3 = re.search('\"icon-weather-3\"></i>(.*?)<sup>', contents)
    plu_3 = str(result.group(1))
    min_3 = str(result_2.group(1))
    max_3 = str(result_3.group(1))

    contents = contents[contents.find(result.group(0)) + 150:]
    result = re.search('\"icon-weather-1\"></i>(.*?)<small>', contents)
    contents = contents[contents.find(result.group(0)) + 150:]

    result = re.search('\"icon-weather-1\"></i>(.*?)<small>', contents)
    result_2 = re.search('\"icon-weather-2\"></i>(.*?)<sup>', contents)
    result_3 = re.search('\"icon-weather-3\"></i>(.*?)<sup>', contents)
    plu_5 = str(result.group(1))
    min_5 = str(result_2.group(1))
    max_5 = str(result_3.group(1))

    return [float(min_1), float(max_1), float(plu_1), float(min_3), float(max_3), float(plu_3), float(min_5),float(max_5), float(plu_5)]
print(getSimeparData())
print(getClimatempoData())
print(getTempoAgoraData())
print(getFreeMeteoData())
#getAccuWeatherData()