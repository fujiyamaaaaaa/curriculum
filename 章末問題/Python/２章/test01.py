#test01.py

import random
answer = random.randint(1, 10)

while True:  # 無限ループ
    try:
        number = int(input('10までの数値を入力してください: '))
    except ValueError:
        print("数字以外が入力されました。数字のみを入力してください")
        continue
    if answer < number:
        print('もっと小さな数値です')
    elif answer > number:
        print("もっと大きな数字です")
    else:
        print("素晴らしい！正解です！")
        break