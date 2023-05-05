
from datetime import datetime as dtm
from datetime import timedelta as dtmdt
from pandas import date_range, concat, DataFrame, to_numeric, cut, qcut
from pathlib import Path
import numpy as n
np = n

from PlotTemplate.core.func import *




## plot function
@_template_setting(figsize=_cm2inch(33.87, 8.47), dirnam='timeSeries', fs=22)
def tmSeries(st_tm, ed_tm, _df_val, main_set, twin_val=None, twin_set=None, split_date=None, tick_tm=None, show_leg=True,
			 print_date=False, show_xtick=True, show_twin_ytick=True, show_yr=True, show_twin_label=True,
			 minor_freq='1d', **kwarg):

	main_set.update(kwarg)
	out_nam = main_set["out_nam"]
	print(f'tmSeries : ', end='')

	## parameter
	fig, ax, fs, font_dic_norm, font_dic_bold = kwarg['fig'], kwarg['ax'], kwarg['fs'], kwarg['font_dic_norm'], kwarg['font_dic_bold']

	tick_tm = tick_tm or (st_tm, ed_tm)
	tick = main_set.get('xticks')
	if tick is None:
		tick = date_range(*tick_tm, freq=main_set['tick_freq'])

	minor_tick = date_range(st_tm, ed_tm, freq=minor_freq)
	title_pad = 15

	## plot
	ln1, = ax.plot(_df_val, **main_set['plot_set'])

	ax.tick_params(labelsize=fs, pad=10, labelbottom=False)
	ax.tick_params(axis='x', length=6, width=1.5)
	ax.set(xlim=(st_tm, ed_tm))

	ax = _pic_set(ax, 'y', main_set, fs, font_dic_bold)

	if split_date is not None: 
		ax.vlines(split_date, *ax.get_ylim(), color='#000000', ls='-', lw=2)

		if print_date:
			ax.text(split_date, ax.get_ylim()[-1], split_date.strftime('%Y-%m-%d'), ha='center', va='bottom', **font_dic_bold)
			title_pad = 35

	if twin_set is not None:
		twin_set.update(kwarg)
		_twin = twin_set

		axt = ax.twinx()
		ln2, = axt.plot(twin_val, **_twin['twin_plot_set'])

		axt.tick_params(labelsize=fs, labelright=False, pad=10)

		_ytick_twin = _twin.get('twin_yticks', None)
		axt.tick_params(labelright=show_twin_ytick, right=show_twin_ytick)
		axt.set_yticks(_ytick_twin or _auto_ticks(*_twin['twin_ylim']) or axt.get_yticks(), 
					   _ytick_twin or _auto_ticks(*_twin['twin_ylim']) or axt.get_yticklabels())

		if show_twin_label:
			axt.set_ylabel(_twin['twin_ylabel'], rotation=-90, labelpad=_twin.get('twin_ylabel_pad') or 30, **font_dic_bold)

		axt.set(ylim=_twin['twin_ylim'])

		if show_leg: 
			ax.legend(handles=[ln1,ln2], framealpha=0, fontsize=fs-2.)

		if _twin['out_nam'] is not None:
			out_nam += f"-{_twin['out_nam']}"

	ax.set_xticks(tick)
	ax.set_xticks(minor_tick, minor=True)
	if show_xtick:
		ax.tick_params(labelbottom=True)
		ax.set_xticklabels(tick.strftime('%Y-%m-%d' if show_yr else '%m-%d'), **font_dic_norm)


	font_dic_bold.update(fontsize=fs+5)

	fig.tight_layout()

	return fig, out_nam

	# ax.set_title(main_set['title'],pad=title_pad,**font_dic_bold)

	# ax.ticklabel_format(axis='y', scilimits=(-2,4), useMathText=True)
	# ax.yaxis.offsetText.set_fontproperties(dict(size=fs))

	# ax.set(yticks=main_set.get('yticks') or _auto_ticks(*main_set['ylim']) or ax.get_yticks(),
		   # xlim=(st_tm,ed_tm))
	# ax.set_ylabel(main_set['ylabel'], labelpad=main_set.get('ylabel_pad') or 5, **font_dic_bold)



