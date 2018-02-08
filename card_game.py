import random
"""该程序是基于“插入排序法”扩展的斗地主游戏小程序,其核心是实现市面上斗地主游戏发牌自动排序的功能"""
def shuffle():
    """
    此函数用于洗牌，牌库为列表Deck，其中3-10分别代表3-10四花色的牌
    11代表‘J’牌，12代表‘Q’牌，13代表‘K’牌，99代表‘A’牌，100代表‘2’牌
    233代表‘小王’牌，666代表‘大王牌’
    在之后的程序中，我将用代码实现现实中的牌面，输出正确的牌
    """
    Deck =[3,3,3,3,            #3
           4,4,4,4,            #4
           5,5,5,5,            #5
           6,6,6,6,            #6
           7,7,7,7,            #7
           8,8,8,8,            #8
           9,9,9,9,            #9
           10,10,10,10,        #10
           11,11,11,11,        #J
           12,12,12,12,        #Q
           13,13,13,13,        #K
           99,99,99,99,        #A
           100,100,100,100,    #2
           233,                #小王
           666]                #大王
    random.shuffle(Deck)       #洗牌
    return Deck

def sort(lst):
    '''此函数是本程序的核心，插入排序法的python版本'''
    for i in range(1,len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] < key:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = key
    return lst

def replace(lst):
    '''此函数是将数字替换成现实中的牌面'''
    while 11 in lst:
        lst[lst.index(11)] = 'J'
    while 12 in lst:
        lst[lst.index(12)] = 'Q'
    while 13 in lst:
        lst[lst.index(13)] = 'K'
    while 99 in lst:
        lst[lst.index(99)] = 'A'
    while 100 in lst:
        lst[lst.index(100)] = 2
    while 233 in lst:
        lst[lst.index(233)] = '小王'
    while 666 in lst:
        lst[lst.index(666)] = '大王'
    return lst

def HoleCards(lst):    #盖牌
    hole_cards = replace(sort(lst))
    print(hole_cards)

def FirstCards(lst):   #第一个玩家的17张牌
    first_cards = replace(sort(lst))
    print(first_cards)

def SecondCards(lst):  #第二个玩家的17张牌
    second_cards = replace(sort(lst))
    print(second_cards)

def ThirdCards(lst):  #第三个玩家的17张牌
    third_cards = replace(sort(lst))
    print(third_cards)

if __name__ == '__main__':
    print('-----斗地主-----')
    Deck = shuffle()       #洗牌
    hole_cards = Deck[:3]  # 斗地主起始的三张盖牌
    HoleCards(hole_cards)
    first_cards = Deck[3:20]  # 第一个玩家拿的17张牌
    FirstCards(first_cards)
    second_cards = Deck[20:37]  # 第二个玩家拿的17张牌
    SecondCards(second_cards)
    third_cards = Deck[37:54]  # 第三个玩家拿的17张牌
    ThirdCards(third_cards)