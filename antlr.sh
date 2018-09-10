#!/usr/bin/env bash

# Adapted from https://github.com/antlr/antlr4/blob/master/doc/getting-started.md

cd /usr/local/lib
curl -O http://www.antlr.org/download/antlr-4.7.1-complete.jar

export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"

alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java org.antlr.v4.gui.TestRig'

# Adapted from https://github.com/antlr/antlr4/blob/master/doc/python-target.md

antlr4 -Dlanguage=Python3 -o . -lib . pacifica/jsonpath/parser/JSONPath.g4