@_template_setting(figsize=(9,8), subplot_kw=dict(polar=True), dirnam='polarPlot', fs=30)
def bivariatePolarPlot(df_wd, df_ws, df_val, main_set, calsfy=None, **kwarg):

	main_set.update(kwarg)
	out_nam = main_set["out_nam"]
	print(f'bivariatePolarPlot : ',end='')

	## parameter
	fig, ax, fs, font_dic_norm, font_dic_bold = kwarg['fig'], kwarg['ax'], kwarg['fs'], kwarg['font_dic_norm'], kwarg['font_dic_bold']
	labels  = ['N','E','S','W']
	theta_w = np.radians(df_wd)

	if calsfy is not None:
		theta_w = theta_w.loc[calsfy].copy()
		df_ws	= df_ws.loc[calsfy].copy()
		df_val  = df_val.loc[calsfy].copy()

	## plot
	box = ax.get_position()
	ax.set_position([box.x0*.35, box.y0*.6, box.width, box.height])
	cax = fig.add_axes([box.x1, box.y0*.6, .03, box.height])

	sca = ax.scatter(theta_w, df_ws, c=df_val, **main_set['sca_set'])

	ax.set(theta_zero_location='N', theta_direction=-1, rlabel_position=45,
		   ylim=main_set['ylim'])

	cbar = fig.colorbar(sca, cax=cax, shrink=1.2)
	cbar.ax.set_title(main_set['bar_title'], pad=20, **font_dic_norm)
	cbar.ax.tick_params(labelsize=fs)
	cbar.ax.ticklabel_format(axis='y', scilimits=(-2,3), useMathText=True)
	cbar.ax.yaxis.offsetText.set_fontproperties(dict(size=fs))

	ax.set_yticks(main_set['yticks'])
	yticklab = main_set['yticks'].astype(str)
	yticklab[-1] = f'{yticklab[-1]} m/s'
	ax.set_yticklabels(yticklab, va='center', ha='left', **font_dic_norm)

	ax.set_thetagrids(range(0,360,90), labels=labels, **font_dic_norm)
	
	ax.tick_params(labelsize=fs+5, pad=10)

	font_dic_bold.update(fontsize=fs+15)
	ax.set_title(main_set['title'], pad=23, **font_dic_bold)

	return fig, out_nam



@_template_setting(figsize=(9,8), dirnam='scatter', fs=28)
def scatter(df_x, df_y, main_set, linregre=True, line_1to1=True, _clasfy=None, **kwarg):

	main_set.update(kwarg)
	out_nam = main_set["out_nam"]
	print(f'scatter : ',end='')

	## parameter
	fig, ax, fs, font_dic_norm, font_dic_bold = kwarg['fig'], kwarg['ax'], kwarg['fs'], kwarg['font_dic_norm'], kwarg['font_dic_bold']
	if _clasfy is not None:
		df_x = df_x.loc[_clasfy].copy()
		df_y = df_y.loc[_clasfy].copy()
		df_val = df_val.loc[_clasfy].copy()
	df_sca = concat([df_x,df_y], axis=1, keys=['x','y'])
	df_x, df_y = df_sca.x, df_sca.y

	box = ax.get_position()
	ax.set_position([box.x0, box.y0*1.2, box.width, box.height])

	## plot
	sca = ax.scatter(df_x, df_y, zorder=3, **main_set['sca_set'])

	ax = _pic_set(ax, 'x', main_set, fs, font_dic_bold)
	ax = _pic_set(ax, 'y', main_set, fs, font_dic_bold)
	
	ax.grid(color='#999999')

	if linregre:
		func, regr_func = _LinRegr(df_x, df_y, _over0=False)

		xmax, ymax = ax.get_xlim()[-1], ax.get_ylim()[-1]
		x_data = n.linspace(0, xmax if xmax>ymax else ymax, 100)

		ln, = ax.plot(x_data, func(x_data), color='#ff4c4d', ls='--', label=regr_func,zorder=3)
		
		ax.legend(handles=[ln], framealpha=0, fontsize=fs-4.)
	
		if line_1to1:
			ax.plot([0,ax.get_ylim()[-1]], [0,ax.get_ylim()[-1]], color='#7f7f7f', zorder=3)

	font_dic_bold.update(fontsize=fs+15.)
	ax.set_title(main_set['title'], pad=15, **font_dic_bold)

	return fig, out_nam

	# ax.set(xlim=main_set['xlim'],ylim=main_set['ylim'])
	# ax.set(xticks=main_set.get('xticks') or _auto_ticks(*main_set['xlim']) or ax.get_xticks(), 
		   # yticks=main_set.get('yticks') or _auto_ticks(*main_set['ylim']) or ax.get_yticks(),
		   # xlim=main_set['xlim'],ylim=main_set['ylim'])

	# ax.set_xlabel(main_set['xlabel'],labelpad=main_set.get('xlabel_pad',0),**font_dic_bold)
	# ax.set_ylabel(main_set['ylabel'],labelpad=main_set.get('ylabel_pad',0),**font_dic_bold)

	# ax.ticklabel_format(axis='y',scilimits=(-2,3),useMathText=True)
	# ax.yaxis.offsetText.set_fontproperties(dict(size=fs))

