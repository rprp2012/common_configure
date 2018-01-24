# Custom Configuration for Tools

Here are personal configurations for many tools by rprp2012.

## Vim Congiure
.vimrc is for Vim.
### linux
1.在"~/"下创建".vim"文件夹  
2.安装vundle  
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim  
3.修改.vimrc  
将.vimrc.vundle里的内容添加到.vimrc里  
4.安装需要的插件  
将想要安装的插件,按照地址填写方法,将地址填写在"vundle#begin"和"vundle#end"之间就可以保存之后,启动vim运行":PluginInstall"  
5.移除不需要的插件  
编辑.vimrc文件移除的你要移除的插件所对应的plugin那一行,保存退出当前的vim  
重新打开vim，输入命令BundleClean  
6.其他  
更新插件BundleUpdate  
列出所有插件BundleList  
查找插件BundleSearch  

## Tmue Configure
.tmux.conf is for Tmux.  
