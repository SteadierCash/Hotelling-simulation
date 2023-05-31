# import random
import matplotlib.pyplot as plt
# import numpy as np
# import statistics as st
#
#
# import matplotlib.pyplot as plt
import numpy as np
import random


class Player:
    def __init__(self, player_number, place, price, quality):
        self.player_number = player_number
        self.place = place
        self.price = price
        self.quality = quality
        self.cost = 0
        self.utility = 0

    def calculate_cost(self, i):
        self.cost = (((abs(i - self.place) + 1) / 100) ** 2) * 0.4\
                    + ((self.price / 10) ** 2) * 0.4\
                    - ((self.quality / 10) ** 2) * 0.2

    def calculated_utility(self, utility):
        self.utility = utility

    def new_place(self, iteration, l):
        left = self.place - (iteration - 999) * 2
        right = self.place + (iteration - 999) * 2

        if self.player_number == 1:

            if left < 1:
                left = 1
            if right > 500:
                right = 500

        elif self.player_number == 2:

            if left < 500:
                left = 500
            if right > l:
                right = l
        self.place = random.randint(left, right)

    def new_price(self, iteration):
        left = self.price - (iteration + 1) * 2
        right = self.price + (iteration + 1) * 2

        if left < self.quality:
            left = self.quality
        if right > 40:
            right = 40

        self.price = random.randint(left, right)

    def new_quality(self, iteration):
        left = self.quality - (iteration - 999) * 2
        right = self.quality + (iteration - 999) * 2

        if left < 10:
            left = 10
        if right > 30:
            right = 30

        self.quality = random.randint(left, right)

    def __copy__(self):
        return Player(self.player_number, self.place, self.price, self.quality)

    def write(self):
        return self.place, self.price, self.quality, self.utility


def utilhelp(players_list, l):

    utility = []

    player_number_list = []
    same_val_list = []
    #local_same_val = []

    for i in range(1, l + 1):

        for player in players_list:
            player.calculate_cost(i)
            #players_list.append(player)

        min_nr = players_list[0].player_number
        min_cost = players_list[0].cost

        same = False

        for k in range(1, len(players_list)):

            if players_list[k].cost < min_cost:
                min_nr = players_list[k].player_number
                min_cost = players_list[k].cost

            elif players_list[k].cost == min_cost:
                same_val_list.append(players_list[k].player_number)
                same_val_list.append(min_nr)
                same = True

        if min_cost < 6 and same is False:
            player_number_list.append(min_nr)
        else:
            continue

    for element in players_list:
        count = player_number_list.count(element.player_number)
        element.calculated_utility(count)

    for element2 in same_val_list:
        for player2 in players_list:
            if element2 == player2.player_number:
                player2.utility += 0.5

    for player in players_list:
        player.utility = player.utility * player.price

    return players_list


def util(poz, l):

    dist_poz = []
    dist_all_poz = []
    full_sublist = []

    for sublist in poz:
        full_sublist.append([sublist.place, sublist.price, sublist.quality])
        if [sublist.place, sublist.price, sublist.quality] not in dist_poz:
            dist_poz.append([sublist.place, sublist.price, sublist.quality])
            dist_all_poz.append(sublist)

    if len(dist_poz) == len(poz):
        utility_final = utilhelp(poz, l)
        return utility_final

    else:
        dist_players_list = utilhelp(dist_all_poz, l)

        cnt_list = []

        for pozycja in dist_poz:
            count = full_sublist.count(pozycja)
            cnt_list.append([pozycja[0], pozycja[1], pozycja[2], count])

        for player in dist_players_list:
            for cnt in cnt_list:
                if player.place == cnt[0] and player.price == cnt[1] and player.quality == cnt[2]:
                    val = player.utility / cnt[3]
                    player.calculated_utility(val)

        for player in poz:
            for dist_player in dist_players_list:
                if player.place == dist_player.place and player.price == dist_player.price and player.quality == dist_player.quality:
                    player.calculated_utility(dist_player.utility)

        return poz


