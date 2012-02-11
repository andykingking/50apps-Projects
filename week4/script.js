(function() {
  var make_note;
  make_note = function() {
    var d;
    d = new Date();
    return '<div class="note ui-draggable"><div class="title">' + d.getDate() + '/' + (d.getMonth() + 1) + '/' + d.getFullYear() + ' ' + d.toTimeString().slice(0, 5) + '</div><textarea></textarea></div>';
  };
  $(document).ready(function() {
    return $("#make").click(function() {
      $("#pad").prepend(make_note());
      return $(".note").draggable({
        handle: "div.title",
        stack: ".note"
      });
    });
  });
}).call(this);
