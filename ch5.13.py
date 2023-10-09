import distance
def distances():
    for t in range(1,11):
        dista=distance.falling_distance(t)
        print(f'{t} seconds falling in distance of {dista:,.3f} meter')
distances()
