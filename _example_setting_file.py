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

				# pie plot
				'pieExt' : dict(color=['#007b87','#e08e70','#6bbab1','#ffaf95',],
								leg_nam=[r'b$\rm _{sp}$',r'b$\rm _{ap}$',r'b$\rm _{sg}$',r'b$\rm _{ag}$',],
								leg_title=None,
								text_title='Extinction (1/Mm)',),

				'pieEvent' : dict(text_nam=['Event','Total','Clean']),


				# line plot
				'volume_line' : dict(xlim=(10,1e4), ylim=(0,8e10), xscale='log', xlabel='Diameter (nm)', ylabel=r'dV/dlogD$\bf _p$'),

				'clasfyEnhance' : dict(line_set=[dict(label='clean',color='#247c03',lw=2), dict(label='event',color='#ff2626',lw=2)]),


				# classify bar plot
				'typ_reconstruc' : dict(color_list=['#FFFF33','#FF3333','#33FF33','#5555FF','#B94FFF','#AAAAAA',],
										leg_nam=['OM','AS','AN','Soil','SS','EC']),

				'clasfyEvent' : dict(tick_nam=['Total','Event','Clean'], clasfy_nam=['all','event','clean'], 

									 line_set=[dict(label='total',color='#ffb703',lw=2), dict(label='event',color='#023047',lw=2), 
											   dict(label='total',color='#8ecae6',lw=2)],

									 sca_set=[dict(label='all',color='#ffb703'), dict(label='event',color='#023047'), 
											  dict(label='clean',color='#8ecae6')]
									),


				# box plot
				'typ_PM' : dict(color_list=['#f08080','#f8ad9d','#ffdab9',], leg_nam=[r'PM$\rm _{10}$',r'PM$\rm _{2.5}$',r'PM$\rm _{1.0,NV}$']),


				# single parameter
				'ext'  : dict(lim=(0,450), label=r'Extinction (1/Mm)', title='Extinction',
							  plot_set=dict(label='Ext.', color='#4c79ff'),
							  sca_set=dict(cmap='jet', vmin=0, vmax=200),
							  box_set=dict(color_list=['#6facd8',], leg_nam=['Extinction']),
							  bar_title='Ext. (1/Mm)'),

				'PM25'  : dict(lim=(0,60),label=r'PM$\bf _{2.5}$ $\bf( \mu g/m^3)$',ticks=[0,20,40,60],title=r'PM$\bf _{2.5}$',
							  plot_set=dict(label='PM$_{2.5}$',color='#fd3535'),label_pad=-3,
							  sca_set=dict(cmap='jet',vmin=10,vmax=30),
							  bar_title=r'PM$\rm _{2.5}$ ($\rm \mu g/m^3$)'),

				'MSE'  : dict(lim=(0,12),label=r'MSE (m$\bf ^2$/g)',ticks=[0,4,8,12],title='MSE',
							  plot_set=dict(label='MSE',color='#fd3535'),label_pad=-5,
							  sca_set=dict(cmap='jet',vmin=2,vmax=8),
							  bar_title=r'MSE (m$\rm ^2$/g)'),

				'GMD'  : dict(lim=(10,70),label=r'GMD (nm)', ticks=[10,30,50,70],title='GMD',
							  plot_set=dict(label='GMD',color='#fd3535'),
							  sca_set=dict(cmap='jet',vmin=20,vmax=50),
							  bar_set=dict(color_list=['#7396ff',],leg_nam=[r'GMD (nm)',]),
							  bar_title=r'GMD (nm)',leg_title=r'GMD'),

				'rec_mass' : dict(lim=(0,60), label=r'Mass Concentration ($\bf \mu g/m^3$)',
							  plot_set=dict(color='#333333',label=r''), label_pad=0,
							  sca_set=dict(cmap='jet',vmin=10,vmax=50),
							  bar_title=r''),

				'mass_coe' : dict(lim=(0,90), label=r'Mass Concentration ($\bf \mu g/m^3$)', title=r'Mass Concentration',
							  plot_set=dict(color='#333333',label=r'PM'), label_pad=0,
							  sca_set=dict(cmap='jet',vmin=10,vmax=50),
							  bar_title=r'PM'),





				}



clasfy_setting = {

				'summer_2020' : {
								'basic' : dict(nam='sum2020',title='2020 Summer'),

								'rec_ext' : dict(lim=(0,100),  sca_set=dict(cmap='jet',vmin=30,vmax=120),),

								'clasfyEvent' : dict(tick_nam=['Total','Event','Clean'], clasfy_nam=['all','event','clean'], 

													 line_set=[dict(label='total',color='#ffb703',lw=2), dict(label='event',color='#023047',lw=2), 
															   dict(label='total',color='#8ecae6',lw=2)],

													 sca_set=[dict(label='all',color='#ffb703'), dict(label='event',color='#023047'), 
															  dict(label='clean',color='#8ecae6')]
													),



								},


				}