def nash(poz, num_poz, l):

    product = poz
    # util_list = []
    #
    # for position in full_list:
    #     util_list.append(position[1])

    higher_val = False
    counter = 0

    while not higher_val and counter < 10000:

        if poz[num_poz].utility == 1000:
            print('brak lepszej pozycji!')
            break

        counter += 1
        #new_price = random.randint(20, 30)
        poz_list_2 = [elem.__copy__() for elem in poz]

        if (0 < counter < 1000):# or counter >= 3000:
            poz_list_2[num_poz].new_price(counter)

        if (1000 <= counter < 2000) or counter >= 3000:
            poz_list_2[num_poz].new_quality(counter)
            poz_list_2[num_poz].new_price(counter)

        if (2000 <= counter < 3000) or counter >= 3000:
            poz_list_2[num_poz].new_place(counter, l)

        full_list_2 = util(poz_list_2, l)


        #print(f'próba {counter} - {full_list_2}')

        if full_list_2[num_poz].utility > poz[num_poz].utility:
            higher_val = True
            product = full_list_2

    if counter == 10000:
        print("Brak lepszej pozycji!")

    return product
    # print(f"war {ux, uy, uz, ut}")

# print(util([[100, 20], [400, 5], [600, 25]], 1000))
# print(nash([[100, 20], [400, 5], [600, 25]], 0, 1000))
# print("great")


def main():
    outcome = []
    outcome_pos = []

    l = 1000

    for i in range(1):

        x_poz = random.randint(1, 500)
        x_quality = random.randint(10, 30)
        x_price = random.randint(x_quality, 40)

        y_poz = random.randint(500, l)
        y_quality = random.randint(10, 30)
        y_price = random.randint(y_quality, 40)

        # z_poz = random.randint(1, l)
        # z_price = random.randint(10, 30)
        # z_quality = random.randint(10, 30)

        # t_poz = random.randint(1, l)
        # t_price = random.randint(10, 30)
        # t_quality = random.randint(10, 30)

        x = Player(1, x_poz, x_price, x_quality)
        y = Player(2, y_poz, y_price, y_quality)
        #z = Player(3, z_poz, z_price, z_quality)
        #t = Player(4, t_poz, t_price, t_quality)

        #utility = util([x, y], l)
        utility = util([x, y], l)
        print(f"próba: początek - utility x : {x.write()} - utility y : {y.write()}") #- utility z : {z.write()} - utility t : {t.write()}")
        #print(f"próba: początek - utility x : {x.write()} - utility y : {y.write()} ")
        print("----------------------------------------------------------")

        util_list = []
        # list_y = []
        #
        # list_x.append(utility[0])
        # list_y.append(utility[1])

        for k in range(0, 10000000):
            this_util = []
            if k > 4:
                if util_list[k - 1] == util_list[k - 2]:
                    break

            utility = nash([x, y], 0, l)
            x = utility[0]
            y = utility[1]
            # z = utility[2]
            # t = utility[3]

            print(f"próba:{k} - utility x : {x.write()} - utility y : {y.write()}")# - utility z : {z.write()} - utility t : {t.write()}")
            utility = nash([x, y], 1, l)
            x = utility[0]
            y = utility[1]
            # z = utility[2]
            # t = utility[3]

            # print(f"próba:{k} - utility x : {x.write()} - utility y : {y.write()}")# - utility z : {z.write()} - utility t : {t.write()}")
            # utility = nash([x, y, z, t], 2, l)
            # x = utility[0]
            # y = utility[1]
            # # z = utility[2]
            # # t = utility[3]

            # print(
            #     f"próba:{k} - utility x : {x.write()} - utility y : {y.write()}")# - utility z : {z.write()} - utility t : {t.write()}")
            # utility = nash([x, y, z, t], 3, l)
            # x = utility[0]
            # y = utility[1]
            # z = utility[2]
            # t = utility[3]

            this_util.append(utility)
            util_list.append(utility)
            #print(f"próba:{k} - utility x : {x.write()} - utility y : {y.write()} - utility z : {z.write()}")
            print(f"próba:{k} - utility x : {x.write()} - utility y : {y.write()}")# - utility z : {z.write()} - utility t : {t.write()}")
            print("----------------------------------------------------------")

        #outcome.append([])
        #outcome_pos.append([x, y])

    print("----------------------------------------------------------")
    #print(f'utility x : {x.write()} - utility y : {y.write()} - utility z : {z.write()}')
    print(f'utility x : {x.write()} - utility y : {y.write()}')
    print("----------------------------------------------------------")
    #print('outcome_pos')
    #print(outcome_pos)

    # o1 = []
    # o2 = []
    # for t in util_list:
    #     o1.append(t[0][0][0])
    #     o2.append(t[0][0][0])
    #
    # plt.plot(o1, label="line 1", linestyle="-")
    # plt.plot(o2, label="line 2", linestyle="--")
    # plt.show()
if __name__ == "__main__":
    main()