@_template_setting(figsize=(9.6,8), dirnam='scatterVal', fs=30)
def scatterVal(df_x, df_y, df_val, main_set, df_size=None, size_range=None, linregre=True, line_1to1=True, 
			   _clasfy=None, show_box=False, box_cut=5, box_qcut=None, **kwarg):

	main_set.update(kwarg)
	out_nam = main_set["out_nam"]
	print(f'scatterVal : ',end='')

	## parameter
	fig, ax, fs, font_dic_norm, font_dic_bold = kwarg['fig'], kwarg['ax'], kwarg['fs'], kwarg['font_dic_norm'], kwarg['font_dic_bold']
	if _clasfy is not None:
		df_x = df_x.loc[_clasfy].copy()
		df_y = df_y.loc[_clasfy].copy()
		df_val = df_val.loc[_clasfy].copy()
	df_sca = concat([df_x, df_y, df_val], axis=1, keys=['x', 'y', 'c'])

	## plot
	box = ax.get_position()
	ax.set_position([box.x0, box.y0*1.2, box.width*.9, box.height])
	cax = fig.add_axes([box.x1*.97, box.y0*1.2, .03, box.height])

	if df_size is not None:
		## make sure the max size is the whole number of 5 times
		_coe_a, _coe_b = main_set.get('coe_a') or 3, main_set.get('coe_b') or 6
		size_norm = (df_size.max())

		if size_range is not None:
			_cut = dict(bins=[-n.inf]+size_range+[n.inf], labels=[size_range[0]]+size_range, 
						include_lowest=True, ordered=False)
			df_size = DataFrame(cut(df_size.values.flatten(), **_cut)).astype(float).set_index(df_sca.index)[0]

			size_norm = size_range[-1]
			psudo_size = ( n.array(size_range) / size_norm*_coe_a )**_coe_b

		size = ( df_size.values / size_norm*_coe_a )**_coe_b

	else:
		size = kwarg.get('s') or 20
	df_sca['s'] = size
	df_sca = df_sca.dropna()

	sca = ax.scatter(df_sca.x, df_sca.y, c=df_sca.c.values, s=df_sca.s, zorder=3, **main_set['sca_set'])

	ax = _pic_set(ax, 'x', main_set, fs, font_dic_bold)
	ax = _pic_set(ax, 'y', main_set, fs, font_dic_bold)
	
	cbar = fig.colorbar(sca,cax=cax)
	font_dic_norm.update(fontsize=fs-3)
	cax.set_title(main_set['bar_title'], pad=20, **font_dic_norm)
	cbar.ax.tick_params(labelsize=fs,)

	ax.grid(color='#999999')

	if linregre:
		func, regr_func = _LinRegr(df_x, df_y, _over0=False)

		x_data = n.linspace(0, df_x.max(), 100)
		ln, = ax.plot(x_data, func(x_data), color='#000000', ls='--', label=regr_func, zorder=3)
		
		leg = ax.legend(handles=[ln], framealpha=0, fontsize=fs-4.)
		fig.add_artist(leg)

		if line_1to1:
			ax.plot([0,ax.get_ylim()[-1]], [0,ax.get_ylim()[-1]], color='#7f7f7f', zorder=3)

	if df_size is not None:

		if size_range is not None:
			psu_sca = ax.scatter(df_sca.x.iloc[:psudo_size.size], df_sca.y.iloc[:psudo_size.size],
								 color='#ffffff', s=psudo_size, zorder=1)

			leg_handle, _ = psu_sca.legend_elements('sizes', num=psudo_size.size, 
													func=lambda _: _**(1/_coe_b)/_coe_a*size_norm, fmt='{x:.1f}')
			leg_txt = [f'< {size_range[0]}'] + size_range[1:-1] + [f'> {size_range[-1]}']

			leg = ax.legend(leg_handle, leg_txt, framealpha=0, fontsize=fs-4.,
							title=main_set.get('leg_title', None), title_fontsize=fs-4)

		else:
			ax.legend(*sca.legend_elements('sizes', func=lambda _: _**(1/_coe_b)/_coe_a*size_norm,fmt='{x:.1f}'),
					  framealpha=0, fontsize=fs-4., title=main_set.get('leg_title', None),
					  title_fontsize=fs-4)

	if show_box:

		_props = dict(color='#000000', lw=1)
		_box_props = dict(facecolor='#ff794c', lw=1, alpha=.2)

		_box_x = df_sca.x.where( (df_sca.x>=ax.get_xlim()[0]) & (df_sca.x<=ax.get_xlim()[-1]) )

		cat_cut, bins = cut( _box_x, box_cut, retbins=True )
		if box_qcut is not None:
			cat_cut, bins = qcut( _box_x, box_qcut, retbins=True )

		box_pos = ( bins[:-1] + bins[1:] ) / 2
		box_wid = ( ax.get_xlim()[1] - ax.get_xlim()[0] ) / len(bins) * 1

		df_sca['cut'] = cat_cut
		_box_lst, _mn_lst = [], []
		for _grp, _df in df_sca.loc[_box_x.dropna().index].groupby('cut'):
			_df = _df.y
			_box_lst.append(_df)
			_mn_lst.append(_df.mean())

		box = ax.boxplot(_box_lst, positions=box_pos, sym='', manage_ticks=False, zorder=4,
						 patch_artist=True, showmeans=False, meanline=False, widths=box_wid,
						 boxprops=_box_props, capprops=_props, whiskerprops=_props, medianprops=_props)

		ax.plot(box_pos, _mn_lst, color='#000000', marker='*', zorder=3, ls='none')

	cbar.ax.ticklabel_format(axis='y', scilimits=(-2,3), useMathText=True)
	cbar.ax.yaxis.offsetText.set_fontproperties(dict(size=fs-16.))

	font_dic_bold.update(fontsize=fs+15.)
	ax.set_title(main_set['title'], pad=15, **font_dic_bold)

	return fig, out_nam



