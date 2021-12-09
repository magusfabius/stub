# thanks to the universe
# sometimes you got to insert an error. Murphy tearhy ... I think that everything will appen at some point ... you choose the universe and bring who's near you in the black hell hole (which is psycho but physical at the same time)

import time
from random import randrange

#quantistic python library

print(randrange(10))

# binary return
# #TODO: different random type of results

def alea_iacta_est():
    i = 0
    play = True
    user_seed = input("type a number o just something ... it will be translated in a integer in any way: ")
  
    # alea in hands
    start_counter = time.time()
    alea_iact = input("Press y to continue or something else to abort...")
    
    if alea_iact == "y":
        end_counter = time.time()
        delta = int((end_counter - start_counter)*1000)
        print("alea in hand for: ", delta)

        delta_randomized = int(randrange(delta))
        print(delta_randomized)

        random_int = randrange(int(delta_randomized * user_seed))
        print("final result: ", random_int)

    else:
        #abort
        print("aboarting, no enter command pressed")

    """
    while play:

        print(i)
        i = i + 1
    """

alea_iacta_est()

        
