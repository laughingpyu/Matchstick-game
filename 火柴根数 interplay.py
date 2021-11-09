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
        userpick=int(input('用户选取数量：'))
        stick_num=stick_num-userpick
        print('用户取后有{}根火柴'.format(stick_num))
        if stick_num ==0:
            print('用户胜利')
            break
        computerpick=optimal_take_away(stick_num)
        print('电脑取了{}根.'.format(computerpick))
        stick_num = stick_num - computerpick
        print('电脑取后有{}根火柴'.format(stick_num))
        if stick_num ==0:
            print('电脑胜利')
            break
    else:
        break