@_template_setting(figsize=(9,8), dirnam='scatterMulti', fs=30)
def scatterMulti(df_x_lst, df_y_lst, main_set, linregre=True, linregre_typ='each', line_1to1=True, **kwarg):

	main_set.update(kwarg)
	out_nam = main_set["out_nam"]
	print(f'scatterMulti : ',end='')

	## parameter
	fig, ax, fs, font_dic_norm, font_dic_bold = kwarg['fig'], kwarg['ax'], kwarg['fs'], kwarg['font_dic_norm'], kwarg['font_dic_bold']

	## plot
	box = ax.get_position()
	ax.set_position( [ box.x0*1.4, box.y0*1.375, box.width, box.height ] )
	size = 20

	leg_handle, df_all = [], []
	for _df_x, _df_y, _set in zip(df_x_lst, df_y_lst, main_set['sca_set']):

		_df = concat([_df_x,_df_y], axis=1, keys=['x','y']).dropna()
		_df_x, _df_y = _df.x.copy(), _df.y.copy()

		if ( len(_df_x)==0) | (len(_df_y)==0 ):
			continue

		_handle = ax.scatter(_df_x, _df_y, s=20, zorder=2, **_set)

		if linregre & (linregre_typ=='each'):
			func, regr_func = _LinRegr(_df_x, _df_y, _over0=False)
			_func, _num = regr_func.split('\n')
			regr_func = f"{_set['label']} : {_func} {_num}"
			
			x_data = n.linspace(0, _df_x.max(), 100)
			_handle, = ax.plot(x_data, func(x_data), color=_set['color'], ls='--', label=regr_func, zorder=3)

		df_all.append(_df)
		leg_handle.append(_handle)

	ax = _pic_set(ax, 'x', main_set, fs, font_dic_bold)
	ax = _pic_set(ax, 'y', main_set, fs, font_dic_bold)

	if linregre:
		df_all = concat(df_all)

		func, regr_func = _LinRegr(df_all.x, df_all.y, _over0=False)
		_func, _num = regr_func.split('\n')
		regr_func = f"all : {_func} {_num}"

		x_data = n.linspace(0, df_all.x.max(), 100)
		_handle, = ax.plot(x_data, func(x_data), color='#000000', ls='--', label=regr_func, zorder=4)

		leg_handle.insert(0, _handle)

	if line_1to1:
		ax.plot([0,ax.get_ylim()[-1]], [0,ax.get_ylim()[-1]], color='#7f7f7f', zorder=3)

	leg = ax.legend(handles=leg_handle, framealpha=0, fontsize=fs-13. if linregre else fs-4.)
	fig.add_artist(leg)

	ax.grid(color='#999999')

	font_dic_bold.update(fontsize=fs+15.)
	ax.set_title(main_set['title'], pad=15, **font_dic_bold)

	return fig, out_nam

	# ax.tick_params(axis='x', labelsize=fs, pad=main_set.get('xtick_pad') or 5)
	# ax.tick_params(axis='y', labelsize=fs, pad=main_set.get('ytick_pad') or 5)
	# ax.set(xlim=main_set['xlim'],ylim=main_set['ylim'])
	# ax.set(xticks=main_set.get('xticks') or _auto_ticks(*main_set['xlim']) or ax.get_xticks(), 
		   # yticks=main_set.get('yticks') or _auto_ticks(*main_set['ylim']) or ax.get_yticks(),
		   # xlim=main_set['xlim'],ylim=main_set['ylim'])

	# ax.set_xlabel(main_set['xlabel'],labelpad=main_set.get('xlabel_pad') or 0,**font_dic_bold)
	# ax.set_ylabel(main_set['ylabel'],labelpad=main_set.get('ylabel_pad') or 0,**font_dic_bold)

	# ax.ticklabel_format(axis='x',scilimits=(-2,4),useMathText=True)
	# ax.xaxis.offsetText.set_fontproperties(dict(size=fs))
	# ax.ticklabel_format(axis='y',scilimits=(-2,3),useMathText=True)
	# ax.yaxis.offsetText.set_fontproperties(dict(size=fs))

