grammar JSONPath;

jsonpath
   : '$' subscript? EOF
   ;

subscript
   : '..' ( subscriptableBareword | subscriptables ) subscript?
   | '.' subscriptableBareword subscript?
   | subscriptables subscript?
   ;

subscriptables
   : '[' subscriptable ( ',' subscriptable )* ']'
   ;

subscriptableBareword
   : ID
   | '*'
   ;

subscriptable
   : STRING
   | NUMBER{self.tryCast(int)}? ( ':' ( NUMBER{self.tryCast(int)}? )? ( ':' NUMBER{self.tryCast(int)}? )? )?
   | '*'
   | '?' '(' expression ')'
   ;

expression
   : andExpression
   ;

andExpression
   : orExpression ( 'and' andExpression )?
   ;

orExpression
   : notExpression ( 'or' orExpression )?
   ;

notExpression
   : 'not' notExpression
   | '(' expression ')'
   | ( '$' | '@' ) subscript? ( ( '=' | '!=' | '<' | '<=' | '>' | '>=' ) value )?
   ;


ID
   : [_A-Za-z] [_A-Za-z0-9]*
   ;


/* c.f., https://github.com/antlr/grammars-v4/blob/master/json/JSON.g4 */

json
   : value
   ;

obj
   : '{' pair (',' pair)* '}'
   | '{' '}'
   ;

pair
   : STRING ':' value
   ;

array
   : '[' value (',' value)* ']'
   | '[' ']'
   ;

value
   : STRING
   | NUMBER
   | obj
   | array
   | 'true'
   | 'false'
   | 'null'
   ;


STRING
   : '"' (ESC | SAFECODEPOINT)* '"'
   ;


fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;
fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;
fragment HEX
   : [0-9a-fA-F]
   ;
fragment SAFECODEPOINT
   : ~ ["\\\u0000-\u001F]
   ;


NUMBER
   : '-'? INT ('.' [0-9] +)? EXP?
   ;


fragment INT
   : '0' | [1-9] [0-9]*
   ;

// no leading zeros

fragment EXP
   : [Ee] [+\-]? INT
   ;

// \- since - means "range" inside [...]

WS
   : [ \t\n\r] + -> skip
   ;
