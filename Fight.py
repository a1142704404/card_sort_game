def fight(lst1,lst2,lst3):
    '''抢地主函数'''
    lst1,lst2,lst3 = lst1,lst2,lst3
    j = 0
    p1,p2,p3 = 0,0,0

    length = len(input('请一号玩家输入"叫地主|不叫":'))
    if length > 2:
        p1 += 1
        j = 1
    if j < 1:
        length = len(input('请二号玩家输入"叫地主|不叫":'))
        if length > 2:
            p2 += 1
            j = 1
    elif j == 1:
        length = len(input('请二号玩家输入"抢地主|不抢":'))
        if length > 2:
            p2 += 1
            j = 1
    if j < 1:
        length = len(input('请三号玩家输入"叫地主|不叫":'))
        if length > 2:
            p3 += 1
            j = 1
    elif j == 1:
        length = len(input('请三号玩家输入"抢地主|不抢":'))
        if length > 2:
            p3 += 1

    if p1 > p2 and p1 > p3:
        print('一号玩家是地主！')
        return lst1
    if p2 > p1 and p2 > p3:
        print('二号玩家是地主！')
        return lst2
    if p3 > p1 and p3 > p2:
        print('三号玩家是地主！')
        return lst3
    if p1 == 1 and p2 == 1 and p3 ==1:
        length = len(input('请一号玩家输入"抢地主|不抢":'))
        if length > 2:
            print('一号玩家是地主！')
            return lst1
        else:
            print('二号玩家是地主！')
            return lst2
    if p1 == p2 == 1 and p3 == 0:
        length = len(input('请一号玩家输入"抢地主|不抢":'))
        if length > 2:
            print('一号玩家是地主！')
            return lst1
        else:
            print('二号玩家是地主！')
            return lst2
    if p2 == p3 == 1 and p1 == 0:
        length = len(input('请二号玩家输入"抢地主|不抢":'))
        if length > 2:
            print('二号玩家是地主！')
            return lst2
        else:
            print('三号玩家是地主！')
            return lst3
    if p1 == p3 == 1  and p2 == 0:
        length = len(input('请一号玩家输入"抢地主|不抢":'))
        if length > 2:
            print('二号玩家是地主！')
            return lst2
        else:
            print('三号玩家是地主！')
            return lst3
    if p1 == 0 and p2 == 0 and p3 == 0:
        print('看来三位玩家对牌都不满意，请重新开始游戏！')
        return None

