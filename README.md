# layerzero-sybil-query
LayerZero 女巫查询脚本


1. 安装依赖
这个脚本需要以下的Python库：
pandas
tqdm
logging
使用以下命令来安装这些库：
```pip install pandas tqdm```

2. 准备数据
myaddress.csv：倒入你的地址，注意要保留第一行的ADDRESS。
initialList.csv：这是LayerZero提供的80W女巫数据，不用管。

将这两个文件放在脚本的同一目录下。

3. 运行脚本
在终端中，切换到脚本所在的目录，然后使用以下命令来运行脚本：
```python main.py```
脚本运行时，会在终端中显示进度条和日志信息。女巫地址，会保存到程序目录下的`sybil.csv`文件中。