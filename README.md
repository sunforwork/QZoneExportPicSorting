# QZoneExportPicSorting

QZoneExport插件的说说图片分拣工具（按年份、时间分拣）

## 使用指南

1. 下载 [QZoneExport 插件](https://github.com/ShunCai/QZoneExport) 的 release，并使用 JSON 格式备份你的空间。
2. 安装 Python 环境。如果你不会，请参考 [这个教程](https://zhuanlan.zhihu.com/p/344887837)。
3. 安装 ijson 库。使用命令行执行以下命令：
   ```sh
   pip install ijson
   ```
4. 修改 `1.py` 中的目录路径等相关信息为你的实际文件路径（请使用绝对路径）：
   ```python
   json_file_path = r'C:\Users\Administrator\Desktop\down\666\Messages\2014.json'
   img_source_dir = r'C:\Users\Administrator\Desktop\down\666\Messages\images'
   img_dest_dir = r'C:\Users\Administrator\Desktop\down\2014img'
   ```
5. 在你存放 `1.py` 的地方，打开文件资源管理器，在路径栏输入 `cmd`，以此路径打开命令行。
6. 输入 `python 1.py` 并等待执行完成。
