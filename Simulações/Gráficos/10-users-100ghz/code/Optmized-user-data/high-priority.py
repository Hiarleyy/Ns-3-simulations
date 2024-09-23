#%%
import matplotlib.pyplot as plt
#%%
#SINR
time_list = [0, 10, 20, 30, 40, 50, 60]
high_original_sinr = [23.428736] * 7
high_optmized_sinr = [26.433733] * 7
plt.plot(time_list, high_original_sinr, label='Original')
plt.plot(time_list, high_optmized_sinr, label='Optmized')
plt.title('SINR original vs optmized')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), 
           ncol=1, fontsize='medium', title='high priority', title_fontsize='large')
plt.tight_layout()
plt.show()
# %%
#DELAY
high_original_delay = [0.000715] * 7
high_optmized_delay = [0.000722] * 7
plt.plot(time_list, high_original_delay,label='Original')
plt.plot(time_list, high_optmized_delay, label='Optmized')
plt.title('Delay original vs optmized')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), 
           ncol=1, fontsize='medium', title='high priority', title_fontsize='large')
plt.tight_layout()
plt.show()
# %%
