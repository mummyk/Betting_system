class UzoBetting:
    '''An UzoBetting class'''
    play_default: bool = False
    staking: float = 1000.00

    # initialization or constructor method of
    def __init__(self, play: bool, stake: float, odds: list):

        # instance variables
        if play is False:
            play = self.play_default
        if stake == 0:
            stake = self.staking
        self.play = play
        self.stake = stake
        self.odd = odds
        self.arbitrage_calculator()

    # Process the scraped data and get the largest odds
    def get_largest_odd(self):
        """
        Where o1 is Home
              o2 is Away
              o3 is draw
        """
        value = []
        if len(self.odd) == 2:
            o1, o2 = self.odd
            # get the max for o1,o2
            o1_max, o2_max = max(o1), max(o2)
            value = [o1_max, o2_max]
        elif len(self.odd) == 3:
            o1, o2, o3 = self.odd
            # get the max for o1,o2,o3
            o1_max, o2_max, o3_max = max(o1), max(o2), max(o3)
            value = [o1_max, o2_max, o3_max]

        return value

    def arbitrage_calculator(self):
        ''' Number of ways calculation function'''
        ways = 0
        percentage = 0
        arb_ords = 0
        odds = self.get_largest_odd()
        # two ways calculation function
        if len(self.odd) == 2:
            o1, o2 = odds
            arb_ords = ((1/o1)+(1/o2))*100
            if arb_ords < 100:
                round(arb_ords, 2)
                percentage = round((100 - arb_ords), 2)
                w1 = self.stake/(1 + (o1/o2))
                w2 = self.stake/(1 + (o2/o1))
                ways = [round(w1), round(w2)]

        # for thre way
        elif len(self.odd) == 3:
            o1, o2, o3 = odds
            arb_ords = ((1/o1)+(1/o2)+(1/o3))*100
            if arb_ords < 100:
                percentage = round((100 - arb_ords))
                w1 = round(self.stake/(1+(o1/o2)+(o1/o3)))
                w2 = round(self.stake/(1+(o2/o1)+(o2/o3)))
                w3 = round(self.stake/(1+(o3/o1)+(o3/o2)))

                ways = [w1, w2, w3]

        game = dict(Arbitrage=arb_ords, Roi=percentage, Ways=ways, Odds=odds)

        return game


odds_list_two = [[1.80, 1.20, 1.12, 1.50], [2.20, 2.00, 1.95, 2.50]]
odds_list_three = [[2.30, 2.00, 1.12, 1.50], [
    2.20, 2.00, 1.95, 3.35], [3.50, 2.40, 3.67, 4.40]]
three_ways = [2.30, 3.35, 4.40]
two_ways = [1.80, 2.50]

uzo = UzoBetting(True, 20000, odds_list_three)
# uzo.arbitrage_calculator(two_ways)
