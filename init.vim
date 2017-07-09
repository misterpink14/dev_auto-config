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

" File Finding
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'

" Autocompletion
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
" File finding
"Plug 'cloudhead/neovim-fuzzy' " Need to install fzy via brew first

" Initialize plugin system
call plug#end()
" ^^^^^^^^^^^^  PLUGIN STOP  ^^^^^^^^^^^^

set cursorline               " highlight current line

" ----------- THEME ----------
syntax enable
set background=dark
let g:hybrid_custom_term_colors = 1
" let g:hybrid_reduced_contrast = 1 " Remove this line if using the default palette.
colorscheme hybrid
let g:airline_theme='hybrid'

" ----------- TABS ----------
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '|'

set tabstop=4           " Render TABs using this many spaces.
set tabstop=4
set shiftwidth=4
"set expandtab

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
let g:NERDTreeWinSize=40
" enable line numbers
let NERDTreeShowLineNumbers=1
" make sure relative line numbers are used
autocmd FileType nerdtree setlocal relativenumber

" --------- AutoCompletion ---------
let g:deoplete#enable_at_startup = 1

" --------- File Finding ----------
" nnoremap <C-p> :FuzzyOpen<CR>
set grepprg=rg\ --vimgrep
" --column: Show column number
" --line-number: Show line number
" --no-heading: Do not show file headings in results
" --fixed-strings: Search term as a literal string
" --ignore-case: Case insensitive search
" --no-ignore: Do not respect .gitignore, etc...
" --hidden: Search hidden files and folders
" --follow: Follow symlinks
" --glob: Additional conditions for search (in this case ignore everything in the .git/ folder)
" --color: Search color options
command! -bang -nargs=* Find call fzf#vim#grep('rg --column --line-number --no-heading --fixed-strings --ignore-case --no-ignore --hidden --follow --glob "!.git/*" --color "always" '.shellescape(<q-args>), 1, <bang>0)
" when in tmux...
" command! -bang -nargs=* Find call fzf#vim#grep('rg --column --line-number --no-heading --fixed-strings --ignore-case --no-ignore --hidden --follow --glob "!.git/*" --color "always" '.shellescape(<q-args>).'| tr -d "\017"', 1, <bang>0)

