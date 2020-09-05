function compile() {
  var html = document.getElementById('HTML');
  var css = document.getElementById('CSS');
  var js = document.getElementById('JS');
  var code = document.getElementById('code').contentWindow.document;
  document.body.onkeyup = function () {
    code.open();
    code.writeln(
      html.value +
        '<style>' +
        css.value +
        '</style>' +
        '<script>' +
        js.value +
        '</script>',
    );
    code.close();
  };
}

compile();
