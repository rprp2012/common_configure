runtime! debian.vim
"设置编码
set encoding=utf-8
set fencs=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
set fileencodings=utf-8,ucs-bom,chinese
 
"语言设置
set langmenu=zh_CN.UTF-8
 
"设置语法高亮
syntax enable
syntax on
"设置搜索高亮
set hls
 
"设置配色方案
colorscheme torte
 
"可以在buffer的任何地方使用鼠标
set mouse=a
set selection=exclusive
set selectmode=mouse,key
 
"高亮显示匹配的括号
set showmatch
 
"去掉vi一致性
set nocompatible

"显示行号
set nu
"长久显示状态栏
set laststatus=2

"设置缩进
set tabstop=4
set softtabstop=4
set shiftwidth=4
set autoindent
set cindent
if &term=="xterm"
    set t_Co=8
    set t_Sb=^[[4%dm
    set t_Sf=^[[3%dm
endif
 
"打开文件类型自动检测功能
"filetype on
"filetype indent on

"对于python，将tap变成4个空格
set expandtab
set softtabstop=4

"取消各种中间文件和备份
set noundofile
set nobackup
set noswapfile

" 关闭时保存折叠，启动时加载折叠
au BufWinLeave * silent mkview
au BufWinEnter * silent loadview

"""""""""""""ctags和taglist设置
"设置ctags路径
let Tlist_Ctags_Cmd = "ctags.exe"
"不同时显示多个文件的tag，仅显示一个
let Tlist_Show_One_File = 1
"taglist为最后一个窗口时，退出vim
let Tlist_Exit_OnlyWindow = 1
"taglist窗口显示在右侧，缺省为左侧
"let Tlist_Use_Right_Window =1
"设置taglist窗口大小
"let Tlist_WinHeight = 100
let Tlist_WinWidth = 40
"设置taglist打开关闭的快捷键F8
noremap <F8> :TlistToggle<CR>
"更新ctags标签文件快捷键设置
noremap <F7> :!ctags -R<CR>
