#test02.py

while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        number = int(input('選択してください。: '))

        # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。

        if number==1:
            print("↓\n","ValueError")
            try:
                a=int("Value")
            except ValueError as hoge:
                print(hoge.args,"\n↓","\nもう一度選択しましょう")
            continue
        elif number==2:
            print("↓\n","IndexError")
            try:
                lst=[1,2,3]
                print(lst[3])
            except IndexError as index:
                print(index.args,"\n↓\nもう一度選択しましょう")
            continue
        elif number==3:
            print("↓\n例外を発生させませんでした\n↓\nもう一度選択しましょう")
            continue

    # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。

        else:
            print("↓\n終了します")
            break
    except ValueError:
        print("数字以外が入力されました。数字のみを入力してください")
        continue
print('↓')
print('無限ループを終了します')