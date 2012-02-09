(function() {
  var add_note, make_note;
  $('.note').onmousedown = function() {
    return this.mousemove = function(e) {
      return this.posLeft = e.pageY && (this.posTop = e.PageX);
    };
  };
  $('.note').onmouseup = function() {
    return this.mousemove = null;
  };
  make_note = function() {
    return $('<textarea class="note">Text here</textarea>');
  };
  add_note = function() {
    return make_note().appendTo("section");
  };
  $(document).ready(function() {
    return $('button'.click = function() {
      return add_note;
    });
  });
}).call(this);
