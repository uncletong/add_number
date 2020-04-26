# add_number
支持的系统：
* Windows

快速添加下载专辑中的音轨的序号
当前支持：
* 网易云音乐
* QQ音乐

支持的音频格式：
* MP3 (ID3 v1, v1.1, v2.2, v2.3+)
* Wave/RIFF
* OGG
* OPUS
* FLAC
* WMA
* MP4/M4A/M4B

## 效果预览
从网易云音乐/QQ音乐下载的专辑文件如下：
![](https://github.com/uncletong/-/blob/master/1587904031(1).jpg)
使用程序后，会自动删除文件名【-】以及以前的信息，并添加曲目编号，曲目编号根据音乐文件中的元数据的音轨号自动生成。效果如下
![](https://github.com/uncletong/-/blob/master/1587904410(1).jpg)

## 安装和使用
`git clone https://github.com/uncletong/add_number.git`

然后需要安装依赖,在下载的文件夹内：

`pip install -r requeriments.txt`

打开命令行，进入所在文件夹内，输入

`python add_number.py `

然后将需要处理的专辑文件夹拖入，敲下回车，即可进行自动处理
![](https://github.com/uncletong/-/blob/master/3.gif)


