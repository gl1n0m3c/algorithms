graph = {}
graph["you"] = ['alice', 'bob', 'claire']
graph["alice"] = ['peggy']
graph["bob"] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue = graph['you']
searched = []

def person_is_seller(name):
    return name[-1] == 'm'

def search_for_seller():
    global search_queue
    global searched
    i = 0
    while search_queue and i < len(search_queue):
        person = search_queue[i]
        if person_is_seller(person):
            print(person + ' is a mengo seller!')
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
        i += 1
    return False

search_for_seller()