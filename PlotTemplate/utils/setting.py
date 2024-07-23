import numpy as n
np = n



## different setting with different function
## create setting dictionary auto
## set the lim or range to each parameter 
##
##
## clasfy_setting = {
##			 		A : dict( nam = spr, title = 2022 Spring)
## 					B : dict( nam = NE,  title = North East )
##					}
##
## basic_setting  = {
##			 		A : dict( xlim = (1,2), xticks= ...... )
## 					B : dict( xlim = (1,2), xticks= ...... )
##					}
##
## sca_setting(A_B_C,clasfy_set=None)
## 
## 		decode A, B, C
##		add clasfy_set
##
## return setting



basic_setting = {

				'time' : dict(),

				'temp' : dict(lim=(12,36),label=r'Temperature ($\rm \degree$C)',ticks=[12,20,28,36],nam='temp',
							  plot_set=dict(label='Temp.',color='#fd3535')),

				'ws'   : dict(lim=(0,6),label=r'Wind Speed (m/s)',ticks=None,nam='ws',
							  plot_set=dict(label='WS',color='#52b788',lw=1.5),
							  sca_set=dict(cmap='jet',vmin=1,vmax=3),
							  bar_title='WS (m/s)'),

				'wd'   : dict(lim=(0,360),label=r'Wind Speed ($\bf \degree$)',ticks=[0,180,360],nam='wd',
							  plot_set=dict(color='#555555',label='WD',ls='none',marker='o',ms=2)),

				'ext'  : dict(lim=(0,450),label=r'Extinction (1/Mm)',title='Extinction',
							  plot_set=dict(label='Ext.',color='#4c79ff'),
							  sca_set=dict(cmap='jet',vmin=0,vmax=200),
							  box_set=dict(color_list=['#6facd8',],leg_nam=['Extinction']),
							  bar_title='Ext. (1/Mm)'),

				'aod'  : dict(lim=(0,2), label=r'AOD', title='AOD',
							  plot_set=dict(label='AOD', color='#ff7373'),
							  sca_set=dict(cmap='jet', vmin=0, vmax=200),
							  box_set=dict(color_list=['#6facd8',], leg_nam=['AOD']),
							  bar_title='AOD'),

				'RH'  : dict(lim=(20,100),label=r'RH (%)',ticks=[20,40,60,80,100],title='RH',
							  plot_set=dict(label='RH',color='#42b1ff'),
							  sca_set=dict(cmap='jet',vmin=60,vmax=90),
							  bar_title='RH'),

				'ext_day'  : dict(lim=(0,450),label=None,ticks=[0,150,300,450],title='Extinction',
							  plot_set=dict(label='Ext.',color='#555555',marker='D',mfc='#ffffff'),
							  sca_set=dict(cmap='jet',vmin=50,vmax=250),
							  bar_title='Ext.'),

				'dext'  : dict(lim=(-30,30),label=r'dExt.',ticks=None,nam='dext',
							  plot_set=dict(label='dExt.',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=-20,vmax=20),
							  bar_title='dExt.'),

				'd2ext'  : dict(lim=(None,None),label=r'd$\bf ^2$Ext.',ticks=[0,100,200,300],nam='d2ext',
							  plot_set=dict(label='dExt.',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=None,vmax=None),
							  bar_title=r'd$\rm ^2$Ext.'),

				'rec_ext'  : dict(lim=(0,450),label=r'Reconstructed Ext. (1/Mm)', nam='rec-ext',
							  plot_set=dict(label='Rec-Ext.',color='#353526'),label_twin=None,
							  sca_set=dict(cmap='jet',vmin=30,vmax=150),
							  bar_title='Rec-Ext. (1/Mm)'),

				'rec_wet_ext'  : dict(lim=(0,500),label=r'Wet Reconstructed Ext. (1/Mm)',ticks=[0,250,500],nam='rec-ext',
							  # plot_set=dict(label='Ext.',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=30,vmax=150),
							  bar_title='Wet Rec-Ext. (1/Mm)'),

				'mie_ext'  : dict(lim=(0,450),label=r'Mie Ext. (1/Mm)',nam='mie-ext',
							  plot_set=dict(label='Mie Ext.',color='#353526'),label_twin=None,
							  sca_set=dict(cmap='jet',vmin=30,vmax=150),
							  bar_title='Mie Ext. (1/Mm)'),

				'pbl'  : dict(lim=(200,1200),label=r'PBL (m)',ticks=None,nam='pbl',
							  sca_set=dict(cmap='jet',vmin=200,vmax=800),
							  plot_set=dict(label='PBL',color='#6f6f6f',lw=1.5),
							  bar_title='PBL (m)'),

				'vc'  : dict(lim=(0,4000),label=r'VC ($\bf m^2$/s)',ticks=[0,2000,4000],nam='pbl',
							  sca_set=dict(cmap='jet',vmin=200,vmax=800),
							  plot_set=dict(label='VC',color='#ff5a5a',lw=0,marker='o',ms=2),
							  bar_title='VC'),

				'SSA'  : dict(lim=(.2,1),label=r'SSA',ticks=[.2,.4,.6,.8,1.],title='SSA',
							  plot_set=dict(label='SSA',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=.6,vmax=1),
							  bar_title='SSA'),

				'sca'  : dict(lim=(0,300),label=r'Scatter Coe. (1/Mm)',ticks=[0,100,200,300],title='Scatter',
							  plot_set=dict(label='sca.',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=30,vmax=160),
							  bar_title='Sca. (1/Mm)'),

				'mie_sca'  : dict(lim=(0,300),label=r'Mie Scatter Coe. (1/Mm)',ticks=[0,100,200,300],nam='mie-sca',
							  plot_set=dict(label='sca.',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=30,vmax=160),
							  bar_title='Mie Sca. (1/Mm)'),

				'abs'  : dict(lim=(0,60),label=r'Absorption Coe. (1/Mm)',ticks=[0,20,40,60],title='Absorption',
							  plot_set=dict(label='abs.',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=20,vmax=40),
							  bar_title='Abs. (1/Mm)'),

				'mie_abs'  : dict(lim=(0,60),label=r'Mie Absorption Coe. (1/Mm)',ticks=[0,20,40,60],nam='mie-sca',
							  plot_set=dict(label='abs.',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=20,vmax=40),
							  bar_title='Mie Abs. (1/Mm)'),

				'MSE'  : dict(lim=(0,12),label=r'MSE (m$\bf ^2$/g)',ticks=[0,4,8,12],title='MSE',
							  plot_set=dict(label='MSE',color='#fd3535'),label_pad=-5,
							  sca_set=dict(cmap='jet',vmin=2,vmax=8),
							  bar_title=r'MSE (m$\rm ^2$/g)'),

				'dMSE'  : dict(lim=(None,None),label=r'dMSE',ticks=[0,2,4,6,8],nam='dmse',
							  plot_set=dict(label='dMSE',color='#fd3535'),label_pad=-5,
							  sca_set=dict(cmap='jet',vmin=-1,vmax=1),
							  bar_title=r'dMSE'),

				'd2MSE'  : dict(lim=(None,None),label=r'dMSE',ticks=[0,2,4,6,8],nam='d2mse',
							  plot_set=dict(label='dMSE',color='#fd3535'),label_pad=-5,
							  sca_set=dict(cmap='jet',vmin=None,vmax=None),
							  bar_title=r'd$\rm ^2$MSE'),

				'MAE'  : dict(lim=(0,4),label=r'MAE (m$\bf ^2$/g)',ticks=[0,2,4],title='MAE',
							  plot_set=dict(label='MAE',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=.5,vmax=2.5),
							  bar_title=r'MAE (m$\rm ^2$/g)'),

				'MEE'  : dict(lim=(0,12),label=r'MEE (m$\bf ^2$/g)',ticks=[0,4,8,12],title='MEE',
							  plot_set=dict(label='MEE',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=2,vmax=10),
							  bar_title=r'MEE (m$\rm ^2$/g)'),

				'GMD'  : dict(lim=(10,70),label=r'GMD (nm)',ticks=[10,30,50,70],title='GMD',
							  plot_set=dict(label='GMD',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=20,vmax=50),
							  bar_set=dict(color_list=['#7396ff',],leg_nam=[r'GMD (nm)',]),
							  bar_title=r'GMD (nm)',leg_title=r'GMD'),

				'GMD_surf'  : dict(lim=(0,400),label=r'GMD$\bf _{surface}$ (nm)',title=r'GMD$\bf _{surface}$',
							  plot_set=dict(label=r'GMD$\rm _{surface}$ (nm)',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=100,vmax=300),
							  bar_set=dict(color_list=['#7396ff',],leg_nam=[r'GMD$\rm _{surf}$ (nm)',]),
							  bar_title=r'GMD$\rm _{surf}$ (nm)',leg_title=r'GMD$\rm _{surface}$'),

				'GMD_vol'  : dict(lim=(0,1e3),label=r'GMD$\bf _{volume}$ (nm)',title=r'GMD$\bf _{volume}$',
							  plot_set=dict(label=r'GMD$\rm _{volume}$ (nm)',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=200,vmax=800),
							  bar_title=r'GMD$\rm _{vol}$ (nm)',leg_title=r'GMD$\rm _{volume}$'),
							  
				'GSD'  : dict(lim=(1,3),label=r'GSD',ticks=None,
							  sca_set=dict(cmap='jet',vmin=1.6,vmax=2.6),
							  bar_title=r'GSD'),
							  
				'GSD_surf'  : dict(lim=(1,3),label=r'GSD $\bf _{surface}$',ticks=None,
							  sca_set=dict(cmap='jet',vmin=2,vmax=4),title=r'GSD $\bf _{surface}$',
							  bar_title=r'GSD$\rm _{surf}$'),
						  
				'GSD_vol'  : dict(lim=(1,3),label=r'GSD $\bf _{volume}$',ticks=None,
							  sca_set=dict(cmap='jet',vmin=2,vmax=3.5),
							  bar_title=r'GSD$\rm _{vol}$'),

				'apsGSD'  : dict(lim=(1,3),label=r'GSD',ticks=None,
							  sca_set=dict(cmap='jet',vmin=1.2,vmax=1.6),
							  bar_title=r'apsGSD'),
								  
				'TNC'  : dict(lim=(0,1e5),label=r'TNC (#/$\bf cm^{3}$)',ticks=None,title='TNC',
							  plot_set=dict(label='TNC',color='#fd3535'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=1e4,vmax=4e4),
							  bar_title=r'TNC (#/$\rm cm^{3}$)'),

				'dTNC'  : dict(lim=(-6e4,6e4),label=r'dTNC',ticks=None,nam='dtnc',
							  sca_set=dict(cmap='jet',vmin=-1e4,vmax=1e4),bar_title=r'dTNC',
							  plot_set=dict(label='dTNC',color='#fd3535'),label_pad=0,),
								
				'd2TNC'  : dict(lim=(None,None),label=r'd$\bf ^2$TNC',ticks=None,nam='d2tnc',
							  sca_set=dict(cmap='jet',vmin=-1e4,vmax=1e4),
							  plot_set=dict(label='dTNC',color='#fd3535'),label_pad=0,bar_title=r'd$\bf ^2$TNC'),
																	  
				'smpsTNC'  : dict(lim=(0,None),label=r'smps-TNC (#/$\bf cm^{3}$)',ticks=None,nam='smpstnc',
							  plot_set=dict(label='TNC',color='#fd3535'),label_pad=0,
							  # sca_set=dict(cmap='jet',vmin=30,vmax=150),
							  bar_title=r'TNC (#/$\rm cm^{3}$)'),	
					  
				'apsTNC'  : dict(lim=(0,80),label=r'aps-TNC (#/$\bf cm^{3}$)',ticks=[0,20,40,60,80],nam='apstnc',
							  plot_set=dict(label='TNC',color='#fd3535'),label_pad=0,
							  # sca_set=dict(cmap='jet',vmin=30,vmax=150),
							  bar_title=r'TNC (#/$\rm cm^{3}$)'),

				'TSC'  : dict(lim=(0,1.2e9),label=r'TSC ($\bf nm^2 / cm^3$)',ticks=[0,.4e9,.8e9,1.2e9],title='TSC',
							  plot_set=dict(label='TSC',color='#fd3535'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=1e8,vmax=4e8),
							  bar_title=r'TSC'),

				'dTSC'  : dict(lim=(None,None),label=r'dTSC',ticks=None,nam='dtsc',
							  sca_set=dict(cmap='jet',vmin=-1e8,vmax=1e8),bar_title=r'dTSC',
							  plot_set=dict(label='dTSC',color='#fd3535'),label_pad=0,),
								
				'd2TSC'  : dict(lim=(None,None),label=r'dTSC',ticks=None,nam='d2tsc',
							  sca_set=dict(cmap='jet',vmin=-1e8,vmax=1e8),
							  plot_set=dict(label='d$\bf ^2$TSC',color='#fd3535'),label_pad=0,bar_title=r'd$\bf ^2$TSC'),

				'TSC_um2'  : dict(lim=(0,1.2e3),label=r'TSC ($\bf \mu m^2 / cm^3$)',nam='tsc-um2',
							  plot_set=dict(label='TSC',color='#fd3535'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=100,vmax=600),
							  bar_title=r'TSC ($\rm \mu m^2 / cm^3$)'),

				'smpsTSC'  : dict(lim=(0,1.2e9),label=r'smps-TSC ($\bf nm^2 / cm^3$)',ticks=[0,.4e9,.8e9,1.2e9],nam='smpstsc',
							  plot_set=dict(label='TSC',color='#fd3535'),label_pad=0,
							  # sca_set=dict(cmap='jet',vmin=30,vmax=150),
							  bar_title=r'TSC ($\rm nm^2 / cm^3$)'),

				'smpsTSC_um2'  : dict(lim=(0,1.2e3),label=r'smps-TSC ($\bf \mu m^2 / cm^3$)',ticks=[0,.4e3,.8e3,1.2e3],nam='smpstsc-um2',
							  plot_set=dict(label='TSC',color='#fd3535'),label_pad=0,
							  # sca_set=dict(cmap='jet',vmin=30,vmax=150),
							  bar_title=r'TSC ($\rm \mu m^2 / cm^3$)'),

				'apsTSC'  : dict(lim=(0,None),label=r'aps-TSC ($\bf \mu m^2 / cm^3$)',ticks=None,nam='apstsc',
							  plot_set=dict(label='TSC',color='#fd3535'),label_pad=0,
							  # sca_set=dict(cmap='jet',vmin=30,vmax=150),
							  bar_title=r'TSC ($\rm \mu m^2 / cm^3$)'),

				'TVC'  : dict(lim=(0,6e10),label=r'TVC ($\bf nm^3 / cm^3$)',ticks=None,title='TVC',
							  plot_set=dict(label='TVC',color='#fd3535'),label_pad=-5,
							  sca_set=dict(cmap='jet',vmin=1e10,vmax=3e10),
							  bar_title=r'TVC'),

				'TVC_um3' : dict(lim=(0,60),label=r'TVC ($\bf \mu m^3 / cm^3$)',nam='tvc-um3',
							  plot_set=dict(label='TVC',color='#333333'),label_pad_twin=30,label_pad=0,
							  sca_set=dict(cmap='jet',vmin=5,vmax=40),
							  bar_title=r'TVC'),

				'dTVC'  : dict(lim=(None,None),label=r'dTVC',ticks=None,nam='dtvc',
							  sca_set=dict(cmap='jet',vmin=None,vmax=None),
							  plot_set=dict(label='dTVC',color='#fd3535'),label_pad=0,),
								
				'PM10'  : dict(lim=(0,60),label=r'PM$\bf _{10}$ $\bf( \mu g/m^3)$',ticks=[0,20,40,60],title=r'PM$\bf _{10}$',
							  plot_set=dict(label='PM$_{10}$',color='#fd3535'),label_pad=-3,
							  sca_set=dict(cmap='jet',vmin=10,vmax=60),
							  bar_title=r'PM$\rm _{10}$ ($\rm \mu g/m^3$)'),

				'PM25'  : dict(lim=(0, 60), label=r'PM$\bf _{2.5}$ $\bf( \mu g/m^3)$', title=r'PM$\bf _{2.5}$',
							  plot_set=dict(label='PM$_{2.5}$', color='#fd3535'), label_pad=-3,
							  sca_set=dict(cmap='jet', vmin=10, vmax=30),
							  bar_title=r'PM$\rm _{2.5}$ ($\rm \mu g/m^3$)'),

				'rec_PM25'  : dict(lim=(0,60),label=r'Reconstructed Mass $\bf( \mu g/m^3)$',ticks=[0,20,40,60],title=r'Reconstructed Mass',
							  plot_set=dict(label='Rec. Mass',color='#fd3535'),label_pad=-3,
							  sca_set=dict(cmap='jet',vmin=10,vmax=30),
							  bar_title=r'Rec. Mass ($\rm \mu g/m^3$)'),

				'PM1'   : dict(lim=(0,40),label=r'PM$\bf _{1}$ $\bf( \mu g/m^3)$',ticks=[0,10,20,30,40],title='PM1',
							  plot_set=dict(label='PM$_{1}$',color='#fd3535'),label_pad=-3,
							  sca_set=dict(cmap='jet',vmin=5,vmax=30),
							  bar_title=r'PM$\rm _{1.0}$ ($\rm \mu g/m^3$)'),

				'PM1NV'   : dict(lim=(0,40),label=r'PM$\bf _{1, NV}$ $\bf( \mu g/m^3)$',ticks=[0,10,20,30,40],title=r'PM$\bf _{1.0, NV}$',
							  plot_set=dict(label=r'PM$\rm _{1,NV}$',color='#ff7373'),label_pad=-3,
							  sca_set=dict(cmap='jet',vmin=5,vmax=30),
							  bar_title=r'PM$\rm _{1.0, NV}$ ($\rm \mu g/m^3$)'),

				'PM25_PM1NV' : dict(lim=(0,None),label=r'PM$\bf _{1.0-2.5}$ $\bf( \mu g/m^3)$',ticks=None,title=r'PM$\bf _{1.0-2.5}$',
								  plot_set=dict(label=r'PM$\rm _{1.0-2.5}$',color='#ff7373'),label_pad=-3,
								  sca_set=dict(cmap='jet',vmin=5,vmax=30),
								  bar_title=r'PM$\rm _{1.0-2.5}$'),

				'density' : dict(lim=(0.4,1.6),label=r'Density$\bf _{merge}$ ($\bf g/cm^3$)',title=r'Density$\bf _{merge}$',
							  plot_set=dict(color='#265cff',label='density'),label_pad=-3,label_pad_twin=-3,
							  sca_set=dict(cmap='jet',vmin=.6,vmax=1.2),
							  bar_set=dict(color_list=['#7396ff',],leg_nam=[r'Density$\rm _{merge}$ ($\rm g/cm^3$)',]),
							  bar_title=r'$\rm \rho_{merge}$'),

				'density05' : dict(lim=(0,2),label=r'Density <0.5 $\bf \mu m$ ($\bf g/cm^3$)',ticks=[0,.5,1,1.5,2],title=r'Density$\bf _{< 0.5 \mu m}$',
							  plot_set=dict(color='#5a82ff',label=r'density <0.5 $\rm \mu m$'),label_twin=None,
							  sca_set=dict(cmap='jet',vmin=.6,vmax=1.2),
							  bar_title=r'$\rm \rho  _{< 0.5 \mu m}$'),

				'PM1NV_TVC' : dict(lim=(0.4,1.6),label=r'PM$\bf _{1,NV}$/TVC ($\bf g/cm^3$)',ticks=[.4,.8,1.2,1.6],title=r'Density$\bf _{PM1}$',
								  plot_set=dict(color='#265cff',label='density'),label_pad=-3,
								  sca_set=dict(cmap='jet',vmin=.6,vmax=1.2),
								  bar_title=r'$\rm \rho_{PM1}$'),

				'PM1_TVC' : dict(lim=(0.4,1.6),label=r'PM$\bf _1$/TVC ($\bf g/cm^3$)',ticks=[.4,.8,1.2,1.6],nam='pm1-tvc',
								  plot_set=dict(color='#265cff',label='density'),label_pad=-3,
								  sca_set=dict(cmap='jet',vmin=.6,vmax=1.2),
								  bar_title=r'$\rm \rho (g/cm^3$)'),

				'PM25_TVC' : dict(lim=(0.4,1.6),label=r'PM$\bf _{2.5}$/TVC ($\bf g/cm^3$)',ticks=[.4,.8,1.2,1.6],title=r'Density$\bf _{PM2.5}$',
								  plot_set=dict(color='#265cff',label='density'),label_pad=-3,
								  sca_set=dict(cmap='jet',vmin=.6,vmax=1.2),
								  bar_title=r'$\rm \rho_{PM2.5} (g/cm^3$)'),

				'd_density' : dict(lim=(0.4,1.6),label=r'Density ($\bf g/cm^3$)',ticks=[.4,.8,1.2,1.6],nam='den',
							  plot_set=dict(color='#265cff',label='density'),label_pad=-3,
							  sca_set=dict(cmap='jet',vmin=.6,vmax=1.2),
							  bar_title=r'$\rm \rho (g/cm^3$)'),

				'density_all' : dict(lim=(0,1.6),label=r'Density no QC ($\bf g/cm^3$)',ticks=[0.,.4,.8,1.2,1.6],nam='den-all',
								  plot_set=dict(color='#265cff',label='density'),label_pad=-3,
								  sca_set=dict(cmap='jet',vmin=None,vmax=3.),
								  bar_title=r'$\rm \rho (g/cm^3$)'),

				'ASratio' : dict(lim=(0,.4),label=r'AS ratio',ticks=None,nam='asratio',
							  plot_set=dict(color='#265cff',label='AS ratio'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0.,vmax=.4),
							  bar_title=r'AS ratio'),

				'ANratio' : dict(lim=(0,.4),label=r'AN ratio',ticks=None,nam='anratio',
							  plot_set=dict(color='#265cff',label='AN ratio'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0.,vmax=.4),
							  bar_title=r'AN ratio'),

				'OMratio' : dict(lim=(.2,.8),label=r'OM ratio',ticks=None,nam='omratio',
							  plot_set=dict(color='#265cff',label='OM ratio'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=.2,vmax=.8),
							  bar_title=r'OM ratio'),

				'ebc_ug' : dict(lim=(0,4),label=r'eBC ($\bf \mu g/m^3$)',ticks=[0,1,2,3,4],
							  plot_set=dict(color='#333333',label='eBC'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=.2,vmax=None),
							  bar_title=r'eBC ($\rm \mug/m^3$)'),

				'eBC' : dict(lim=(0,4000),label=r'eBC ($\bf ng/m^3$)',ticks=[0,1000,2000,3e3,4e3],title='BC',
							  plot_set=dict(color='#333333',label='eBC'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=None,vmax=None),
							  box_set=dict(color_list=['#777777',],leg_nam=['eBC']),
							  bar_title=r'eBC ($\rm ng/m^3$)'),

				'T_EC' : dict(lim=(0,4),label=r'Thermal EC ($\bf \mu g/m^3$)',ticks=[0,1,2,3,4],
							  plot_set=dict(color='#333333',label='T_EC'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=.2,vmax=None),
							  bar_title=r'T_EC ($\rm \mug/m^3$)'),

				'O_EC' : dict(lim=(0,4),label=r'Optical EC ($\bf \mu g/m^3$)',ticks=[0,1,2,3,4],
							  plot_set=dict(color='#333333',label='O_EC'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=.2,vmax=None),
							  bar_title=r'O_EC ($\rm \mug/m^3$)'),

				'ALWC' : dict(lim=(0,60),label=r'ALWC ($\bf \mu g/m^3$)',ticks=[0,20,40,60],title='ALWC',
							  plot_set=dict(color='#333333',label='ALWC'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=10,vmax=40),
							  box_set=dict(color_list=['#4ca6ff',],leg_nam=[r'ALWC']),
							  bar_title=r'ALWC ($\rm \mu g/m^3$)'),

				'ALWCratio' : dict(lim=(0,1),label=r'ALWC/PM$\bf _{2.5}$',ticks=[0,.5,1],title=r'ALWC/PM$\bf _{2.5}$',
							  plot_set=dict(color='#333333',label='ALWC/PM$\rm _{2.5}$'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=.2,vmax=.8),
							  box_set=dict(color_list=['#4ca6ff',],leg_nam=[r'ALWC']),
							  bar_title=r'ALWC/PM$\rm _{2.5}$'),

				'pH' : dict(lim=(1,9),label=r'pH',ticks=[1,3,5,7,9],title='pH',
							  plot_set=dict(color='#333333',label='pH'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=10,vmax=40),
							  box_set=dict(color_list=['#c9ff26',],leg_nam=[r'pH']),
							  bar_title=r'pH'),

				'TVOC' : dict(lim=(0,300),label=r'TVOC (ppbv)',ticks=[0,100,200,300],
							  plot_set=dict(color='#333333',label='TVOC'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40),
							  bar_title=r'TVOC (ppbv)'),

				'LOH' : dict(lim=(0,30),label=r'LOH (s$\bf ^{-1}$)',ticks=[0,10,20,30],
							  plot_set=dict(color='#333333',label='LOH'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40),
							  bar_title=r'LOH (s$\rm ^{-1}$)'),

				'OFP' : dict(lim=(0,500),label=r'OFP (ppbv)',ticks=[0,250,500],
							  plot_set=dict(color='#333333',label='OFP'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40),
							  bar_title=r'OFP (ppbv)'),

				'VOC_consumed' : dict(lim=(0,150),label=r'VOC consumed (ppbv)',ticks=None,
							  plot_set=dict(color='#333333',label='VOC consumed'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=None,vmax=None),
							  bar_title=r'VOC consumed'),

				'OFP_initial' : dict(lim=(0,2000),label=r'OFP initial (ppbv)',ticks=None,
							  plot_set=dict(color='#333333',label='OFP initial'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=None,vmax=None),
							  bar_title=r'OFP initial'),

				'OFP_consumed' : dict(lim=(0,2000),label=r'OFP consumed (ppbv)',ticks=None,
							  plot_set=dict(color='#333333',label='OFP consumed'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=None,vmax=None),
							  bar_title=r'OFP consumed'),

				'SOAP' : dict(lim=(0,5),label=r'SOAP ($\bf \mu g/m^3$)',ticks=[0,2.5,5],
							  plot_set=dict(color='#333333',label='ALWC'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40),
							  bar_title=r'SOAP ($\rm \mu g/m^3$)'),

				'NOR' : dict(lim=(0,.5),label=r'NOR',ticks=[0,.1,.2,.3,.4,.5],
							  plot_set=dict(color='#333333',label='NOR'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0,vmax=.2),
							  bar_title=r'NOR'),

				'SOR' : dict(lim=(0,1),label=r'SOR',ticks=[0,.2,.4,.6,.8,1.],
							  plot_set=dict(color='#333333',label='SOR'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=.2,vmax=.8),
							  bar_title=r'SOR'),

				'SOCratio' : dict(lim=(0,1),label=r'SOC/PM$\bf _{2.5}$',ticks=[0,.2,.4,.6,.8,1.],
							  plot_set=dict(color='#333333',label='SOC ratio'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40),
							  bar_title=r'SOC ratio'),

				'SOC' : dict(lim=(0,20),label=r'SOC ($\bf \mu g/m^3$)',ticks=[0,10,20],
							  plot_set=dict(color='#333333',label='SOC'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=2,vmax=6),
							  bar_title=r'SOC ($\rm \mu g/m^3$)'),

				'POC' : dict(lim=(0,5),label=r'POC ($\bf \mu g/m^3$)',ticks=[0,2.5,5],
							  plot_set=dict(color='#333333',label='POC'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=1,vmax=4),
							  bar_title=r'POC ($\rm \mu g/m^3$)'),

				'O3' : dict(lim=(0,80),label=r'O$\bf _3$ (ppbv)',ticks=[0,20,40,60,80],
							  plot_set=dict(color='#333333',label='ALWC'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40),
							  bar_title=r'O3 (ppbv)'),

				'dO3' : dict(lim=(0,20),label=r'O$\bf _3$ gradient (ppbv/hr)',
							  plot_set=dict(color='#333333',label='dO$\rm _3$'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=None,vmax=None),
							  bar_title=r'dO$\rm _3$ (ppbv/hr)'),

				'Ox' : dict(lim=(0,80),label=r'O$\bf _x$ (ppbv)',ticks=[0,20,40,60,80],
							  plot_set=dict(color='#333333',label='O$\rm _x$'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=20,vmax=60),
							  bar_title=r'O$\rm _x$ (ppbv)'),

				'NH4' : dict(lim=(0,12),label=r'NH$\bf _4 ^+$ ($\bf \mu g/m^3$)',ticks=[0,3,6,9,12],
							  plot_set=dict(color='#333333',label='NH$\rm _4 ^+$'),label_pad=-10,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40),
							  bar_title=r'NH$\rm _4 ^+$ ($\rm \mu g/m^3$)'),

				'SO4' : dict(lim=(0,12),label=r'SO$\bf _4 ^{2-}$ ($\bf \mu g/m^3$)',ticks=[0,3,6,9,12],
							  plot_set=dict(color='#333333',label='SO$\rm _4 ^{2-}$'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40),
							  bar_title=r'SO$\rm _4 ^{2-}$ ($\rm \mu g/m^3$)'),

				'NO3' : dict(lim=(0,12),label=r'NO$\bf _3 ^-$ ($\bf \mu g/m^3$)',ticks=[0,3,6,9,12],
							  plot_set=dict(color='#333333',label='NO$\rm _3 ^-$'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40),
							  bar_title=r'NO$\rm _3 ^-$ ($\rm \mu g/m^3$)'),

				'NO2' : dict(lim=(0,60),label=r'NO$\bf _2$ (ppb)',ticks=[0,20,40,60],title=r'NO$\bf _2$',
							  plot_set=dict(color='#333333',label='NO$\rm _2$'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40),
							  box_set=dict(color_list=['#7396ff',],leg_nam=[r'NO$\rm _2$']),
							  bar_title=r'NO$\rm _2$ (ppb)'),

				'SO2' : dict(lim=(0,5),label=r'SO$\bf _2$ (ppb)',ticks=[0,1,2,3,4,5],title=r'SO$\bf _2$',
							  plot_set=dict(color='#333333',label='SO$\rm _2$'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40),
							  box_set=dict(color_list=['#ff7373',],leg_nam=[r'SO$\rm _2$']),
							  bar_title=r'SO$\rm _2$ (ppb)'),

				'uNH4' : dict(lim=(0,.8), label=r'NH$\bf _4 ^+$ ($\bf \mu mol/m^3$)', 
							  plot_set=dict(color='#333333',label='NH$\rm _4 ^+$'), label_pad=5,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40), tick_pad=5,
							  bar_title=r'NH$\rm _4 ^+$ ($\rm \mu mol/m^3$)'),

				'uSO4_uNO3' : dict(lim=(0,.8), label=r'2SO$\bf _4 ^{2-}$+NO$\bf _3 ^-$ ($\bf \mu mol/m^3$)', 
							  plot_set=dict(color='#333333',label='2SO$\rm _4 ^{2-}$+NO$\bf _3 ^-$'), label_pad=5,
							  sca_set=dict(cmap='jet',vmin=0,vmax=40), tick_pad=5,
							  bar_title=r'2SO$\rm _4 ^{2-}$+NO$\bf _3 ^-$'),

				'PM_frac' : dict(lim=(0,1),label=r'$\bf PM_{1.0, NV}/PM_{2.5}$',ticks=[0,.2,.4,.6,.8,1.],title=r'$\bf PM_{1.0,NV}/PM_{2.5}$',
							  plot_set=dict(color='#333333',label=r'$\rm PM_{frac}$'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=.2,vmax=1),
							  box_set=dict(color_list=['#888888'],leg_nam=['PM fraction']),
							  bar_title=r'$\rm PM_{frac}$'),

				'all_PM_frac' : dict(lim=(0,1.),label=r'Ratio',ticks=[0,.2,.4,.6,.8,1.],title=r'PM Fraction',
							  bar_title=r'$\rm PM_{frac}$'),

				'Opt_coe' : dict(lim=(0,12),label=r'Optical Coe.',ticks=[0,4,8,12],title=r'Optical Coefficient',
							  plot_set=dict(color='#333333',label=r'Opt. Coe.'),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=3,vmax=8),
							  bar_title=r'Opt. Coe.'),

				'mass_coe' : dict(lim=(0,90), label=r'Mass Concentration ($\bf \mu g/m^3$)', title=r'Mass Concentration',
							  plot_set=dict(color='#333333',label=r'PM'), label_pad=0,
							  sca_set=dict(cmap='jet',vmin=10,vmax=50),
							  bar_title=r'PM'),

				'rec_mass' : dict(lim=(0,60), label=r'Mass Concentration ($\bf \mu g/m^3$)',
							  plot_set=dict(color='#333333',label=r''),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=10,vmax=50),
							  bar_title=r''),

				'rec_mass_pm25' : dict(lim=(0,.6),label=r'Ratio' ,title=r'Chemical Compound / PM$\bf _{2.5}$',
							  plot_set=dict(color='#333333',label=r''),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=10,vmax=50),
							  bar_title=r''),

				'second_ratio' : dict(lim=(0,.5),label=r'Ratio',ticks=[0,.25,.5],title=r'Ratio',
								  plot_set=dict(color='#333333',label=r''),label_pad=0,
								  sca_set=dict(cmap='jet',vmin=10,vmax=50),bar_set=dict(color_list=['#f56373','#b7dbbb',],leg_nam=[r'SOR',r'NOR']),
								  bar_title=r''),

				'second_gas' : dict(lim=(0,40),label=r'Gas (ppb)',ticks=[0,10,20,30,40],title=r'Gas',
								  plot_set=dict(color='#333333',label=r''),label_pad=0,
								  sca_set=dict(cmap='jet',vmin=10,vmax=50),bar_set=dict(color_list=['#7396ff','#ff7373',],leg_nam=[r'NO$\rm _2$',r'SO$\rm _2$',]),
								  bar_title=r'',box_set=dict(color_list=['#7396ff','#ff7373',],leg_nam=[r'NO$\rm _2$',r'SO$\rm _2$',])),

				'second_gas_nox_ox' : dict(lim=(0,80),label=r'NO$\bf _x$ and O$\bf _x$ (ppb)',ticks=[0,20,40,60,80],title=r'Gas',
										  plot_set=dict(color='#333333',label=r''),label_pad=0,
										  sca_set=dict(cmap='jet',vmin=10,vmax=50),bar_set=dict(color_list=['#7396ff','#bbbbbb',],leg_nam=[r'NO$\rm _x$',r'O$\rm _x$',]),
										  bar_title=r'',box_set=dict(color_list=['#7396ff','#bbbbbb',],leg_nam=[r'NO$\rm _x$',r'O$\rm _x$'])),

				'second_gas_no2_ox' : dict(lim=(0,80),label=r'NO$\bf _2$ and O$\bf _x$ (ppb)',ticks=[0,20,40,60,80],title=r'Gas',
										  plot_set=dict(color='#333333',label=r''),label_pad=0,
										  sca_set=dict(cmap='jet',vmin=10,vmax=50),bar_set=dict(color_list=['#7396ff','#bbbbbb',],leg_nam=[r'NO$\rm _2$',r'O$\rm _x$',]),
										  bar_title=r'',box_set=dict(color_list=['#7396ff','#bbbbbb',],leg_nam=[r'NO$\rm _2$',r'O$\rm _x$'])),

				'OCgrp' : dict(lim=(0,10),label=r'Mass Concentration ($\bf \mu g/m^3$)',ticks=[0,5,10,],title=r'Mass Concentration',
							  plot_set=dict(color='#333333',label=r''),label_pad=0,
							  sca_set=dict(cmap='jet',vmin=10,vmax=50),
							  bar_title=r''),

				'pieExt' : dict(color=['#007b87','#e08e70','#6bbab1','#ffaf95',],
								leg_nam=[r'b$\rm _{sp}$',r'b$\rm _{ap}$',r'b$\rm _{sg}$',r'b$\rm _{ag}$',],
								leg_title=None,
								text_title='Extinction (1/Mm)',),

				'pieIMPROVE' : dict(color=['#FFFF33','#FF3333','#33FF33','#5555FF','#B94FFF','#AAAAAA',],
										leg_nam=['OM','AS','AN','Soil','SS','EC'],
										leg_title=None,
										text_title='Rec. Ext.',),

				'pieEvent' : dict(text_nam=['Event','Total','Clean']),

				'pie_reconstruc' : dict(color=['#FFFF33','#FF3333','#33FF33','#5555FF','#B94FFF','#AAAAAA',],
										leg_nam=['OM','AS','AN','Soil','SS','EC'],
										leg_title=None,
										text_title='Rec. Mass',),

				'pieCase' : dict(text_nam=['Start','Increase','Peak','Decrease','End']),

				'typ_reconstruc' : dict(color_list=['#FFFF33','#FF3333','#33FF33','#5555FF','#B94FFF','#AAAAAA',],
										leg_nam=['OM','AS','AN','Soil','SS','EC']),

				'typ_reconstruc2' : dict(color_list=['#FFFF33','#e5153f','#00d400','#ff8f1e','#5555FF','#B94FFF','#AAAAAA',],
										 leg_nam=['OM','Sulfate','Nitrate','Ammonia','Soil','SS','EC']),

				'typ_spr2022_sm2022_au2022' : dict(color_list=['#b9e6ff','#4b96ce','#ffa9a3','#f87575',],
												   leg_nam=['2022 Spring','2022 Summer','2022 Autumn']),

				'typ_optcoe' : dict(color_list=['#95D5B2','#52B788','#2D6A4F','#f87575',],leg_nam=['MEE','MSE','MAE']),

				'typ_1um_25um' : dict(color_list=['#d2d9eb','#248ca1',],leg_nam=[r'< 1 $\rm \mu$m',r'< 2.5 $\rm \mu$m']),
												   
				'typ_OCgrp' : dict(color_list=['#dde5b6','#a98467',],leg_nam=['POC','SOC']),
												   
				'typ_all_PM_frac' : dict(color_list=['#6c757d','#ced4da',],leg_nam=[r'PM$\rm _{2.5}$/PM$\rm _{10}$',r'PM$\rm _{1.0,NV}$/PM$\rm _{2.5}$']),

				'typ_PM' : dict(color_list=['#f08080','#f8ad9d','#ffdab9',],leg_nam=[r'PM$\rm _{10}$',r'PM$\rm _{2.5}$',r'PM$\rm _{1.0,NV}$']),

				'clasfyRH' : dict(tick_nam=['<60','60-70','70-80','80-90','>90'],clasfy_nam=['<60','60-70','70-80','80-90','>90'],xlabel='RH (%)'),

				'clasfyOx' : dict(tick_nam=['<30','30-40','40-50','50-60','>60'],clasfy_nam=['<30','30-40','40-50','50-60','>60'],xlabel='Ox (ppb)'),

				'clasfyALWC' : dict(tick_nam=['<3','3-6','6-9','>9'],clasfy_nam=['<3','3-6','6-9','>9'],xlabel=r'ALWC ($\bf \mu g/m^3$)',xlabelpad=-5),

				'clasfyALWCratio' : dict(tick_nam=['<0.25','0.25-0.5','0.5-0.75','>0.75'],clasfy_nam=['<0.25','0.25-0.5','0.5-0.75','>0.75'],xlabel=r'ALWC/PM$\rm _{2.5}$'),

				'clasfyEvent' : dict(tick_nam=['Total','Event','Clean'], clasfy_nam=['all','event','clean'], 

									 line_set=[dict(label='total',color='#ffb703',lw=2), dict(label='event',color='#023047',lw=2), 
											   dict(label='clean',color='#8ecae6',lw=2)],

									 sca_set=[dict(label='total',color='#ffb703'), dict(label='event',color='#023047'), 
											  dict(label='clean',color='#8ecae6')]
									),

				'clasfyCase' : dict(tick_nam=['Start','Increase','Peak','Decrease','End'],clasfy_nam=['Start','Increase','Peak','Decrease','End']),
				# 'clasfyCase' : dict(tick_nam=['蔥肉卷','圓甜不辣','牛肋條','爆卵柳葉魚','雞軟骨串'],clasfy_nam=['A','B','C','D','E']),

				'clasfyAmmonia' : dict(tick_nam=['Over Excess','Excess'],clasfy_nam=['over_excess','excess']),
				
				'clasfyEnhance' : dict(line_set=[dict(label='clean',color='#247c03',lw=2),dict(label='event',color='#ff2626',lw=2)]),

				'clasfyCase_5stg' : dict(line_set=[dict(label='st.',color='#ffb703',lw=2), dict(label='incr.',color='#fb8500',lw=2), 
												   dict(label='peak',color='#023047',lw=2), dict(label='decr.',color='#219ebc',lw=2),
												   dict(label='ed.',color='#8ecae6',lw=2)],
										 sca_set=[dict(label='st.',color='#ffb703'), dict(label='incr.',color='#fb8500'), 
												  dict(label='peak',color='#023047'), dict(label='decr.',color='#219ebc'),
												  dict(label='ed.',color='#8ecae6')]),

				'clasfyCase_event' : dict(line_set=[dict(label='E1',color='#00799d',lw=2), dict(label='E2',color='#00afb9',lw=2), 
												  dict(label='E3',color='#fed9b7',lw=2), dict(label='E4',color='#f07167',lw=2),
												  dict(label='E5',color='#f7a58f',lw=2), dict(label='E6',color='#7fd6cb',lw=2),],
										 sca_set=[dict(label='E1',color='#00799d'), dict(label='E2',color='#00afb9'), 
												  dict(label='E3',color='#fed9b7'), dict(label='E4',color='#f07167'),
												  dict(label='E5',color='#f7a58f'), dict(label='E6',color='#7fd6cb'),]),
												  # dict(label='ed.',color='#8ecae6')]),

				# 'clasfyEnhance_chem' : dict(line_set=[dict(label='OM',color='#91da6e',lw=2), dict(label='AS',color='#e63946',lw=2), 
												  # dict(label='AN',color='#458a9d',lw=2), dict(label='Soil',color='#cb997e',lw=2),
												  # dict(label='SS',color='#0096c7',lw=2), dict(label='EC',color='#1d3557',lw=2),],
											 # sca_set=[dict(label='E1',color='#00799d'), dict(label='E2',color='#00afb9'), 
													  # dict(label='E3',color='#fed9b7'), dict(label='E4',color='#f07167'),
													  # dict(label='E5',color='#f7a58f'), dict(label='E6',color='#7fd6cb'),]),
												  # dict(label='ed.',color='#8ecae6')]),

				'clasfyEnhance_chem' : dict(line_set=[dict(label='OM',color='#91da6e',lw=2), dict(label='AS',color='#e63946',lw=2), 
													  dict(label='AN',color='#458a9d',lw=2), dict(label='all',color='#000000',lw=2)]),

				'clasfyPNSD_chem_all' : dict(line_set=[dict(label='low OM',color='#91da6e',lw=2,ls='--'), dict(label='high OM',color='#489325',lw=2), 
														  dict(label='low AS',color='#f2939a',lw=2,ls='--'), dict(label='high AS',color='#e63946',lw=2),
														  dict(label='low AN',color='#00aee5',lw=2,ls='--'), dict(label='high AN',color='#008ebd',lw=2),
														  dict(label='low all',color='#555555',lw=2,ls='--'), dict(label='high all',color='#000000',lw=0),
														  dict(label='ref',color='#000000',lw=2,ls='--'),]),

				'clasfyPNSD_chem_ref' : dict(line_set=[dict(label='OM',color='#489325',lw=2), dict(label='AS',color='#e63946',lw=2),
														dict(label='AN',color='#008ebd',lw=2), dict(label='ref low',color='#797979',lw=2,ls='--'),
														dict(label='ref median',color='#000000',lw=2,ls='--'),]),

				'clasfyEnhance_chem_ref' : dict(line_set=[dict(label='OM',color='#489325',lw=2), dict(label='AS',color='#e63946',lw=2),
														  dict(label='AN',color='#008ebd',lw=2), dict(label='all',color='#797979',lw=2,ls='--')]),

				'clasfyEnhance_cplx_chem_ref' : dict(line_set=[dict(label='AS + AN',color='#f7a072',lw=2), dict(label='OM + AN',color='#9dbb94',lw=2),
															   dict(label='OM + AS',color='#d9ba42',lw=2), dict(label='all',color='#797979',lw=2,ls='--')]),

				'clasfyPNSD_cplx_chem_ref' : dict(line_set=[dict(label='AS + AN (low OM)',color='#f7a072',lw=2), dict(label='OM + AN (low AS)',color='#9dbb94',lw=2),
															dict(label='OM + AS (low AN)',color='#d9ba42',lw=2), dict(label='ref low',color='#797979',lw=2,ls='--'),
															dict(label='ref median',color='#000000',lw=2,ls='--'),]),

				'clasfyEnhance_pdf_cdf' : dict(line_set=[dict(label='OM',color='#91da6e',lw=2), dict(label='AS',color='#e63946',lw=2), 
														 dict(label='AN',color='#458a9d',lw=2), dict(label='all',color='#000000',lw=2)]),

				'clasfyCase_3stg' : dict(line_set=[dict(label='st.',color='#ffb703',lw=2), 
												   dict(label='peak',color='#023047',lw=2),
												   dict(label='ed.',color='#8ecae6',lw=2)]),

				'clasfySeason_2022' : dict(line_set=[dict(label='2022 Spr.',color='#00b9a5',lw=2), dict(label='2022 Sum.',color='#f07167',lw=2), 
													 dict(label='2022 Aut.',color='#fed9b7',lw=2), dict(label='2022 Win.',color='#00799d',lw=2),],
										   sca_set=[dict(label='2022 Spr.',color='#00b9a5'), dict(label='2022 Sum.',color='#f07167'), 
													 dict(label='2022 Aut.',color='#fed9b7'), dict(label='2022 Win.',color='#00799d'),]),

				'number_line' : dict(xlim=(10,1e4), ylim=(0,8e4), xscale='log', xlabel='Diameter (nm)', ylabel=r'dN/dlogD$\bf _p$',),

				'surface_line' : dict(xlim=(10,1e4), ylim=(0,1.2e9), xscale='log', xlabel='Diameter (nm)', ylabel=r'dS/dlogD$\bf _p$'),

				'volume_line' : dict(xlim=(10,1e4), ylim=(0,8e10), xscale='log', xlabel='Diameter (nm)', ylabel=r'dV/dlogD$\bf _p$'),

				'enhance_line' : dict(xlim=(10,1e4), ylim=(-1,5), xscale='log', xlabel='Diameter (nm)', ylabel=r'Enhancement Ratio'),

				'ext_enhance_line' : dict(xlim=(10,1e4), ylim=(0,5), xscale='log', xlabel='Diameter (nm)', ylabel=r'Enhancement Ratio'),

				'ext_SD_line' : dict(xlim=(10,1e4), ylim=(0,450), xscale='log', xlabel='Diameter (nm)', ylabel=r'd$\bf \sigma$/dlogD$\bf _p$ (1/Mm)' ),

				'mass_frac_stat_line' : dict(xlim=(0,50), ylim=(0,1), xlabel='Mass Fraction (%)', ylabel=r'Probability' ),



				}



