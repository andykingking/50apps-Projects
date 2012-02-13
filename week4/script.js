(function() {
<<<<<<< HEAD
  var make_note;
  make_note = function() {
    var d;
    d = new Date();
    return '<div class="note ui-draggable"><div class="title">' + d.getDate() + '/' + (d.getMonth() + 1) + '/' + d.getFullYear() + ' ' + d.toTimeString().slice(0, 5) + '</div><textarea></textarea></div>';
  };
  $(document).ready(function() {
    return $("#make").click(function() {
=======
  var append_note, deobjectify_notes, getActiveColor, make_note, objectify_notes, remove_note;

  getActiveColor = function() {
    return $(".active").attr("id");
  };

  make_note = function() {
    var d;
    d = new Date();
    return '<div class="note ui-draggable ' + getActiveColor() + '"><div class="title">' + d.getDate() + '/' + (d.getMonth() + 1) + '/' + d.getFullYear() + ' ' + d.toTimeString().slice(0, 5) + '</div><textarea></textarea></div>';
  };

  objectify_notes = function() {
    var notes;
    notes = new Array;
    $('.note').each(function() {
      var code_html, value_html;
      code_html = $(this).clone().wrap("div").parent().html().slice(9);
      value_html = $(this).children('textarea').val();
      return notes[notes.length] = {
        code: code_html,
        text: value_html
      };
    });
    return localStorage.setItem("notes", JSON.stringify(notes));
  };

  append_note = function(note) {
    var element;
    element = $(note['code']);
    $(element).children('textarea').val(note['text']);
    return $("#pad").prepend(element);
  };

  deobjectify_notes = function(notes) {
    var note, _i, _len, _results;
    _results = [];
    for (_i = 0, _len = notes.length; _i < _len; _i++) {
      note = notes[_i];
      _results.push(append_note(note));
    }
    return _results;
  };

  remove_note = function(event, ui) {
    ui.draggable.remove();
    return objectify_notes();
  };

  $(document).ready(function() {
    var notes;
    $("#make").click(function() {
>>>>>>> master
      $("#pad").prepend(make_note());
      return $(".note").draggable({
        handle: "div.title",
        stack: ".note"
      });
    });
<<<<<<< HEAD
  });
=======
    $(".colorpicker").click(function() {
      $(".active").removeClass("active");
      return $(this).addClass("active");
    });
    $("#remove").droppable({
      drop: remove_note
    });
    if (typeof localStorage !== 'undefined') {
      notes = JSON.parse(localStorage.getItem("notes"));
      if (notes !== null) {
        deobjectify_notes(notes);
        $(".note").draggable({
          handle: "div.title",
          stack: ".note"
        });
      }
    }
    return $(document).keyup(function() {
      return objectify_notes();
    });
  });

>>>>>>> master
}).call(this);