@_template_setting(figsize=(12,8), dirnam='boxPlot', fs=22)
def boxPlot(df_lst, clasfy_lst, main_set, **kwarg):

	main_set.update(kwarg)
	out_nam = main_set['out_nam']
	print(f'boxPlot : ', end='')

	if len(df_lst) != len(clasfy_lst):
		clasfy_lst *= len(df_lst)

	if len(df_lst) != len(clasfy_lst):
		raise ValueError('Length of Data List Should Be Same as The Length of Classify-Data List !!!')

	## parameter
	fig, ax, fs, font_dic_norm, font_dic_bold = kwarg['fig'], kwarg['ax'], kwarg['fs'], kwarg['font_dic_norm'], kwarg['font_dic_bold']
	clasfy_nam = main_set['clasfy_nam']

	box_pos  = n.arange(0, (len(df_lst)+1)*len(clasfy_nam), len(df_lst)+1)
	tick_pos = box_pos.copy() + (len(df_lst)-1) / 2

	## plot 
	leg_lst = []
	for _dt, _clas_dt, _colr in zip(df_lst, clasfy_lst, main_set['color_list']):
		
		_dt_lst, _mean_lst = [], []
		for _clas_nam in clasfy_nam:
			_dt_box = _dt.loc[_clas_dt[_clas_nam]].dropna().copy()
			_dt_lst.append(_dt_box)
			_mean_lst.append(_dt_box.mean())

		_props = dict(color='#000000', lw=1)
		_box_props = dict(facecolor=_colr, lw=1)
		box = ax.boxplot(_dt_lst, positions=box_pos, sym='',
						 patch_artist=True, showmeans=False, meanline=False, widths=.8,
						 boxprops=_box_props, capprops=_props, whiskerprops=_props, medianprops=_props)
		ax.plot(box_pos, _mean_lst, color='#000000', marker='*', zorder=3, ls='none')

		box_pos += 1
		leg_lst.append(box['boxes'][0])

	ax = _pic_set(ax, 'y', main_set, fs, font_dic_bold)
	ax.tick_params(labelsize=fs, pad=5)

	ax.set_xticks(tick_pos)
	ax.set_xticklabels(main_set['tick_nam'], **font_dic_bold)

	ax.legend(handles=leg_lst, labels=main_set['leg_nam'], framealpha=0, fontsize=fs-5.)

	font_dic_bold.update(fontsize=fs+5.)
	ax.set_title(main_set['title'], pad=15, **font_dic_bold)

	return fig, out_nam

	# ax.set(ylim=main_set['ylim'])
	# ax.set(xticks=tick_pos,xlim=(-1,box_pos[-1]),
		   # yticks=main_set.get('yticks') or _auto_ticks(*main_set['ylim']) or ax.get_yticks(),
		   # ylim=main_set['ylim'])
	# ax.ticklabel_format(axis='y',scilimits=(-2,4),useMathText=True)
	# ax.yaxis.offsetText.set_fontproperties(dict(size=fs))
	# ax.set_ylabel(main_set['ylabel'],**font_dic_bold)



@_template_setting(figsize=(10,10), dirnam='piePlot', fs=20)
def piePlot(*dt_lst, main_set, br_per=None, show_legend=True, show_txt=True, show_info=True, pie_type='origin', 
			info_loc=(.5,.5), **kwarg):
	"""
	plot Pie plot

	Parameters
	----------
	*dt_lst : Series or DataFrame objects
		If multiple data input, the order of the circles will be set from outer to inner.
	main_set : dictionary
		Plot setting, control by 'config.py', 'kwarg' will replace the argument of 'main_set'.
	br_per : int, default None
		Gradient ratio of the color, from outer to inner.
	show_legend : bool, default True
		Show legend at the upper right.
	show_txt : bool, default True
		Show percentage on the circle.
	show_info : bool, default True
		Show mean value at the loc of 'info_loc'.
	pie_type : str, default 'origin'
		'origin' : Set the pie chart as filled circle, if size of 'dt_lst' >1, will only plot the first data
		'donut' : Set the pie chart as donut circle.
	info_loc : tuple, default (0.5, 0.5)
		Infomation text location.
	"""

	main_set.update(kwarg)
	out_nam = main_set["out_nam"]
	print(f'piePlot : ',end='')

	## parameter
	fig, ax, fs, font_dic_norm, font_dic_bold = kwarg['fig'], kwarg['ax'], kwarg['fs'], kwarg['font_dic_norm'], kwarg['font_dic_bold']

	width, outer_r, pie_pad, pctdis = .2, 1.2, .0, .01
	color, nam = main_set['color'], main_set.get('text_nam')

	if pie_type=='donut':
		txt_lst = []
		for _idx, _df in enumerate(dt_lst):

			_df = _df.dropna().copy()
			ax.pie(_df.mean().values, explode=None, labels=None, labeldistance=None, colors=color,
				   autopct='%1.1f%%' if show_txt else None, shadow=False, textprops=font_dic_bold,
				   radius=outer_r-(width+pie_pad)*_idx, pctdistance=0.9-pctdis*_idx,
				   startangle=0, wedgeprops=dict(width=width, edgecolor='k'))

			_df_all = _df.sum(axis=1).copy()
			txt_lst.append(fr'{nam[_idx]} : {_df_all.mean():.2f} $\pm$ {_df_all.std():.2f}')

			color = _bright_color(color, br_per)

		if show_info:
			fig.text(*info_loc, main_set['text_title']+'\n\n'+'\n'.join(txt_lst), va='center', ha='center', **font_dic_bold)

	elif pie_type=='origin':
		_df = dt_lst[0].dropna().copy()

		ax.pie(_df.mean().values, explode=None, labels=None, labeldistance=None, colors=color,
			   autopct='%1.1f%%' if show_txt else None, shadow=False, textprops=font_dic_bold,
			   startangle=0, wedgeprops=dict(edgecolor='k'))

	if show_legend:
		legend = ax.legend(main_set['leg_nam'], framealpha=0, fontsize=fs, title_fontsize=fs, bbox_to_anchor=[.9,.8], loc=3,
						   title=main_set['leg_title'])

	font_dic_bold.update(fontsize=fs+5.)
	ax.set_title(main_set['title'], pad=8, **font_dic_bold)

	return fig, out_nam




