" Vim syntax file for rollit
" Language:         rollit
" Maintainer:       Brendan

" Quit when a syntax file was already loaded
if version < 600
  syntax clear
elseif exists("b:current_syntax")
  finish
endif

" We need nocompatible mode in order to continue lines with backslashes.
" Original setting will be restored.
let s:cpo_save = &cpo
set cpo&vim

syn keyword rollitRepeat            until do except for every that at after restart before when
syn keyword rollitException         attempt but always occurs oops
syn keyword rollitLoad              load from into
syn keyword rollitConditional       use if then and or not has otherwise unless
syn keyword rollitLeave             leave
syn keyword rollitOperator	        and has not or isa
syn keyword rollitClear             clear

syn match   rollitspecialentries    "<\s*[=\.:\^!]\s*>" display
syn match   rollitSpecialEntries    "<\s*clear\s*>" display
"syn match   rollitSpecialAccessors  "<\s*[=\.:]\s*>" display
syn match   rollitEscape	        +\\[abfnrtv'\\]+ contained
syn match   rollitEscape	        "\%(\\u\x\{4}\|\\U\x\{8}\)" contained
syn match   rollitNumber            "\(\(\h\w*\)\@<!\|d\)\@<=\d\+\(\(\w*\h\)\@!\|d\)\@=" display
syn match   rollitFloat             "\(\h\w*\)\@<!\d\+\.\d\+\(\w*\h\)\@!" display
syn match   rollitSpecialName       "[~\$?!]" skipwhite nextgroup=rollitModifierCall,rollitOperator
syn match   rollitOperator          "[+=\-\*\^&%]=\?" display
syn match   rollitDice              "\(\h\w*\)\@<!d\(\w*\h\)\@!" display
syn match   rollitOperator          "%/" display
syn match   rollitModOperator       "->" display contained display
syn match   rollitModOperator       "\(<\)\@<!=>" display contained display
syn match   rollitModOperator       "\(<\)\@<!:>" display contained display
"syn match   rollitModOperator       "[=-:]>" display contained display
syn match   rollitModOperator       "<-" display contained display
syn match   rollitDelimeter         "|" display
syn match   rollitModifierDef       "\h\w*\s*<-\s*" display contains=rollitModOperator
syn match   rollitModifierCall      "\s*[:=-]>\s*\h\w*" display contains=rollitModOperator
syn match   rollitEmptyRoll         "\[\s*:\s*\]" display
syn match   rollitEmptyBag          "{\s*:\s*}" display

syn keyword rollitTodo              FIXME NOTE NOTES TODO XXX CONSIDER contained
syn match   rollitComment	        "//.*$" contains=rollitTodo,@Spell

syn region rollitString     start="\z\('\)" end="\z1" contains=rollitEscape,@Spell
syn region rollitRollDef    start="\[:\(\]\)\@!" end=":\]" contains=ALL fold
syn region rollitBlock      start="\[\(:\)\@!" end="\(:\)\@<!\]" contains=ALLBUT,rollitExpand fold
syn region rollitBagDef     start="{:\(}\)\@!" end=":}" display contains=ALL fold
syn region rollitReduce     start="{\(:\)\@!" end="\(:\)\@<!}" display
            \ contains=ALLBUT,rollitModifierDef,rollitDelimeter,rollitLeave,
syn region rollitRawAccess  start="\.<" end=">" display
            \ contains=ALLBUT,rollitModifierDef,rollitDelimeter,rollitLeave,

" catch errors caused by wrong parenthesis
" syn region  rollitBlock	transparent matchgroup=rollitParen  start="(" end=")"
"             \ contains=@rollitTop,rollitParenT1
" syn region  rollitBlock1 transparent matchgroup=rollitParen1 start="(" end=")"
"             \ contains=@rollitTop,rollitParenT2 contained
" syn region  rollitBlock2 transparent matchgroup=rollitParen2 start="(" end=")"
"             \ contains=@rollitTop,rollitParenT  contained
" syn match   rollitBlockError	 ")"

"hi def link rollitStatement		    Statement
hi def link rollitspecialentries        StorageClass
hi def link rollitClear                 Keyword
hi def link rollitBagDef                Typedef
hi def link rollitEmptyBag              Typedef
hi def link rollitRollDef               Structure
hi def link rollitEmptyRoll             Structure
hi def link rollitException             Exception
hi def link rollitConditional           Conditional
hi def link rollitLeave                 Function
hi def link rollitModifierDef           Function
hi def link rollitModifierCall          Function
hi def link rollitRepeat		        Repeat
hi def link rollitLoad			        Include
hi def link rollitSpecialName		    SpecialChar
hi def link rollitTodo			        Todo
hi def link rollitString		        String
hi def link rollitNumber		        Number
hi def link rollitFloat		            Float
hi def link rollitOperator		        Operator
hi def link rollitDice    		        Operator
hi def link rollitModOperator		    Operator
hi def link rollitExpand		        Operator
hi def link rollitDelimeter		        Delimeter
hi def link rollitEscape		        Special
hi def link rollitComment		        Comment


let b:current_syntax = "rollit"

let &cpo = s:cpo_save
unlet s:cpo_save
