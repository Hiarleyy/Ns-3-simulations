#%%
import matplotlib.pyplot as plt
#%%
time_list = [0, 10, 20, 30, 40, 50, 60]
medium_original_sinr = [24.758408] * 7
medium_optmized_sinr = [36.653145] * 7
plt.plot(time_list, medium_original_sinr,label='Original')
plt.plot(time_list, medium_optmized_sinr, label='Optmized')
plt.title('Sinr original vs optmized')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), 
           ncol=1, fontsize='medium', title='medium priority', title_fontsize='large')
plt.tight_layout()
plt.show()
# %%
medium_original_delay = [0.000719] * 7
medium_optmized_delay = [0.000722] * 7
plt.plot(time_list, medium_original_delay,label='Original')
plt.plot(time_list, medium_optmized_delay, label='Optmized')
plt.title('Delay original vs optmized')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), 
           ncol=1, fontsize='medium', title='medium priority', title_fontsize='large')
plt.tight_layout()
plt.show()
# %%
