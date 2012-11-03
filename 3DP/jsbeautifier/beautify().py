import jsbeautifier
res = jsbeautifier.beautify("String.prototype.trim = function(){ this.replace( /^\s+|\s+$/g, '' ); }")

print res