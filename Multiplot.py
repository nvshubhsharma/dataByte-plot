#!/usr/bin/env python
# coding: utf-8

# 

# In[33]:


import matplotlib.pyplot as plt
import matplotlib.style as stl
month= list(range(1,13))
facecream=[2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
facewash=[1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
toothpaste=[5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400]
batsoap=[9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400]
shamp=[1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800]
moist=[1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
tot_units=[21100,18330,22470,22270,20960,20140,29550,36140,23400,26670,41280,30020]
tot_prof=[211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]
plt.plot(month,facecream,"g",label="facecream")
plt.plot(month,toothpaste,"b",label="Toothpaste")
plt.plot(month,batsoap,"c",label="Bathing Soap")
plt.plot(month,shamp,"k",label="Shampoo")
plt.plot(month,moist,label="Moisturizer")
plt.plot(month,facewash,"r",label="Facewash")
plt.legend()
plt.show()



# In[ ]:





# In[ ]:





# In[ ]:




