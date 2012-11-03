import jsbeautifier

opts = jsbeautifier.default_options()
print "brace_style=",opts.brace_style
print "eval_code=",opts.eval_code
print "indent_char=!%s!" % opts.indent_char
print "indent_size=",opts.indent_size
print "indent_with_tabs=",opts.indent_with_tabs
print "jslint_happy=",opts.jslint_happy
print "keep_array_indentation=",opts.keep_array_indentation
print "keep_function_indentation=",opts.keep_function_indentation
print "max_preserve_newlines=",opts.max_preserve_newlines
print "preserve_newlines=",opts.preserve_newlines
print "unescape_strings=",opts.unescape_strings

opts.brace_style="collapse"

source="String.prototype.trim = function(){ this.replace( /^\s+|\s+$/g, '' ); }"
res = jsbeautifier.beautify(source,opts)
