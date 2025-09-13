#test01.py

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-darkgrid')
fig,ax=plt.subplots(1,2)

date=["09-10","09-11","09-12"]
work=[10,0,10]
study=[4,6,3]

ax[0].plot(date,work,color="blue",label="time(h)")
ax[0].set_title("藤山の直近3日間の勤務時間",fontname="MS Gothic")
ax[0].legend()

ax[1].plot(date,study,color="blue",label="time(h)")
ax[1].set_title("藤山の直近3日間の勉強時間",fontname="MS Gothic")
ax[1].legend()

plt.tight_layout()

plt.show()