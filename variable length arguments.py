# def person(name,*data):
#     print(name)
#     print(data)
# person('river',34,'nice','nike')

def kid(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

kid('high',who=6,me=5,like='srh')

#firstcase it single star
#where only the first one is considered as name and all others are considered as data
#secondcase we hav
#where the first one is considered as name
#and remaining which are defined as keywords by **kwargs