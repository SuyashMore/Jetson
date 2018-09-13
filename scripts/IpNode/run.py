from block_recognition import BlockRecognition
from block_recognition2 import BlockRecognition2

#Z6red I4 O1 J3darkblue S5green L2orange
Lxx1=[3000,3000,3000,3000,3000,2000]
Lxx2=[1500,1900,1000,1300,700,1200]
Lxx3=[400,700,400,600,300,1000]

br1 = BlockRecognition(ID,l1=230, l2=480, l3=200, l4=640, Lxx=Lxx1)
br2 = BlockRecognition(ID,l1=120, l2=230, l3=100, l4=540, Lxx=Lxx2)
br3 = BlockRecognition(ID,l1=0, l2=120, l3=280, l4=450, Lxx=Lxx3)

brr1=br1.run()
brr2=br2.run()
brr3=br3.run()


def give_one_letter(brr1,brr2,brr3):
    max =0
    key =0
    for x, y in brr1.items():
        if y > max:
            key=x
            max=y
    key2 = 0
    max = 0
    for x, y in brr2.items():
        if y > max:
            key2=x
            max=y
    key3=0
    max=0
    for x,y in brr3.items():
        if y > max:
            key3=x
            maxs=y
    return brr1[key],brr2[key2],brr3[key3]


def getVal1():
    x,y,z=give_one_letter(brr1,brr2,brr3)
    return x,y,z

# O1 L2 J3 I4 S5 Z6
# Lxx4=[3000,3000,1000,3000,1300,2000]

# br4 = BlockRecognition2(camera_id=config.CAMERA_ID, optimal_fps=config.FPS,l1=0, l2=480, l3=0, l4=640, Lxx=Lxx4)

# brr4, Str=br4.run()

# n1=calc_digit(give_one_letter(brr1))
# n2=calc_digit(give_one_letter(brr2))
# n3=calc_digit(give_one_letter(brr3))

# n4=calc_digit(Str[0])
# n5=calc_digit(Str[0])
# n6=calc_digit(Str[0])

# N1=n1*100+n2*10+n3
# N2=n4*100+n5*10+n6

# print("1111111111111",N1)
# print("2222222222222",N2)
# #

# Select a point and perform inverse based on arm design