@_template_setting(figsize=(8,6), dirnam='linePlot', fs=17)
def linePlot(*df_lst, main_set, shade_lst=None, x_lst=None, y_lst=None, twin=None, vlines=False, hlines=False, **kwarg):

	main_set.update(kwarg)
	out_nam = main_set["out_nam"]
	print(f'linePlot : ',end='')

	## parameter
	fig, ax, fs, font_dic_norm, font_dic_bold = kwarg['fig'], kwarg['ax'], kwarg['fs'], kwarg['font_dic_norm'], kwarg['font_dic_bold']

	if x_lst is not None:
		df_lst = []
		for _x, _y in zip(x_lst, y_lst):
			df_lst.append(DataFrame(_y, index=_x))
	
	## plot
	ln_lst = []
	if shade_lst is not None:

		for _df, _set, _shade in zip(df_lst, main_set['line_set'], shade_lst):
			ln, = ax.plot(_df, **_set)
			ln_lst.append(ln)

			fill = ax.fill_between(_df.index, _df+_shade, _df-_shade, alpha=.2, **_set)
			fill.set_lw(0)
	else:
		for _df, _set in zip(df_lst, main_set['line_set']):
			ln,  = ax.plot(_df, **_set)
			ln_lst.append(ln)

	ax.tick_params(labelsize=fs, pad=main_set.get('tick_pad',5))
	ax.set(xlim=main_set['xlim'], ylim=main_set['ylim'], 
		   xscale=main_set.get('xscale','linear'), yscale=main_set.get('yscale','linear'))

	if vlines:
		ax.vlines(vlines, *ax.get_ylim(), color='#444444', ls='--')
	if hlines:
		ax.hlines(hlines, *ax.get_xlim(), color='#444444', ls='--')

	ax.set_xlabel(main_set['xlabel'], labelpad=main_set.get('xlabel_pad') or 0,**font_dic_bold)
	ax.set_ylabel(main_set['ylabel'], labelpad=main_set.get('ylabel_pad') or 0,**font_dic_bold)

	if main_set.get('xscale') != 'log':
		ax.set(xticks=main_set.get('xticks') or _auto_ticks(*main_set['xlim']) or ax.get_xticks(), ylim=main_set['ylim'])
		ax.ticklabel_format(axis='x', scilimits=(-2,3), useMathText=True)
		ax.xaxis.offsetText.set_fontproperties(dict(size=fs))

	if main_set.get('yscale') != 'log':
		ax.set(yticks=main_set.get('yticks') or _auto_ticks(*main_set['ylim']) or ax.get_yticks(), xlim=main_set['xlim'])

		ax.ticklabel_format(axis='y', scilimits=(-2,3), useMathText=True)
		ax.yaxis.offsetText.set_fontproperties(dict(size=fs))

	ax.legend(handles=ln_lst, framealpha=0, fontsize=fs-2., title=main_set.get('leg_title'), title_fontsize=fs-2)

	font_dic_bold.update(fontsize=fs+5.)
	ax.set_title(main_set['title'], pad=8, **font_dic_bold)

	return fig, out_nam


