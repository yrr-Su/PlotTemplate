
import functools
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb, to_hex, LinearSegmentedColormap
from matplotlib.pyplot import subplots, close, show, rcParams
from scipy.optimize import curve_fit
import numpy as n
from pathlib import Path
from pandas import concat, DataFrame
import bdb



__all__ = [
			'_template_setting',
			'_LinRegr',
			'_bright_color',
			'_cm2inch',
			'_auto_ticks',
			'_pic_set',
			'_manual_cmap',
			'_coerce_dtype2np',

			'iniParams',

	]

## setting
class iniParams:
	
	pathPicOut = Path('picture')
	showPic	   = True

## inner function

def _template_setting(**_setting):
	def _decorator(plot_func):

		@functools.wraps(plot_func)
		def _wrap(*arg, **kwarg):

			## figure setting
			_sub_dir	 = kwarg.get('sub_dir') or Path('.')
			_figsize	 = kwarg.get('figsize') or _setting['figsize']
			_dirnam		 = kwarg.get('dirnam')  or _setting['dirnam']
			_apnd_nam	 = kwarg.get('nam', False)
			_fs			 = kwarg.setdefault('fs', _setting['fs'])
			_subplot_kw	 = _setting.get('subplot_kw')

			## parameter
			_font_fam = 'Times New Roman'
			rcParams['font.sans-serif']	 = _font_fam
			rcParams['mathtext.fontset'] = 'custom'
			_font_dic_norm = dict(fontsize=_fs, math_fontfamily='custom')
			_font_dic_bold = dict(fontsize=_fs, math_fontfamily='custom', fontweight='bold')

			## figure
			_fig, _ax = subplots(figsize=_figsize, subplot_kw=_subplot_kw, dpi=200.)

			## plot function
			_fail = False
			try:
				_fig, _out_nam = plot_func(*arg, fig=_fig, ax=_ax, font_dic_norm=_font_dic_norm, font_dic_bold=_font_dic_bold,
										   **kwarg)
			except Exception as err:
				if type(err) == bdb.BdbQuit: raise
				_out_nam = kwarg['main_set']['out_nam']
				_fail = err

			if _apnd_nam:
				_out_nam += f'-{_apnd_nam}'

			if _fail:
				print(_out_nam + ' - fail')
				print(f'\t{_fail}')

				return _wrap

			print(_out_nam)

			if iniParams.showPic: show()

			## savefig and create figure dir
			_path_out = iniParams.pathPicOut / _dirnam / _sub_dir
			_path_out.mkdir(exist_ok=True, parents=True)
			_fig.savefig(_path_out / _out_nam)
			close()
			
		return _wrap
	return _decorator


def _LinRegr(_dt_x, _dt_y, _over0=False):
	
	_df = DataFrame([_dt_x.values.flatten(), _dt_y.values.flatten()]).T.dropna()
	_df_x, _df_y = _df[0], _df[1]

	def R_sq(_fc, _opt, _x, _y):
		_tss = n.sum((_y - _y.mean())**2.)  ## total sum of square
		_rss = n.sum((_y - _fc(_x, *_opt))**2.) ## residual sum of square
		return 1. - _rss / _tss

	## regression
	if _over0:
		func = lambda _x, _sl : _sl * _x  
	else:
		func = lambda _x, _sl, _inte : _sl*_x+_inte

	popt, pcov = curve_fit(func,_df_x,_df_y)
	rsq = R_sq(func,popt,_df_x,_df_y)

	if (n.log10(popt[0])<-2)|(n.log10(popt[0])>5):
		slope = f'{popt[0]:.1e}'
	else:
		slope = f'{popt[0]:.1f}'

	if _over0:
		text = fr'y = {slope}x, $\rm R^2$ = {rsq:.2f}'+f'\n(n = {_df_x.size})'
	else:
		text = fr'y = {slope}x {popt[1]:+.1f}, $\rm R^2$ = {rsq:.2f}'+f'\n(n = {_df_x.size})'
	
	return lambda _x: func(_x,*popt), text

def _bright_color(color_lst, br_per=None):

	br_per = br_per or 15

	hsv = rgb_to_hsv(list(map(lambda _: [ int(_.strip('#')[_i:_i+2],16)/256 for _i in range(0,6,2)  ],color_lst)))

	hsv_bright = hsv.copy()
	hsv_bright[:,2] = hsv_bright[:,2]*(1+br_per/100)
	hsv_bright[:,1] = hsv_bright[:,1]*(1-br_per/100)
	hsv_bright[hsv_bright>1] = 1.

	return list(map(to_hex,hsv_to_rgb(hsv_bright)))

