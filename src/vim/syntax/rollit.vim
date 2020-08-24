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

syn keyword rollitRepeat        until do except when for every that at after restart before
syn keyword rollitLoad          load from into
syn keyword rollitConditional   use if then and or not has otherwise unless
syn keyword rollitLeave         leave
syn keyword rollitOperator	    and has not or

syn match   rollitEscape	     +\\[abfnrtv'\\]+ contained
syn match   rollitEscape	     "\%(\\u\x\{4}\|\\U\x\{8}\)" contained
syn match   rollitNumber         "\(\(\h\w*\)\@<!\|d\)\@<=\d\+\(\(\w*\h\)\@!\|d\)\@=" display
syn match   rollitFloat          "\(\h\w*\)\@<!\d\+\.\d\+\(\w*\h\)\@!" display
syn match   rollitSpecialName    "[~\$?!]" skipwhite nextgroup=rollitModifierCall,rollitOperator
syn match   rollitOperator       "[+=\-\*\^&]=\?" display
syn match   rollitOperator       "\(\h\w*\)\@<!d\(\w*\h\)\@!" display
syn match   rollitModOperator    "->" display contained display
syn match   rollitModOperator    "<-" display contained display
syn match   rollitExpand         "[@]" display contained
syn match   rollitDelimeter      "|" display
syn match   rollitModifierDef    "\h\w*\s*<-\s*" display contains=rollitModOperator
syn match   rollitModifierCall   "\s*->\s*\h\w*" display contains=rollitModOperator

syn keyword rollitTodo          FIXME NOTE NOTES TODO XXX CONSIDER contained
syn match   rollitComment	    "//.*$" contains=rollitTodo,@Spell

syn region rollitString     start="'" end="'" contains=rollitEscape,@Spell
syn region rollitBlock      start="\[" end="\]" contains=ALLBUT,rollitExpand fold
syn region rollitReduce     start="{" end="}" display
            \ contains=ALLBUT,rollitModifierDef,rollitDelimeter,rollitLeave,


"hi def link rollitStatement		    Statement
hi def link rollitConditional       Conditional
hi def link rollitLeave             Function
hi def link rollitModifierDef       Function
hi def link rollitModifierCall      Function
hi def link rollitRepeat		    Repeat
hi def link rollitLoad			    Include
hi def link rollitSpecialName		SpecialChar
hi def link rollitTodo			    Todo
hi def link rollitString		    String
hi def link rollitNumber		    Number
hi def link rollitFloat		        Float
hi def link rollitOperator		    Operator
hi def link rollitModOperator		Operator
hi def link rollitExpand		    Operator
hi def link rollitDelimeter		    Delimeter
hi def link rollitEscape		    Special
hi def link rollitComment		    Comment


let b:current_syntax = "rollit"

let &cpo = s:cpo_save
unlet s:cpo_save
