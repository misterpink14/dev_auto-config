"dein Scripts-----------------------------
set nocompatible               " Be iMproved

" Required:
set runtimepath+=~/.vim/dein/repos/github.com/Shougo/dein.vim " path to dein.vim
call dein#begin(expand('~/.vim/dein')) " plugins' root path


call dein#add('Shougo/dein.vim')
call dein#add('Shougo/vimproc.vim', {
    \ 'build': {
    \     'windows': 'tools\\update-dll-mingw',
    \     'cygwin': 'make -f make_cygwin.mak',
    \     'mac': 'make -f make_mac.mak',
    \     'linux': 'make',
    \     'unix': 'gmake',
    \    },
    \ })
call dein#add('Shougo/unite.vim')

" ----- PLUGINS -----
call dein#add('chrisbra/csv.vim',
     \{'on_ft': ['csv']})
call dein#add('scrooloose/nerdtree',
      \{'on_cmd': 'NERDTreeToggle'})
call dein#add('Xuyuanp/nerdtree-git-plugin',
      \{'on_cmd': 'NERDTreeToggle'})
call dein#add('Shougo/deoplete.nvim',
      \{'on_i': 1})
call dein#add('mhartington/deoplete-typescript',
      \{'on_ft': ['ts']})
call dein#add('leafgarland/typescript-vim',
      \{'on_ft': ['ts']})
call dein#add('vim-airline/vim-airline')
call dein#add('vim-airline/vim-airline-themes')

" ----- THEMES -----
call dein#add('romainl/Apprentice',
		\{'rev': 'fancylines-and-neovim'})


call dein#end()

" Install plugins on startup.
if dein#check_install()
  call dein#install()
endif

"End dein Scripts-------------------------


set termguicolors
let base16colorspace=256  " Access colors present in 256 colorspace

" ----------- THEME ----------
syntax enable
" set background=dark
colorscheme apprentice

" ----------- TABS ----------
set tabstop=4           " Render TABs using this many spaces.
set shiftwidth=4
filetype plugin indent on

" ----------- Lines -----------
set ruler               " Show the line and column numbers of the cursor.
set number              " Show the line numbers on the left side.
set linespace=0         " Set line-spacing to minimum.
set showcmd             " Show command in bottom bar
set mouse=a             " Select text without line numbers

" ----------- Navigation -----------
noremap <Up> <NOP>
noremap <Down> <NOP>
noremap <Left> <NOP>
noremap <Right> <NOP>


" ----------- NERDTREE ----------
map <C-n> :NERDTreeToggle<CR>
" let g:NERDTreeDirArrowExpandable = '▸'
" let g:NERDTreeDirArrowCollapsible = '▾'
"Auto open for directories
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | endif
"Auto close vim if NERDTREE is the only thing open
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
" ----- git-plugin -----
let g:NERDTreeIndicatorMapCustom = {
    \ "Modified"  : "✹",
    \ "Staged"    : "✚",
    \ "Untracked" : "✭",
    \ "Renamed"   : "➜",
    \ "Unmerged"  : "═",
    \ "Deleted"   : "✖",
    \ "Dirty"     : "✗",
    \ "Clean"     : "✔︎",
    \ 'Ignored'   : '☒',
    \ "Unknown"   : "?"
    \ }
let g:NERDTreeWinSize = 40

" ----------- vim-airline -----------
let g:airline#extensions#tabline#enabled = 1
" let g:airline#extensions#tabline#left_sep = ' '
" let g:airline#extensions#tabline#left_alt_sep = '|'
let g:airline_detect_paste=1
let g:airline_detect_crypt=1
let g:airline#extensions#tabline#fnamemod = ':t'

" This allows buffers to be hidden if you've modified a buffer.
" This is almost a must if you wish to use buffers in this way.
set hidden

" ----------- deoplete ---------
let g:deoplete#enable_at_startup = 1 " Use deoplete.

" ----------- te ----------
:tnoremap <Esc> <C-\><C-n>
:tnoremap <expr> <C-R> '<C-\><C-N>"'.nr2char(getchar()).'pi'


