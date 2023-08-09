
from PlotTemplate.utils.setting import basic_setting, clasfy_setting
import numpy as n
np = n

# get setting
class setting_parser:

	def __init__(self, clasfy_nam=None, update_file=None):

		if update_file is not None:
			from importlib import import_module
			_setting = import_module( str(update_file) )

			basic_setting.update( getattr(_setting, 'basic_setting', {}) )
			clasfy_setting.update( getattr(_setting, 'clasfy_setting', {}) )


		self.cla_set = basic_setting

		self.cla_bsc = dict()
		if clasfy_nam is not None:
			self.cla_bsc = clasfy_setting[clasfy_nam].pop('basic')
			self.cla_set.update(clasfy_setting[clasfy_nam])

		self.out_nam = f"{'-' + self.cla_bsc.get('nam') or ''}"


	def get_config(self, set_nam):
		all_set = self.cla_set[set_nam]
		all_set['set_nam'] = set_nam
		return all_set


	def set_tmSer(self, set_nam, tick_freq='10d', minor_tick_freq='1d', twin=False):

		all_set = {}
		bsc_set = self.cla_set[set_nam]

		axis = 'twin_y' if twin else 'y'
		for _ynam in ['lim', 'label', 'label_twin', 'ticks', 'label_pad', 'label_pad_twin']:
			all_set[f'{axis}{_ynam}'] = bsc_set.get(_ynam)

		if twin:
			all_set['twin_plot_set'] = bsc_set['plot_set']
			all_set['out_nam'] = f"{set_nam}{self.out_nam}"
		else:
			all_set['plot_set'] = bsc_set['plot_set']
			all_set['out_nam'] = f"tmser-{set_nam}{self.out_nam}"

		all_set['tick_freq'] = tick_freq
		all_set['minor_tick_freq'] = minor_tick_freq


		return all_set

	def set_bivPol(self, set_nam, ticks=n.arange(0,6,1), lim=(0,5)):

		all_set = {}
		bsc_set = self.cla_set[set_nam]

		for _nam in ['bar_title', 'sca_set']:
			all_set[_nam] = bsc_set[_nam]

		all_set['title'] = self.cla_bsc.get('title')
		all_set['yticks'] = ticks
		all_set['ylim'] = lim
		
		all_set['out_nam'] = f"bivpol-{set_nam}{self.out_nam}"

		return all_set

	def set_scaVal(self, set_nam,):

		all_set = {}
		nam_lst = set_nam.split('-')
		x_set, y_set, val_set = self.cla_set[nam_lst[0]], self.cla_set[nam_lst[1]], self.cla_set[nam_lst[2]]

		for _nam in ['label', 'ticks', 'lim', 'ticks', 'label_pad', 'tick_pad']:
			all_set[f'x{_nam}'] = x_set.get(_nam)
			all_set[f'y{_nam}'] = y_set.get(_nam)

		for _nam in ['bar_title', 'sca_set']:
			all_set[_nam] = val_set.get(_nam)

		if len(nam_lst)==4:
			all_set['leg_title'] = self.cla_set[nam_lst[3]].get('leg_title')

		all_set['title'] = self.cla_bsc.get('title')
		
		all_set['out_nam'] = f"scaval-{set_nam}{self.out_nam}"

		return all_set

	def set_scaMul(self, set_nam,):	

		all_set = {}
		nam_lst = set_nam.split('-')
		x_set, y_set, clasfy_set = self.cla_set[nam_lst[0]], self.cla_set[nam_lst[1]], self.cla_set[nam_lst[2]]

		for _nam in ['label', 'ticks', 'lim', 'ticks', 'label_pad', 'tick_pad']:
			all_set[f'x{_nam}'] = x_set.get(_nam)
			all_set[f'y{_nam}'] = y_set.get(_nam)

		all_set.update(clasfy_set)

		all_set['title'] = self.cla_bsc.get('title')
		
		all_set['out_nam'] = f"scamul-{set_nam}{self.out_nam}"

		return all_set

	def set_sca(self, set_nam):

		all_set = {}
		nam_lst = set_nam.split('-')
		x_set, y_set = self.cla_set[nam_lst[0]], self.cla_set[nam_lst[1]]

		for _nam in ['label', 'ticks', 'lim', 'ticks', 'label_pad']:
			all_set[f'x{_nam}'] = x_set.get(_nam)
			all_set[f'y{_nam}'] = y_set.get(_nam)

		all_set['sca_set'] = dict(color='#000000')


		all_set['title'] = self.cla_bsc.get('title')
		all_set['out_nam'] = f"sca-{set_nam}{self.out_nam}"

		return all_set

	def set_pie(self, set_nam,):

		all_set = {}
		_type, _classfy = set_nam.split('-')

		all_set.update(self.cla_set[_type])
		all_set.update(self.cla_set.get(_classfy) or {})
		
		all_set['out_nam'] = f"pie-{set_nam}{self.out_nam}"
		all_set['title'] = self.cla_bsc.get('title')

		return all_set

	def set_box(self, set_nam, use_var_set=True):

		all_set = {}
		_comp, _type, _classfy = set_nam.split('-')
		_comp_set = self.cla_set[_comp]

		for _nam in ['label', 'ticks', 'lim', 'ticks', 'label_pad']:
			all_set[f'y{_nam}'] = _comp_set.get(_nam)

		if use_var_set:
			_type_set = _comp_set.get('box_set') or self.cla_set[_type]
		else:
			_type_set = self.cla_set[_type]

		all_set.update(_type_set)
		all_set.update(self.cla_set[_classfy])
		
		all_set['out_nam'] = f"box-{set_nam}{self.out_nam}"
		all_set['title'] = (_comp_set.get('title') or '')

		return all_set

	def set_clasfybar(self, set_nam, use_var_set=True):

		all_set = {}
		_comp, _type, _classfy = set_nam.split('-')
		_comp_set = self.cla_set[_comp]

		for _nam in ['label', 'ticks', 'lim', 'ticks', 'label_pad']:
			all_set[f'y{_nam}'] = _comp_set.get(_nam)

		if use_var_set:
			_type_set = _comp_set.get('bar_set') or self.cla_set[_type]
		else:
			_type_set = self.cla_set[_type]

		all_set.update(_type_set)
		all_set.update(self.cla_set[_classfy])
		
		all_set['out_nam'] = f"clasfybar-{set_nam}{self.out_nam}"
		all_set['title'] = (_comp_set.get('title') or '')

		return all_set

	def set_line(self, set_nam,):

		all_set = {}
		_type, _classfy = set_nam.split('-')

		all_set.update(self.cla_set[_type])
		all_set.update(self.cla_set[_classfy])

		all_set['title'] = self.cla_bsc.get('title')
		all_set['out_nam'] = f"lnplot-{set_nam}{self.out_nam}"
		
		return all_set

	def set_stack(self, set_nam,):

		all_set = {}
		_type, _classfy = set_nam.split('-')

		all_set.update(self.cla_set[_type])
		all_set.update(self.cla_set[_classfy])

		all_set['title'] = self.cla_bsc.get('title')
		all_set['out_nam'] = f"stkplot-{set_nam}{self.out_nam}"
		
		return all_set

	def set_diu(self, set_nam,):

		all_set = {}
		_type, _classfy = set_nam.split('-')

		all_set.update(self.cla_set[_type])
		all_set.update(self.cla_set[_classfy])

		all_set['title'] = self.cla_bsc.get('title')
		all_set['out_nam'] = f"diuplot-{set_nam}{self.out_nam}"
		
		return all_set





