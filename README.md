# PlotTemplate

PlotTemplate 是一個基於 Matplotlib 的 Python 專案，旨在簡化標準化圖表的製作，例如時間序列圖 (Time Series)、散佈圖 (Scatter Plot) 和極座標圖 (Polar Plot)。透過配置檔案和模板化的函數，使用者可以快速生成風格一致的圖片。

## 專案結構

```
PlotTemplate/
├── PlotTemplate/           # 核心套件目錄
│   ├── config.py           # 設定檔解析與管理 (setting_parser)
│   ├── templatePlot.py     # 主要繪圖函數 (tmSeries, scatter, bivariatePolarPlot 等)
│   ├── core/               # 核心功能與裝飾器
│   │   └── func.py
│   └── utils/              # 工具與預設設定
│       └── setting.py
├── example_setting_file.py # 使用者自定義設定範例
└── _example_setting_file.py
```

##依賴套件 (Requirements)

本專案依賴以下 Python 套件：
- matplotlib
- pandas
- numpy
- scipy

## 特點

- **標準化繪圖**：提供統一的裝飾器 (`@_template_setting`) 處理圖表大小、字體、存檔路徑等通用設定。
- **設定與資料分離**：透過 dictionary 進行參數設定，使繪圖邏輯與樣式設定分離。
- **支援多種圖片**：
  - `tmSeries`: 時間序列圖，支援雙 Y 軸 (Twin Axis)。
  - `scatter`: 散佈圖，支援線性回歸 (`linregre`) 與 1:1 線。
  - `scatterVal`: 數值散佈圖，依據第三維度數值上色，支援資料點大小變化與疊圖 BoxPlot。
  - `scatterMulti`: 多組數據散佈圖。
  - `bivariatePolarPlot`: 雙變數極座標圖 (例如風速風向圖)。
  - `pcoPlot`: Pcolormesh，用於繪製熱圖 (Heatmap)。
  - `boxPlot`: 箱型圖 (Box Plot)，支援分組顯示。
  - `piePlot`: 圓餅圖，支援甜甜圈圖模式 (Donut)。
  - `linePlot`: 一般線圖，支援陰影區間 (Shade)。
  - `stackPlot`: 堆疊圖 (Stacked Plot)。
  - `diuPlot`: 日變化圖 (Diurnal Cycle)，顯示平均值與標準差範圍。
  - `clasfyBar`: 分類長條圖 (Classified Bar Plot)，支援分組或單一長條。
  - `classTmSeries`: 分類時間序列圖，依類別顯示不同顏色。
  - `quiverSeries`: 向量序列圖 (Quiver Series)。

## 使用方式 (Usage)

### 1. 準備設定檔
參考 `example_setting_file.py` 定義繪圖參數。設定檔通常包含不同變數的顯示範圍 (`xlim`, `ylim`)、標籤 (`xlabel`)、顏色 (`color`) 等。

```python
# basic_setting example
basic_setting = {
    'x' : dict(
        lim=(12, 36),
        label=r'X',
        ticks=[12, 20, 28, 36],
        plot_set=dict(label='X.', color='#fd3535'),
        sca_set=dict(cmap='jet',vmin=20,vmax=50)
    ),

    'y' : dict(
        lim=(10, 30),
        label=r'Y',
        ticks=[10, 20, 30],
        plot_set=dict(label='Y.', color='#fd3535'),
        sca_set=dict(cmap='jet',vmin=20,vmax=50)
    ),
}
```

### 2. import 繪圖函數

```python
import pandas as pd
import numpy as np
from datetime import datetime
from PlotTemplate import templatePlot as plot, config

plot.iniParams.showPic = False
bsc_set = config.setting_parser()
plot.iniParams.pathPicOut = Path('picture')

# 準備資料
data_x = pd.DataFrame(np.random.randn(100))
data_y = pd.DataFrame(np.random.randn(100))


plot.scatter(data_x, data_y,
             main_set=bsc_set.set_sca('x-y'),
             linregre=True,
             line_1to1=True,
             nam='xy',
             title=f'test x, y'
            )
```

## 核心模組說明

### `config.py`
提供 `setting_parser` 類別，用於載入預設設定並允許使用者透過外部檔案更新設定。

### `templatePlot.py`
包含主要的繪圖函數。所有繪圖函數均被裝飾器包裝，自動處理圖表初始化 (`fig`, `ax`)、字體設定與圖片儲存。

- `tmSeries(...)`: 繪製時間序列。
- `scatter(...)`: 繪製散佈圖，可選擇是否疊加回歸線。
- `bivariatePolarPlot(...)`: 繪製極座標圖。

### `core/func.py`
定義了 `@_template_setting` 裝飾器，這是整個框架的核心，負責：
- 建立 `matplotlib` figure 和 axes。
- 設定全域字體 (Times New Roman)。
- 捕捉繪圖錯誤。
- 自動儲存圖片到 `picture/` 目錄下對應的子資料夾中。

## 輸出
繪製完成的圖片預設會儲存在專案目錄下的 `picture/` 資料夾中，並根據圖表類型自動分類 (例如 `picture/timeSeries/`, `picture/scatter/`)。
