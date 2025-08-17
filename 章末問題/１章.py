#問題①
#問1-1.
for i in [1,3,5,7]:
    print(f"{i*i}")

#問1-2.
for i in range(8):
    if i%2==1:
        print(f"{i*i}")


#問題②
#問2-1.
all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    if place in get_place:
        print(place + "のチケットが当選しました！")
    elif place in wait_place:
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")

#問2-2.
all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    if place in get_place:
        print(place + "のチケットが当選しました！")
    elif place in wait_place:
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")

newget_place=get_place+wait_place
msg="{}と{}と{}のチケットが当選しました！".format(*newget_place)
print(msg)









