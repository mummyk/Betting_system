class UzoBetting:
    'An UzoBetting class'
    play_default:bool = False
    staking:float = 1000.00
  
    # initialization or constructor method of
    def __init__(self, play,stake):  
          
        # class of UzoBetting
        if play is False:
            play = UzoBetting.play_default
        if stake==0:
            stake=UzoBetting.staking
        self.playing = play
        self.stakes = stake
        
    
    # two ways calculation function
    def two_ways(stakes, odds=[]):
        ways = 0
        percentage = 0
        o1, o2 = odds
        arb_ords = ((1/o1)+(1/o2))*100
        if arb_ords < 100:
            round(arb_ords, 2)
            percentage = round((100 - arb_ords), 2)
            w1 = stakes/(1 + (o1/o2))
            w2 = stakes/(1 + (o2/o1))
            ways = [round(w1), round(w2)]
        else:
            arb_ords = 0
        print(arb_ords,percentage,ways,odds)
        return arb_ords
        
    # Three ways calculation function
    def three_ways(stakes, odds=[]):
        way = 0
        percentage = 0
        o1, o2, o3 = odds
        arb_ords = ((1/o1)+(1/o2)+(1/o3))*100
        if arb_ords < 100:
            arb_ords
            percentage = round((100 - arb_ords))
            w1 = round(stakes/(1+(o1/o2)+(o1/o3)))
            w2 = round(stakes/(1+(o2/o1)+(o2/o3)))
            w3 = round(stakes/(1+(o3/o1)+(o3/o2)))
            ways = [w1,w2,w3]
            
        else:
            arb_ords = 0
        print(arb_ords,percentage,ways,odds)
        return arb_ords
        

    # arbitrage_calculator method of class UzoBetting
    def arbitrage_calculator(self, odds=[]):
        if len(odds) == 2:
            UzoBetting.two_ways(self.stakes,odds)
        elif len(odds) == 3:
            UzoBetting.three_ways(self.stakes, odds)
            
        

three_ways = [2.30,3.35,4.40]
two_ways = [1.80,2.50]
uzo = UzoBetting(True,10000)
uzo.arbitrage_calculator(three_ways)