clasfy_setting = {

				'summer_2020' : {
								'basic' : dict(nam='sum2020',title='2020 Summer'),

								},

				'autumn_2020' : {
								'basic' : dict(nam='aut2020',title='2020 Autumn'),

								},

				'winter_2020' : {
								'basic' : dict(nam='win2020',title='2020 Winter'),

								},

				'spring_2021' : {
								'basic' : dict(nam='spr2021',title='2021 Spring'),

								},

				'summer_2021' : {
								'basic' : dict(nam='sum2021',title='2021 Summer'),

								},

				'autumn_2021' : {
								'basic' : dict(nam='aut2021',title='2021 Autumn'),
								# 'ext'  : dict(lim=(0,300),label=r'Extinction (1/Mm)',ticks=[0,100,200,300],nam='ext',
											  # plot_set=dict(label='Ext.',color='#4c79ff'),
											  # sca_set=dict(cmap='jet',vmin=30,vmax=150),
											  # bar_title='Ext. (1/Mm)'),

								},

				'spring_2022' : {
								'basic' : dict(nam='spr2022',title='2022 Spring'),
								# 'ext'  : dict(lim=(0,300),label=r'Extinction (1/Mm)',ticks=[0,100,200,300],nam='ext',
											  # plot_set=dict(label='Ext.',color='#4c79ff'),
											  # sca_set=dict(cmap='jet',vmin=30,vmax=150),
											  # bar_title='Ext. (1/Mm)'),
								},

				'summer_2022' : {
								'basic' : dict(nam='sum2022',title='2022 Summer'),

								# 'MAE'   : dict(lim=(0,4),label=r'MAE (m$\bf ^2$/g)',ticks=[0,2,4],nam='mae',
											  # plot_set=dict(label='MAE',color='#fd3535'),
											  # sca_set=dict(cmap='jet',vmin=.5,vmax=3),
											  # bar_title=r'MAE (m$\rm ^2$/g)'),
								},

				'autumn_2022' : {
								'basic' : dict(nam='aut2022',title='2022 Autumn'),

								},

				'winter_2022' : {
								'basic' : dict(nam='win2022',title='2022 Winter'),

								},

				'event' : {
								'basic' : dict(nam='event', title=''),

								'rec_ext' : dict(lim=(0,100),  sca_set=dict(cmap='jet',vmin=30,vmax=120),),

								'rec_mass' : dict(lim=(0,20),  sca_set=dict(cmap='jet',vmin=10,vmax=50),),

								'TNC'  : dict(lim=(0,6e4), sca_set=dict(cmap='jet',vmin=2e4,vmax=4e4),),

								'TSC_um2'  : dict(lim=(0,800), sca_set=dict(cmap='jet',vmin=100,vmax=600),),

								'TVC_um3'  : dict(lim=(0,40), sca_set=dict(cmap='jet',vmin=10,vmax=30),),
								},

				'event_2023_aut' : {
								'basic' : dict(nam='event', title='2023 Aut. Event'),

								'rec_ext' : dict(lim=(0,100),  sca_set=dict(cmap='jet',vmin=30,vmax=120),),

								'rec_mass' : dict(lim=(0,20),  sca_set=dict(cmap='jet',vmin=10,vmax=50),),

								'TNC'  : dict(lim=(0,6e4), sca_set=dict(cmap='jet',vmin=2e4,vmax=4e4),),

								'ext'  : dict(lim=(0,500), sca_set=dict(cmap='jet',vmin=20,vmax=400), twin_label_pad=27),

								'TSC_um2'  : dict(lim=(0,800), sca_set=dict(cmap='jet',vmin=100,vmax=600),),

								'TVC_um3'  : dict(lim=(0,50), sca_set=dict(cmap='jet',vmin=10,vmax=30),),
								},

				'event_2023_spr' : {
								'basic' : dict(nam='event', title='2023 Spr. Event'),

								'rec_ext' : dict(lim=(0,100),  sca_set=dict(cmap='jet',vmin=30,vmax=120),),

								'rec_mass' : dict(lim=(0,20),  sca_set=dict(cmap='jet',vmin=10,vmax=50),),

								'TNC'  : dict(lim=(0,6e4), sca_set=dict(cmap='jet',vmin=2e4,vmax=4e4),),

								'ext'  : dict(lim=(0,350), sca_set=dict(cmap='jet',vmin=50,vmax=300), twin_label_pad=27,),

								'TSC_um2'  : dict(lim=(0,800), sca_set=dict(cmap='jet',vmin=100,vmax=600),),

								'TVC_um3'  : dict(lim=(0,50), sca_set=dict(cmap='jet',vmin=10,vmax=30),),
								},

				'event_2023_sum' : {
								'basic' : dict(nam='event', title='2023 Sum. Event'),

								'rec_ext' : dict(lim=(0,100),  sca_set=dict(cmap='jet',vmin=30,vmax=120),),

								'rec_mass' : dict(lim=(0,20),  sca_set=dict(cmap='jet',vmin=10,vmax=50),),

								'TNC'  : dict(lim=(0,6e4), sca_set=dict(cmap='jet',vmin=2e4,vmax=4e4),),

								'ext'  : dict(lim=(0,200), sca_set=dict(cmap='jet',vmin=20,vmax=400), twin_label_pad=27,),

								'TSC_um2'  : dict(lim=(0,800), sca_set=dict(cmap='jet',vmin=100,vmax=600),),

								'TVC_um3'  : dict(lim=(0,50), sca_set=dict(cmap='jet',vmin=10,vmax=30),),
								},

				'phy_chem' : {
								'basic' : dict(nam='phy_chem', title=''),

								'number_line' : dict(xlim=(10,1e4), ylim=(0,8e4), xscale='log', 
													 xlabel='Diameter (nm)', ylabel=r'dN/dlogD$\bf _p$',),

								'surface_line' : dict(xlim=(10,1e4), ylim=(0,8e8), xscale='log', 
													  xlabel='Diameter (nm)', ylabel=r'dS/dlogD$\bf _p$'),

								'volume_line' : dict(xlim=(10,1e4), ylim=(0,4.5e10), xscale='log', 
													 xlabel='Diameter (nm)', ylabel=r'dV/dlogD$\bf _p$'),

								'pie_reconstruc' : dict(color=['#91da6e','#e63946','#458a9d','#bbbbbb','#bbbbbb','#bbbbbb',],
														leg_nam=['OM','AS','AN','Soil','SS','EC'],
														leg_title=None,
														text_title='',),

								# 'rec_ext' : dict(lim=(0,100),  sca_set=dict(cmap='jet',vmin=30,vmax=120),),

								# 'rec_mass' : dict(lim=(0,20),  sca_set=dict(cmap='jet',vmin=10,vmax=50),),

								# 'TNC'  : dict(lim=(0,6e4), sca_set=dict(cmap='jet',vmin=2e4,vmax=4e4),),

								# 'TSC_um2'  : dict(lim=(0,800), sca_set=dict(cmap='jet',vmin=100,vmax=600),),

								# 'TVC_um3'  : dict(lim=(0,40), sca_set=dict(cmap='jet',vmin=10,vmax=30),),
								},



				}













