"set termguicolors
let base16colorspace=256  " Access colors present in 256 colorspace
syntax enable
set background=dark
" This line enables the true color support.
let $NVIM_TUI_ENABLE_TRUE_COLOR=1
set t_Co=256
set t_AB=m
set t_AF=m
if &term =~ '256color'
    set t_ut=
endif

" ----------- TABS ----------
set tabstop=4           " Render TABs using this many spaces.
set shiftwidth=4

" ----------- Lines -----------
set ruler               " Show the line and column numbers of the cursor.
set number              " Show the line numbers on the left side.
set linespace=0         " Set line-spacing to minimum.
set showcmd             " Show command in bottom bar
set mouse=a             " Select text without line numbers
set number relativenumber
augroup numbertoggle " Auto-toggle 
	autocmd!
	autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
	autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END

" ----------- Disable arrow key navigation -----------
noremap <Up> <NOP>
noremap <Down> <NOP>
noremap <Left> <NOP>
noremap <Right> <NOP>

" ----------- netrw -----------
let g:netrw_liststyle = 3
let g:netrw_banner = 0
"1 - open files in a new horizontal split
"2 - open files in a new vertical split
"3 - open files in a new tab
"4 - open in previous window
let g:netrw_browse_split = 0
let g:netrw_winsize = 20
"let g:netrw_altv = 1
"augroup ProjectDrawer
"  autocmd!
"  autocmd VimEnter * :Vexplore
"augroup END


"dein Scripts-----------------------------
if &compatible
  set nocompatible               " Be iMproved
endif

" Required:
set runtimepath+=$userhome/.local/share/dein/repos/github.com/Shougo/dein.vim

" Required:
if dein#load_state('$userhome/.local/share/dein')
  call dein#begin('$userhome/.local/share/dein')

  " Let dein manage dein
  " Required:
  call dein#add('$userhome/.local/share/dein/repos/github.com/Shougo/dein.vim')

  " Add or remove your plugins here:
  "call dein#add('Shougo/neosnippet.vim')
  "call dein#add('Shougo/neosnippet-snippets')

  call dein#add('fatih/vim-go', {'build': ':GoInstallBinaries', 'on_ft': 'go'})
  call dein#add('Shougo/deoplete.nvim')
  "pip3 install neovim
  "pip3 install --upgrade neovim
  "pip2 install --upgrade neovim
  call dein#add('zchee/deoplete-go', 
  	\{'build': 'make', 'on_ft': 'go', 'on_i': 1})
"  call dein#add('mhartington/nvim-typescript',
"  	\{'on_ft': 'ts', 'on_i': 1})
  call dein#add('leafgarland/typescript-vim',
  	\{'on_ft': 'ts'})
"  call dein#add('clojure-vim/async-clj-omni',
"	\{'on_ft': 'clj'})
"  call dein#add('clojure-vim/acid.nvim',
"  	\{'on_ft': 'clj'})

  " Required:
  call dein#end()
  call dein#save_state()
endif

" Required:
filetype plugin indent on
syntax enable

" If you want to install not installed plugins on startup.
if dein#check_install()
  call dein#install()
endif

"End dein Scripts-------------------------


" go-vim
set autowrite " auto save on build
" jump between errors quicker
map <C-n> :cnext<CR>
map <C-m> :cprevious<CR>
nnoremap <leader>a :cclose<CR>
let g:go_list_type = "quickfix" " all error lists will be quickfix
let g:go_fmt_command = "goimports"
let g:go_highlight_types = 1
let g:go_highlight_fields = 1
let g:go_highlight_functions = 1
let g:go_highlight_methods = 1
let g:go_highlight_operators = 1
let g:go_highlight_extra_types = 1
let g:go_highlight_build_constraints = 1 

" deoplete
let g:deoplete#enable_at_startup = 1

" deoplete go
"let g:deoplete#sources#go#gocode_binary = ''
"let g:deoplete#sources#go#package_dot = 0
"let g:deoplete#sources#go#sort_class = []
"let g:deoplete#sources#go#cgo = 0
"let g:deoplete#sources#go#goos = ''
"let g:deoplete#sources#go#gocode_binary = '~/go/bin/gocode'