def _cm2inch(*cm_val):
	return [ _cm/2.54 for _cm in cm_val ]

def _auto_ticks(_hd, _tail):
	if (_hd is not None) & (_tail is not None):

		_tk_intvl, _diff = [3, 4, 5, 2], _tail - _hd
		_diff_sci = 1
		if _diff.as_integer_ratio()[-1] != 1:

			_diff = round(_diff, 2)
			_diff_sci = 10**len(str(_diff).split('.')[-1])
			_diff = int(_diff * _diff_sci)

		for _num in _tk_intvl:
			if (_diff % _num) != 0: continue

			_intvl = (_diff // _num) / _diff_sci
			if ((_intvl % 5) != 0 ) & (_diff > 100): continue

			_ticks = (n.arange(_hd, _tail + _intvl, _intvl))

			if _diff_sci > 1:
				return _ticks.round(1).tolist()

			return _ticks.astype('float64').round(1).tolist()
	return None

def _pic_set(_ax, _axis, _set, _fs, _f_set):

	_ax.tick_params(axis=_axis, labelsize=_fs, pad=_set.get(f'{_axis}tick_pad') or 5)
	_ax.set(**{f'{_axis}lim' : _set[f'{_axis}lim']},
		 	**{f'{_axis}scale' : _set.get(f'{_axis}scale') or 'linear'},)

	if _axis=='x':
		_ax.set(xticks=_set.get('xticks') or _auto_ticks(*_set['xlim']) or _ax.get_xticks(), 
			    xlim=_set['xlim'])

		_ax.set_xlabel(_set['xlabel'], labelpad=_set.get('xlabel_pad') or 0, **_f_set)

		if _set.get('xscale') != 'log':
			if _set.get('xticklabels') is not None:
				_ax.set_xticklabels(
					_set['xticklabels'],
					rotation=_set.get('xtick_rot') or 0
					)
			else:
				_ax.ticklabel_format(
					axis='x',
					scilimits=(-2, 4),
					useMathText=True
					)

		_ax.xaxis.offsetText.set_fontproperties(dict(size=_fs))

	elif _axis=='y':
		_ax.set(yticks=_set.get('yticks') or _auto_ticks(*_set['ylim']) or _ax.get_yticks(), 
			    ylim=_set['ylim'])

		_ax.set_ylabel(_set['ylabel'], labelpad=_set.get('ylabel_pad') or 0, **_f_set)

		if _set.get('yscale') != 'log':
			_ax.ticklabel_format(axis='y', scilimits=(-1, 2), useMathText=True)
		_ax.yaxis.offsetText.set_fontproperties(dict(size=_fs))

	return _ax


def _manual_cmap(*colr, number=256, reverse=False): #

	"""
	create manual color map (cmap)

	Parameters
	----------
	*colr : str
		Combine colors to create a cmap.
	number : int, default 256
		Number of colors in cmap.
	reverse : bool, default False
		Reverse the order of cmap.
	"""

	## fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)

	## parameter
	if reverse:
		colr = colr[::-1]

	_fade_coe = n.linspace( 0, 1, number//(len(colr)-1)+1 )[:-1].reshape(-1,1)
	_colr_lst = n.array( list( map( lambda _: [ int(_.strip('#')[_i:_i+2],16)/256 for _i in range(0,6,2) ], colr ) ) )

	## a*coe + b*(1-coe) -> a + (b-a)*coe
	_fade_colr = []
	for _fs_colr, _diff in zip( _colr_lst[:-1], n.diff(_colr_lst, axis=0) ):
		_fade_colr.append( (_fs_colr + _diff * _fade_coe) )

	_fade_colr_lst = list( map( to_hex, n.vstack(_fade_colr) ) ) + [ colr[-1] ]
	_cmap = LinearSegmentedColormap.from_list('', _fade_colr_lst)

	return _cmap



def _coerce_dtype2np(*_par_lst):

	_out = []
	for _par in _par_lst:

		if type(_par) is not n.ndarray:
			_out.append(n.array(_par))
		else:
			_out.append(_par)

	return _out


