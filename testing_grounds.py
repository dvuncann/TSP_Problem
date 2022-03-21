from itertools import tee, islice, chain

def item_and_next(some_iterable):
    items, nexts = tee(some_iterable, 2)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(items, nexts)

def tsp_strip(cities, distances):
    '''
    :param cities: file of city names
    :param distances: file of distances between cities
    :return: dictionary of city combinations as keys and the corresponding distance as the value
    '''
    names = open(cities)
    lengths = open(distances)
    solo_list = []
    tuple_list = []
    distance_list = []
    global dictionary
    dictionary = {}


    for word in names: #strip the cities file into a list of names
        solo_list.append(word.strip())

    for item in range(len(solo_list)): #combine the list of names into tuples
        for item_2 in range(len(solo_list)):
            tuple = (solo_list[item], solo_list[item_2])
            tuple_list.append(tuple)

    for row in lengths: #strip the lengths into a list of numbers
        row = row.strip()
        row = row.split(' ')
        for item in row:
            if item != '':
                distance_list.append(item)

    for item in range(len(tuple_list)): #combine the tuple combinations with the corresponding distances between the two
        dictionary[tuple_list[item]] = distance_list[item]

    print (dictionary)
    return dictionary
    names.close()
    lengths.close()

def tsp_distance(route, cities, distances):
    '''
    param cities: file of city names
    param distances: file of distances between cities
    param route: list of cities names
    Output: total route distance
    '''
    count = 0 #create a count to tally up distances between cities
    tsp_strip(cities, distances) #use strip function to get dictionary
    for item, nxt in item_and_next(route): # use item_and_next to find current city and the next one
        pair = (item,nxt) #make a tuple out of them
        print (pair)
        if pair in dictionary: #find the distance of the tuple (city pair) in dictionary (which is now global from tsp_strip)
            count = count + float(dictionary[pair]) #add the distance to the count
    print(count) #return total count when all pair is found

road = ['Alpha', 'Beta', 'Delta', 'Alpha'] #example route

tsp_distance(road, 'seven_cities_names.txt', 'seven_cities_dist.txt')


