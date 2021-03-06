def tsp_strip(cities, distances):
    '''
    :param cities: file of city names
    :param distances: file of distances between cities
    :return: dictionary of city combinations as keys and the corresponding distance as the value
    '''
    names = open(cities)
    lengths = open(distances)
    global solo_list
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

    return dictionary
    names.close()
    lengths.close()


#tsp_strip('seven_cities_names.txt', 'seven_cities_dist.txt')

from itertools import tee, islice, chain

def item_and_next(some_iterable):
    items, next = tee(some_iterable, 2)
    next = chain(islice(next, 1, None), [None])
    return zip(items, next)


road = ['Alpha', 'Beta', 'Delta', 'Alpha'] #example route


def tsp_distance(route):
    '''
    param route: list of cities names
    Output: total route distance
    '''
    count = 0 #create a count to tally up distances between cities
    for item, next in item_and_next(route): # use item_and_next to find current city and the next one
        pair = (item,next) #make a tuple out of them
        #print (pair)
        if pair in dictionary: #find the distance of the tuple (city pair) in dictionary (which is now global from tsp_strip)
            count = count + float(dictionary[pair]) #add the distance to the count
    #print(count) #return total count when all pair is found
    return(count)

def tsp_greedy(cities, distances, start):
    '''
    :param cities: file of city names
    :param distances: file of distances
    :param start: string, name of starting city
    :return: list of shortest path found by greedy algorithm and total distance of that path
    '''
    tsp_strip(cities,distances) # collect information from files
    current_city = start
    route =[start]
    copy = solo_list # set current city, add to route, create copy of city list to edit
    for cities in range(len(copy)-1): 
        try: solo_list.remove(current_city)
        except: pass
        nearest = 999999 # try to remove current city from list if it has not been removed already, set large intial distance to find smaller values
        for city in solo_list:
            if tsp_distance([current_city,city]) < nearest:
                nearest = tsp_distance([current_city,city]) # loop through to find closest city, update next and distance btw cities
                next = city
            else:
                pass
        route.append(next)
        current_city = next # 'move to' next city in the route
    route.append(start) # after all cities exhausted, return to start
    print(route, '=', tsp_distance(route))
    return(route) # print/return route and distance

tsp_greedy('seven_cities_names.txt', 'seven_cities_dist.txt','Alpha')

global routes
routes = []
def generate_permutations(partial_perm, remaining_chars):
    # If we have a permutation, print it to the screen
    if len(remaining_chars) == 0:
        routes.append(partial_perm)

    # Otherwise, make a recursive call appending each
    # unused character to partial_perm
    else:
        for char in remaining_chars:  # loop over all possible choices
            # Make copies of the lists to pass to the recursive call
            partial_perm_copy = partial_perm.copy()
            partial_perm_copy.append(char)

            remaining_chars_copy = remaining_chars.copy()
            remaining_chars_copy.remove(char)
            generate_permutations(partial_perm_copy, remaining_chars_copy)


generate_permutations([], ['Alpha', 'Beta','Gamma','Delta','Epsilon','Zeta','Eta'])

def tsp_backtracking():
    total = 99999
    keeper = []
    for path in routes:
        path.append(path[0])
        length = tsp_distance(path)
        if length < total:
            total = length
            keeper = path
    print(keeper, '=', total)


tsp_backtracking()