## temp
"""
				'2022-11-17 ~ 2022-11-23' : {
								'basic' : dict(nam='event', title=''),

								'rec_ext' : dict(lim=(0,100),  sca_set=dict(cmap='jet',vmin=30,vmax=120),),

								'rec_mass' : dict(lim=(0,20),  sca_set=dict(cmap='jet',vmin=10,vmax=50),),

								'TNC'  : dict(lim=(0,6e4), sca_set=dict(cmap='jet',vmin=2e4,vmax=4e4),),

								'TSC_um2'  : dict(lim=(0,800), sca_set=dict(cmap='jet',vmin=100,vmax=600),),

								'TVC_um3'  : dict(lim=(0,40), sca_set=dict(cmap='jet',vmin=10,vmax=30),),
								},

				'2022-11-08 ~ 2022-11-14' : {
								'basic' : dict(nam='event', title=''),

								'rec_ext' : dict(lim=(0,100),  sca_set=dict(cmap='jet',vmin=30,vmax=120),),

								'rec_mass' : dict(lim=(0,20),  sca_set=dict(cmap='jet',vmin=10,vmax=50),),

								'TNC'  : dict(lim=(0,6e4), sca_set=dict(cmap='jet',vmin=2e4,vmax=4e4),),

								'TSC_um2'  : dict(lim=(0,800), sca_set=dict(cmap='jet',vmin=100,vmax=600),),

								'TVC_um3'  : dict(lim=(0,50), sca_set=dict(cmap='jet',vmin=10,vmax=30),),
								},

				'2022-04-03 ~ 2022-04-13' : {
								'basic' : dict(nam='event', title=''),

								'rec_ext' : dict(lim=(0,100),  sca_set=dict(cmap='jet',vmin=30,vmax=120),),

								'rec_mass' : dict(lim=(0,20),  sca_set=dict(cmap='jet',vmin=10,vmax=50),),

								'TNC'  : dict(lim=(0,6e4), sca_set=dict(cmap='jet',vmin=2e4,vmax=4e4),),

								'TSC_um2'  : dict(lim=(0,800), sca_set=dict(cmap='jet',vmin=100,vmax=600),),

								'TVC_um3'  : dict(lim=(0,40), sca_set=dict(cmap='jet',vmin=10,vmax=30),),
								},

				'2022-08-23 ~ 2022-08-25' : {
								'basic' : dict(nam='event', title=''),

								'rec_ext' : dict(lim=(0,100),  sca_set=dict(cmap='jet',vmin=30,vmax=120),),

								'rec_mass' : dict(lim=(0,20),  sca_set=dict(cmap='jet',vmin=10,vmax=50),),

								'TNC'  : dict(lim=(0,6e4), sca_set=dict(cmap='jet',vmin=2e4,vmax=4e4),),

								'TSC_um2'  : dict(lim=(0,800), sca_set=dict(cmap='jet',vmin=100,vmax=600),),

								'TVC_um3'  : dict(lim=(0,40), sca_set=dict(cmap='jet',vmin=10,vmax=30),),
								},

# """