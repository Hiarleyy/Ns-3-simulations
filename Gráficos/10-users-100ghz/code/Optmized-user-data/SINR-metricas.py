#%%
import matplotlib.pyplot as plt
#sinais originais SINR
high = [23.428736] * 7
low = [20.998407] * 7
medium= [24.758408] * 7
#Sinais otimizados SINR
o_high = [26.433733] * 7
o_low = [32.960925] * 7
o_medium= [36.653145] * 7
time_list = [0, 10, 20 , 30 , 40 , 50, 60]
# %%
plt.plot(time_list, high, label='high', color='blue')
plt.plot(time_list, medium, label='medium', color='orange')
plt.plot(time_list, low, label='low', color='red')
plt.plot(time_list, o_high,'--', label='o_high', color='blue')
plt.plot(time_list, o_medium,'--' ,label='o_medium', color='orange')
plt.plot(time_list, o_low, '--',label='o_low', color='red')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2,
             fontsize='medium', title='Priority', 
             title_fontsize='large')

plt.title('Mean SINR rate (Original vs Optmized)')
plt.xlabel('time(s)')
plt.ylabel('SINR(dB)')


plt.show()

# %%
#media geral
original_data_mean_sinr = 22.718661
optmized_data_mean_sinr = 31.088927

u1 =  [27.9415] * 7
u2 =  [26.0163] * 7
u3 =  [26.7339] * 7
u4 =  [23.9315] * 7
u5 =  [19.1594] * 7
u6 =  [20.3801] * 7
u7 =  [20.8094] * 7
u8 =  [15.7612] * 7
u9 =  [14.4300] * 7
u10 = [24.2904] * 7
# mean optmized users
uo1 =  [28.9383] * 7
uo2 =  [36.3131] * 7
uo3 =  [36.7191] * 7
uo4 =  [23.3089] * 7
uo5 =  [27.0540] * 7
uo6 =  [24.6518] * 7
uo7 =  [36.5213] * 7
uo8 =  [32.5131] * 7
uo9 =  [30.0734] * 7
uo10 = [37.9044] * 7
time_list = [0, 10, 20, 30, 40, 50, 60]

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

plt.title('Mean SINR rate (Original vs Optmized)')
plt.xlabel('time(s)')
plt.ylabel('SINR(dB)')
plt.show()
# %%
