def getSimeparData():
    content = loadStrings("http://www.simepar.br/prognozweb/simepar/forecast_by_counties/4106902")
    if content is not None:
        lines = join(content,' ')
        try:
            data = matchAll(str(content),'data: \[(.*?)\]')
            print(data)
            for datum in data:
                print(datum)
        except BaseException as error:
            print('erro')
def setup():
    getSimeparData()
def draw():
    pass