@_template_setting(figsize=(10,8), dirnam='classify_bar', fs=25)
def clasfyBar(bar_lst, main_set, clasfy_lst=None, to_ratio=False, show_legend=True, twin=None, twin_set=None, **kwarg):

	main_set.update(kwarg)
	out_nam = main_set["out_nam"]
	print(f'clasfyBar : ',end='')

	## parameter
	fig, ax, fs, font_dic_norm, font_dic_bold = kwarg['fig'], kwarg['ax'], kwarg['fs'], kwarg['font_dic_norm'], kwarg['font_dic_bold']

	clasfy_nam = main_set['clasfy_nam']
	leg_nam = main_set['leg_nam']

	if twin is not None:
		bar_pos = n.arange(0, (len(leg_nam)+2)*len(clasfy_nam), len(leg_nam)+2)
	else:
		bar_pos = n.arange(0, (len(leg_nam)+1)*len(clasfy_nam), len(leg_nam)+1)
	tick_pos = bar_pos.copy() + (len(leg_nam)-1)/2

	clasfy_lst = clasfy_lst[0]

	## classify 
	mean_lst, std_lst = [], []
	if clasfy_lst is not None:
		df = concat(bar_lst, axis=1)
		drop_idx = concat([df,twin], axis=1).dropna().index
		df = df.loc[drop_idx].reindex(df.index)

		for _key, _dt in df.items():
			_mean_lst, _std_lst = [], []
			for _clas_nam in clasfy_nam:
				_dt_bar = _dt.loc[clasfy_lst[_clas_nam]].copy()
				_mean_lst.append(_dt_bar.mean())
				_std_lst.append(_dt_bar.std())

			mean_lst.append(_mean_lst)
			std_lst.append(_std_lst)
	else:
		mean_lst, std_lst = bar_lst[0], bar_lst[1]

	mean_dt = n.array(mean_lst)
	std_dt  = n.array(std_lst)

	if to_ratio:
		mean_dt /= mean_dt.sum(axis=0)
		std_dt  -= std_dt

		main_set.update(ylim=(0,.6), yticks=[0,.2,.4,.6], ylabel='Ratio')
		main_set['title'] += ' Ratio'
		out_nam += '-ratio'
	main_set.update(kwarg)

	## plot
	leg_lst = []
	for _mean, _std, _colr, _nam in zip(mean_dt, std_dt, main_set['color_list'], main_set['leg_nam']):

		bar = ax.bar(bar_pos, _mean, width=1, yerr=[_std,_std], color=_colr, ecolor=_colr, 
						 capsize=0 if to_ratio else 6, label=_nam)
		bar_pos += 1
		leg_lst.append(bar)

	ax.set(ylim=main_set['ylim'])
	ax.set(xticks=tick_pos, xlim=(-1,bar_pos[-1]),
		   yticks=main_set.get('yticks') or _auto_ticks(*main_set['ylim']) or ax.get_yticks(),
		   ylim=main_set['ylim'],)

	ax.tick_params(labelsize=fs, pad=5)
	ax.ticklabel_format(axis='y', scilimits=(-2,4), useMathText=True)
	ax.yaxis.offsetText.set_fontproperties(dict(size=fs))

	ax.set_xticklabels(main_set['tick_nam'], **font_dic_norm)

	ax.set_xlabel(main_set.get('xlabel'), labelpad=main_set.get('xlabelpad') or 5, **font_dic_bold)
	ax.set_ylabel(main_set['ylabel'], labelpad=main_set.get('ylabel_pad') or 5, **font_dic_bold)
	
	font_dic_bold.update(fontsize=fs+5.)
	ax.set_title(main_set['title'], pad=15, **font_dic_bold)

	if twin is not None:
		ax_t = ax.twinx()

		_mean_lst, _std_lst = [], []
		if clasfy_lst is not None:

			twin = twin.loc[drop_idx].reindex(df.index)

			for _clas_nam in clasfy_nam:
				_dt = twin.loc[clasfy_lst[_clas_nam]].copy()
				_mean_lst.append(_dt.mean())
				_std_lst.append(_dt.std())
		else:
			_mean_lst, _std_lst = twin[0], twin[1]

		errln = ax_t.errorbar(bar_pos, _mean_lst, yerr=_std_lst, color='#000000',
							  capsize=6, marker='o', ms=12, ls='none', label=twin_set['set_nam'])
		ax_t.tick_params(labelsize=fs,)

		ax_t.set(ylim=twin_set.get('lim') or (0,None))
		ax_t.set(yticks=twin_set.get('ticks') or _auto_ticks(*ax_t.get_ylim()) or ax_t.get_yticks())

		ax_t.set_ylabel(twin_set.get('label'), rotation=-90, labelpad=twin_set.get('twin_label_pad') or 25, **font_dic_bold)

		leg_lst.append(errln)
		bar_pos += 1

	if show_legend:
		ax.legend(handles=leg_lst, framealpha=0, fontsize=fs-5.)

	ax.set(xlim=(-1, bar_pos[-1]))

	return fig, out_nam



