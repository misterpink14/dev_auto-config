set termguicolors
let base16colorspace=256  " Access colors present in 256 colorspace
syntax enable
set background=dark

" --------- TABS ----------
set tabstop=4           " Render TABs using this many spaces.
set shiftwidth=4

" --------- Lines ----------
set ruler               " Show the line and column numbers of the cursor.
set number              " Show the line numbers on the left side.
set linespace=0         " Set line-spacing to minimum.
set showcmd             " Show command in bottom bar
set mouse=a             " Select text without line numbers

" --------- Disable arrow key navigation ----------
noremap <Up> <NOP>
noremap <Down> <NOP>
noremap <Left> <NOP>
noremap <Right> <NOP>

" --------- NTerminal ---------
" exit terminal mode with esc
tnoremap <Esc> <C-\><C-n>
" simulate recursive search
tnoremap <expr> <C-R> '<C-\><C-N>"'.nr2char(getchar()).'pi'
" move in terminal
tnoremap <A-h> <C-\><C-N><C-w>h
tnoremap <A-j> <C-\><C-N><C-w>j
tnoremap <A-k> <C-\><C-N><C-w>k
tnoremap <A-l> <C-\><C-N><C-w>l
inoremap <A-h> <C-\><C-N><C-w>h
inoremap <A-j> <C-\><C-N><C-w>j
inoremap <A-k> <C-\><C-N><C-w>k
inoremap <A-l> <C-\><C-N><C-w>l
nnoremap <A-h> <C-w>h
nnoremap <A-j> <C-w>j
nnoremap <A-k> <C-w>k
nnoremap <A-l> <C-w>l


