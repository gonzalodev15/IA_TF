import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


x_ram = np.arange(2, 16, 1) 
x_vid = np.arange(768, 3580, 1)
x_proc = np.arange(2.1, 4.3, 1)  

ram_lo = fuzz.trimf(x_ram, [2, 3, 4])
ram_md = fuzz.trimf(x_ram, [4, 6, 8])
ram_hi = fuzz.trimf(x_ram, [8, 12, 16])

vid_lo = fuzz.trimf(x_vid, [768, 980, 1200]) 
vid_md = fuzz.trimf(x_vid, [1200, 1550, 1920])
vid_hi = fuzz.trimf(x_vid, [1920, 2590, 3580]) 

proc_lo = fuzz.trimf(x_proc, [2.1, 2.3, 2.4]) 
proc_md = fuzz.trimf(x_proc, [2.4, 2.8, 3.1]) 
proc_hi = fuzz.trimf(x_proc, [3.1, 3.7, 4.3]) 


fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))
ax0.plot(x_proc, proc_lo, 'b', linewidth=1.5, label='Poco')
ax0.plot(x_proc, proc_md, 'g', linewidth=1.5, label='Normal')
ax0.plot(x_proc, proc_hi, 'r', linewidth=1.5, label='Mucho')
ax0.set_title('Potencia del procesador')
ax0.legend()
ax1.plot(x_vid, vid_lo, 'b', linewidth=1.5, label='Poco')
ax1.plot(x_vid, vid_md, 'g', linewidth=1.5, label='Normal')
ax1.plot(x_vid, vid_hi, 'r', linewidth=1.5, label='Mucho')
ax1.set_title('Potencia de la tarjeta de video')
ax1.legend()
ax2.plot(x_ram, ram_lo, 'b', linewidth=1.5, label='Poco')
ax2.plot(x_ram, ram_md, 'g', linewidth=1.5, label='Normal')
ax2.plot(x_ram, ram_hi, 'r', linewidth=1.5, label='Mucho')
ax2.set_title('Capacidad de memoria RAM')
ax2.legend()

for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
plt.tight_layout()
plt.show()


ram_level_lo = fuzz.interp_membership(x_ram, ram_lo, 4)
ram_level_md = fuzz.interp_membership(x_ram, ram_md, 4)
ram_level_hi = fuzz.interp_membership(x_ram, ram_hi, 4)
vid_level_lo = fuzz.interp_membership(x_vid, vid_lo, 1550)
vid_level_md = fuzz.interp_membership(x_vid, vid_md, 1550)
vid_level_hi = fuzz.interp_membership(x_vid, vid_hi, 1550)
proc_level_lo = fuzz.interp_membership(x_proc, proc_lo, 3.1)
proc_level_md = fuzz.interp_membership(x_proc, proc_md, 3.1)
proc_level_hi = fuzz.interp_membership(x_proc, proc_hi, 3.1)



active_rule1 = np.fmax(ram_level_lo, vid_level_lo)

proc_activation_lo = np.fmin(active_rule1, proc_level_lo) 

active_rule2 = np.fmax(ram_level_md, vid_level_md)

proc_activation_md = np.fmin(active_rule2, proc_level_md)


active_rule3 = np.fmax(ram_level_hi, vid_level_hi)
proc_activation_hi = np.fmin(active_rule3, proc_level_lo_hi)

aggregated = np.fmax(proc_activation_lo, np.fmax(proc_activation_md, proc_activation_hi))

ram = fuzz.defuzz(x_ram, aggregated, 'centroid')
proc = fuzz.defuzz(x_proc, aggregated, 'centroid')
vid = fuzz.defuzz(x_vid, aggregated, 'centroid')

ram_activation = fuzz.interp_membership(x_ram, aggregated, ram)
proc_activation = fuzz.interp_membership(x_proc, aggregated, proc)
vid_activation = fuzz.interp_membership(x_vid, aggregated, vid)

plt.show()