"""


@_template_setting(figsize=_cm2inch(33.87,8.47), dirnam='timeSeries', fs=22)
def classTmSeries(st_tm,ed_tm,_df_val,_class,main_set,split_date=None,twin_val=None,twin_set=None,
				  print_date=False,show_xtick=True,**kwarg):

	main_set.update(kwarg)
	out_nam = main_set["out_nam"]
	print(f'classTmSeries : {out_nam}')

	## parameter
	fig, ax, fs, font_dic_norm, font_dic_bold = kwarg['fig'], kwarg['ax'], kwarg['fs'], kwarg['font_dic_norm'], kwarg['font_dic_bold']
	index = _df_val.index
	tick = date_range(st_tm,ed_tm,freq=main_set['tick_freq'])
	minor_tick = date_range(st_tm,ed_tm,freq=main_set['minor_tick_freq'])
	title_pad = 15

	## plot
	ln_lst = []
	for _clas, _colr in zip(main_set['class_nam'],main_set['color']):
		ln, = ax.plot(_df_val.loc[_class[_clas]].reindex(index),c=_colr,label=_clas,zorder=3)
		ln_lst.append(ln)

	ax.tick_params(labelsize=fs,pad=15,labelbottom=False)
	ax.tick_params(axis='x',length=6,width=1.5)
	ax.set(yticks=main_set.get('yticks',ax.get_yticks()),xlim=(st_tm,ed_tm),ylim=main_set['ylim'],)

	ax.set_ylabel(main_set['ylabel'],**font_dic_bold)

	if split_date is not None: 
		ax.vlines(split_date,*ax.get_ylim(),color='#000000',ls='-',lw=2,zorder=4)

		if print_date:
			ax.text(split_date,ax.get_ylim()[-1],split_date.strftime('%Y-%m-%d'),ha='center',va='bottom',**font_dic_bold)
			title_pad = 35

	if twin_set is not None:
		_twin = twin_set
		print(f'\ttwin : {_twin["out_nam"]}')

		axt = ax.twinx()
		ln2, = axt.plot(twin_val,**_twin['plot_set'])

		axt.tick_params(labelsize=fs,labelright=False,right=False,pad=15)

		_ytick_twin = _twin.get('ytick_twin',None)
		if _ytick_twin is not False:
			axt.tick_params(labelright=True,right=True)
			axt.set_yticks(_ytick_twin or axt.get_yticks())

		axt.set_ylabel(_twin['ylabel'],rotation=-90,labelpad=10,**font_dic_bold)
		axt.set(ylim=_twin['ylim'])

		ln_lst.append(ln2)

		if _twin['out_nam'] is not None:
			out_nam += f"_{_twin['out_nam']}"

	ax.set_xticks(tick)
	ax.set_xticks(minor_tick,minor=True)
	if show_xtick:
		ax.tick_params(labelbottom=True)
		ax.set_xticklabels(tick.strftime('%Y-%m-%d'),**font_dic_norm)

	_leg = main_set.get('legend',True)
	if _leg: ax.legend(handles=ln_lst,framealpha=0,fontsize=fs-2.,ncol=3)
	
	# font_dic_bold.update(fontsize=fs+5)
	# ax.set_title(main_set['title'],pad=title_pad,**font_dic_bold)

	fig.tight_layout()

	return fig, out_nam

def scatterClasVal(*arg, clsfy=None, clsfy_nam=None, **kwarg,):
	
	fig_dir_nam = kwarg.get('dir_nam','.')
	for _nam in clsfy_nam:
		scatterVal(dirnam=Path('scatterVal')/fig_dir_nam/_nam,_clasfy=clsfy[_nam],*arg,**kwarg)
		print(f'\tclassify : {_nam}')


@_template_setting(figsize=(10,8), dirnam='diurnal_cycle', fs=22)
def diuPlot(df_dic,main_set,**kwarg):


	
# ((trans((self.size,1))-trans((0,0))) *ppd)




	pass





@_template_setting(figsize=(33.87/2.54,8.47/2.54),dirnam='quiverSeries',fs=22)
def quiverSeries(st_tm,ed_tm,_df_val,main_set,twin_val=None,twin_set=None,split_date=None,
				 print_date=False,show_xtick=True,**kwarg):

	out_nam = main_set["out_nam"]
	print(f'tmSeries : {out_nam}')

	## parameter
	fig, ax, fs, font_dic_norm, font_dic_bold = kwarg['fig'], kwarg['ax'], kwarg['fs'], kwarg['font_dic_norm'], kwarg['font_dic_bold']
	tick = date_range(st_tm,ed_tm,freq=main_set['tick_freq'])
	minor_tick = date_range(st_tm,ed_tm,freq='1d')
	title_pad = 15

	## plot
	ln1, = ax.plot(_df_val,**main_set['plot_set'])

	ax.tick_params(labelsize=fs,pad=15,labelbottom=False)
	ax.tick_params(axis='x',length=6,width=1.5)
	ax.set(yticks=main_set.get('yticks') or ax.get_yticks(),xlim=(st_tm,ed_tm),ylim=main_set['ylim'])

	ax.set_ylabel(main_set['ylabel'],**font_dic_bold)

	if split_date is not None: 
		ax.vlines(split_date,*ax.get_ylim(),color='#000000',ls='-',lw=2)

		if print_date:
			ax.text(split_date,ax.get_ylim()[-1],split_date.strftime('%Y-%m-%d'),ha='center',va='bottom',**font_dic_bold)
			title_pad = 35

	if twin_set is not None:
		_twin = twin_set
		print(f'\ttwin : {_twin["out_nam"]}')

		axt = ax.twinx()
		ln2, = axt.plot(twin_val,**_twin['plot_set'])

		axt.tick_params(labelsize=fs,labelright=False,pad=15)

		_ytick_twin = _twin.get('yticks',None)
		if _ytick_twin is not False:
			axt.tick_params(labelright=True)
			axt.set_yticks(_ytick_twin or axt.get_yticks())

		_twin_labelpad = _twin.get('labelpad',15)
		axt.set_ylabel(_twin['ylabel'],rotation=-90,labelpad=_twin_labelpad,**font_dic_bold)

		axt.set(ylim=_twin['ylim'])

		_leg = _twin.get('legend',True)
		if _leg: ax.legend(handles=[ln1,ln2],framealpha=0,fontsize=fs-2.)

		if _twin['out_nam'] is not None:
			out_nam += f"-{_twin['out_nam']}"

	ax.set_xticks(tick)
	ax.set_xticks(minor_tick,minor=True)
	if show_xtick:
		ax.tick_params(labelbottom=True)
		ax.set_xticklabels(tick.strftime('%Y-%m-%d'),**font_dic_norm)

	ax.ticklabel_format(axis='y',scilimits=(-2,3),useMathText=True)
	ax.yaxis.offsetText.set_fontproperties(dict(size=fs))

	font_dic_bold.update(fontsize=fs+5)
	# ax.set_title(main_set['title'],pad=title_pad,**font_dic_bold)

	fig.tight_layout()

	return fig, out_nam



































# """