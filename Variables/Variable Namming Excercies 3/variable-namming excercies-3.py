var.123 = 99
print var.123

#error
var.123 = 99
    ...: print var.123
    ...:
  File "<ipython-input-18-9572e233cef3>", line 1
    var.123 = 99
          ^
SyntaxError: invalid syntax
#because in variable we can not type special character. In this var you use special character (.). That's why it show error.
