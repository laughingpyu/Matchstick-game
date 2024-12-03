import random

def optimal_take_away(stick_num):
    if stick_num == 1:
        return 1
    elif (stick_num - 1) % 6 == 0:
        return 6
    else:
        if stick_num>6:
            return (stick_num-1)%6
        else:
            return stick_num


stick_num=random.randint(60,100)
print('现有{}根火柴'.format(stick_num))
for i in range(stick_num):
    if stick_num != 0:
        userpick=int(input('用户选取数量：'))            #判断输入是否合法
        if userpick in [1, 2, 3, 4, 5, 6]:
            stick_num=stick_num-userpick
            print('用户取后有{}根火柴'.format(stick_num))
            if stick_num == 0:
                print('用户胜利')
                break
        else:
            print('用户输入有误，取的火柴棍数目必须是1到6之间的整数，请重新输入')
            continue
        computerpick=optimal_take_away(stick_num)
        print('电脑取了{}根.'.format(computerpick))
        stick_num = stick_num - computerpick
        print('电脑取后有{}根火柴'.format(stick_num))
        if stick_num == 0:
            print('电脑胜利')
            break
    else:
        break
print('您输入错误的次数太多了，请重新运行该程序')

