#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#________ORIGINAL DATA
u1= [0.000654]*7
u2= [0.000669]*7
u3= [0.000689]*7
u4= [0.000703]*7
u5= [0.000779]*7
u6= [0.000691]*7
u7= [0.000748]*7
u8= [0.000765]*7
u9= [0.000831]*7
u10=[0.000801]*7

high= [0.000762]*7
low= [0.000688]*7
medium= [0.000764]*7

#_____OTIMIZADO DATA
uo1= [0.000638]*7
uo2= [0.000653]*7
uo3= [0.000670]*7
uo4= [0.000694]*7
uo5= [0.000704]*7
uo6= [0.000739]*7
uo7= [0.000757]*7
uo8= [0.000775]*7
uo9= [0.000792]*7
uo10=[0.000810]*7

high_o= [0.000747]*7
low_o= [0.000689]*7
medium_o= [0.000745]*7

time_list = [0,10,20,30,40,50,60]

plt.plot(time_list,u1, label='u1',color ='blue')
plt.plot(time_list,u2, label='u2',color ='green')
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

plt.show()
# %%
plt.plot(time_list, high, label='high',color='blue')
plt.plot(time_list, medium, label='medium',color='orange')
plt.plot(time_list, low, label='low',color='red')
plt.plot(time_list, high_o,'--', label='high_o',color='blue')
plt.plot(time_list, medium_o,'--' ,label='medium_o',color='orange')
plt.plot(time_list, low_o,'--', label='low_o',color='red')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2,
             fontsize='medium', title='Users', 
             title_fontsize='large')
plt.title('Delay mean')
plt.xlabel('time(s)')
plt.ylabel('delay (ms)')
plt.show()
# %%
