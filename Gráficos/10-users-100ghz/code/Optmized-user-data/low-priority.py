#%%
import matplotlib.pyplot as plt
# %%
#SINR mean
time_list = [0, 10, 20, 30, 40, 50, 60]
low_original_sinr = [20.998407] * 7
low_optmized_sinr = [32.960925] * 7
plt.plot(time_list, low_original_sinr,label='Original')
plt.plot(time_list, low_optmized_sinr, label='Optmized')
plt.title('Sinr original vs optmized')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), 
           ncol=1, fontsize='medium', title='Low priority', title_fontsize='large')
plt.tight_layout()
plt.show()
#%%
#Delay mean
low_original_delay = [0.000731] * 7
low_optmized_delay = [0.000704] * 7
plt.plot(time_list, low_original_delay,label='original')
plt.plot(time_list, low_optmized_delay, label='Optmized')
plt.title('Delay Original vs Optmized')
plt.xlabel('Tempo(s)')
plt.ylabel('SINR(dB)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), 
           ncol=1, fontsize='medium', title='Low priority', title_fontsize='large')
plt.tight_layout()
plt.show()
# %%
