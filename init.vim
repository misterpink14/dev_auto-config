set termguicolors
let base16colorspace=256  " Access colors present in 256 colorspace


" vvvvvvvvvvvv  PLUGIN START  vvvvvvvvvvvv
" Using junegunn/vim-plug
" Specify a directory for plugins

" Auto-Update
if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin('~/.local/share/nvim/plugged')


" For CSV files
Plug 'chrisbra/csv.vim'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'w0ng/vim-hybrid'
Plug 'scrooloose/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'jistr/vim-nerdtree-tabs'
Plug 'tpope/vim-sensible'


" Initialize plugin system
call plug#end()
" ^^^^^^^^^^^^  PLUGIN STOP  ^^^^^^^^^^^^


" ----------- THEME ----------
syntax enable
set background=dark
let g:hybrid_custom_term_colors = 1
let g:hybrid_reduced_contrast = 1 " Remove this line if using the default palette.
colorscheme hybrid
let g:airline_theme='hybrid'

" ----------- TABS ----------
let g:airline#extensions#tabline#enabled = 1
" let g:airline#extensions#tabline#left_sep = ' '
" let g:airline#extensions#tabline#left_alt_sep = '|'

" ----------- NerdTree ----------
" Open if no files are specified
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
" Open if a directory is specified
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | endif
" Toggle with ctrl + n
map <C-n> :NERDTreeToggle<CR>
" Auto close vim if NerdTree is the only window open
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
" Arrow symbols
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'
" Make it prettier
let NERDTreeMinimalUI = 1
let NERDTreeDirArrows = 1
" Set width
let g:NERDTreeWinSize=20

