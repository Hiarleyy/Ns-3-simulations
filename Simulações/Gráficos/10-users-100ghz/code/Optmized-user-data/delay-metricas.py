#%%
import matplotlib.pyplot as plt
time_list = [0, 10, 20, 30, 40, 50, 60]
mean_geral_original =  [0.000724] * 7
mean_geral_optmized =  [0.000713] * 7
plt.plot(time_list, mean_geral_original, label='original')
plt.plot(time_list, mean_geral_optmized, label='optmized')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1,
             fontsize='medium', title='Users_mean', 
             title_fontsize='large')

plt.title('Mean Delay rate (Original vs Optmized)')
plt.xlabel('time(s)')
plt.ylabel('delay (ms)')
plt.show()
#%%
#mean original users
u1 =  [0.000725] * 7
u2 =  [0.000744] * 7
u3 =  [0.000759] * 7
u4 =  [0.000777] * 7
u5 =  [0.000644] * 7
u6 =  [0.000669] * 7
u7 =  [0.000679] * 7
u8 =  [0.000697] * 7
u9 =  [0.000805] * 7
u10 = [0.000741] * 7
# mean optmized users
uo1 =  [0.000739] * 7
uo2 =  [0.000757] * 7
uo3 =  [0.000775] * 7
uo4 =  [0.000793] * 7
uo5 =  [0.000633] * 7
uo6 =  [0.000651] * 7
uo7 =  [0.000669] * 7
uo8 =  [0.000687] * 7
uo9 =  [0.000705] * 7
uo10 = [0.000722] * 7

# %%
plt.plot(time_list,u1, label='u1',color ='blue')
plt.plot(time_list,u2, label='uo2',color ='green')
plt.plot(time_list,u3, label='u3',color ='orange')
plt.plot(time_list,u4, label='u4',color ='gray')
plt.plot(time_list,u5, label='u5',color ='violet')
plt.plot(time_list,u6, label='u6',color ='yellow')
plt.plot(time_list,u7, label='u7',color ='brown')
plt.plot(time_list,u8, label='u8',color ='pink')
plt.plot(time_list,u9, label='u9',color ='red')
plt.plot(time_list,u10, label='u10',color ='black')
plt.plot(time_list,uo1,'--',label='uo1',color='blue')
plt.plot(time_list,uo2,'--' ,label='uo2',color ='green')
plt.plot(time_list,uo3,'--' ,label='uo3',color ='orange')
plt.plot(time_list,uo4,'--' ,label='uo4',color ='gray')
plt.plot(time_list,uo5,'--' ,label='uo5',color ='violet')
plt.plot(time_list,uo6,'--' ,label='uo6',color ='yellow')
plt.plot(time_list,uo7, '--',label='uo7',color ='brown')
plt.plot(time_list,uo8,'--' ,label='uo8',color ='pink')
plt.plot(time_list,uo9,'--' ,label='uo9',color ='red')
plt.plot(time_list,uo10,'--' ,label='uo10',color ='black')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2,
             fontsize='medium', title='Users', 
             title_fontsize='large')

plt.title('Mean Delay rate (Original vs Optmized)')
plt.xlabel('time(s)')
plt.ylabel('delay (ms)')
plt.show()
# %%
