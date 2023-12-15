import pyshtools as pysh
import matplotlib.pyplot as plt
import cmcrameri as cm

f,((ax1,ax2,ax3),(ax4,ax5,ax6))=plt.subplots(2,3)
pysh.SHGrid.from_file('IBC_Thickness_drho200_v1.txt').plot(ax=ax1)
pysh.SHGrid.from_file('IBC_Thickness_drho200_v2.txt').plot(ax=ax2)
pysh.SHGrid.from_file('IBC_Thickness_drho200_v3.txt').plot(ax=ax3)
pysh.SHGrid.from_file('IBC_Thickness_drho300_v2.txt').plot(ax=ax4)
pysh.SHGrid.from_file('IBC_Thickness_drho400_v2.txt').plot(ax=ax5)
ax6.set_visible(False)

f,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)
pysh.SHGrid.from_file('Mare_interp.txt').plot(ax=ax1)
pysh.SHGrid.from_file('Mare_init.txt').plot(ax=ax2)
pysh.SHGrid.from_file('Crust_interp.txt').plot(ax=ax3)
pysh.SHGrid.from_file('Crust_init.txt').plot(ax=ax4)

f,ax1=plt.subplots(1,1)
pysh.SHGrid.from_file('IBC_Thickness_gravity.txt').plot(ax=ax1)
plt.show()