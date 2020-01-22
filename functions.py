import csv

with open('data.csv') as f:
    # we are using DictReader because we want our information to be in dictionary format.
    reader = csv.DictReader(f)
    # some more code
    listofdicts = [x for x in reader]
#     for x in reader:   #for loop is in the with block for some reason because reader is not global variable
#         listofdicts.append(x)
        
listofdicts



def findbyname(string):
    for x in listofdicts:
        if x['album'] == string:
            return x
    else:
        return None
        
findbyname('Revolver')



def findbyrank(rank):
    for x in listofdicts:
        if x['number'] == rank:
            return x['album']
    else:
        return None

findbyrank('2')



def findbyyear(year):
    yearslist1 = []
    for x in listofdicts:
        if x['year'] == year:
            yearslist.append(x['album'])
    return yearslist

findbyyear('1966')



def findbyyears(start, end):
    yearslist2 = []
    for x in listofdicts:
        if (int(x['year']) >= start) and (int(x['year']) <= end):
            yearslist2.append(x['album'])
    return yearslist2

findbyyears(1989,1990)



def findbyranks(start, end):
    ranklist = []
    for x in listofdicts:
        if (int(x['number']) >= start) and (int(x['number']) <= end):
            ranklist.append(x['album'])
    return ranklist

findbyranks(2,5)



def alltitles(yourlist):
    return [x['album'] for x in yourlist]

alltitles(listofdicts)



def allartists(yourlist):
    return [x['artist'] for x in yourlist]

allartists(listofdicts)



def mostalbums(yourlist):
    mydict = {}
    currentmaxval = 0
    currentmax = {}
    for x in set(allartists(yourlist)):    #gives dictionary of album name: count
        mydict[x] = allartists(listofdicts).count(x)  
    for k,v in mydict.items():    #searches for highest value (count)
        if v > currentmaxval:
            currentmaxval = v
    for k,v in mydict.items():    #searches for pairs whose values are highest
        if v == currentmaxval:
            currentmax[k] = v
    return currentmax

mostalbums(listofdicts)



def mostword(yourlist):
    wordstocount = {}
    mergedwords = []
    currentmaxval = 0
    currentmax = {}
    for eachtitle in alltitles(yourlist):  #iterate through each title name to make each word an element
        mergedwords.extend(eachtitle.split(' '))
    for x in set(mergedwords):    #gives dictionary of word:count
        wordstocount[x] = mergedwords.count(x)
    for k,v in wordstocount.items():    #find highest value (count) in dictitems
        if v > currentmaxval:
            currentmaxval = v
    for k,v in wordstocount.items():    #finds all pairs whose values are highest
        if v == currentmaxval:
            currentmax[k] = v
    return currentmax

mostword(listofdicts)



import matplotlib as plt
%matplotlib inline
import math
def albumsbydecades(yourlist):
    albumtoyear = {}
    for x in listofdicts:    #gives dictionary of album name:year to find min&max years. 
                             #don't really need to make a dictionary because we don't need album name but it's fine
        albumtoyear[x['album']] = int(x['year'])
    mindecade = math.floor(min(albumtoyear.values())/10)*10    #min decade
    maxdecade = math.ceil(max(albumtoyear.values())/10)*10    #max decade
    listofdecades = []    #will have a list of the start of each decade
    while mindecade < maxdecade:
        listofdecades.append(mindecade)
        mindecade += 10
    countbydecade = []    #will have a list of counts by decade
    for x in listofdecades:
        countbydecade.append(len(findbyyears(x,x+9)))
    return plt.pyplot.bar(listofdecades,countbydecade,width=10,edgecolor='black')

plt.pyplot.xlabel('Decades')
plt.pyplot.ylabel('Albums Released')
plt.pyplot.title('Albums Released Per Decade')

albumsbydecades(listofdicts)



import matplotlib as plt
%matplotlib inline

from collections import defaultdict
genrecount = defaultdict(int)

def albumsbygenre(yourlist):
    cleanlist1 = []
    cleanlist2 = []
    cleanlist3 = []
    cleanlist4 = []
    genres = [x['genre'] for x in listofdicts]
    genres = [x.split(', ') for x in genres]
    for x in genres:
        cleanlist1.extend(x)
    genres = [x.split(' & ') for x in cleanlist1]
    for x in genres:
        cleanlist2.extend(x)
    genres = [x.split('& ') for x in cleanlist2]
    for x in genres:
        cleanlist3.extend(x)
    genres = [x.split(',') for x in cleanlist3]
    for x in genres:    
        cleanlist4.extend(x)
    for genre in cleanlist4:
        genrecount[genre] += 1
    genrecount.pop('')
    return dict(genrecount) #plt.pyplot.bar(,width=10,edgecolor='black')

albumsbygenre(listofdicts)

plt.pyplot.bar(genrecount.keys(),genrecount.values(),edgecolor = 'black')

plt.pyplot.xlabel('Genres')
plt.pyplot.ylabel('Albums Released')
plt.pyplot.title('Albums Released Per Genre')
plt.pyplot.xticks(rotation = 90)



