@rem 切换到ui文件所在目录
@cd bigapp\uis
@rem 编译
@pyuic5 -o videoui.py video.ui
@rem 重新切换到原来的路径
@cd ..\..