
/*
* Uses jQuery!!!!111one
*/


/*====================================
=            ON DOM READY            =
====================================*/
$(function() {

    // Toggle Nav on Click
    $('.toggle-nav').click(function() {
        // Calling a function in case you want to expand upon this.
        toggleNav();
    });


});


/*========================================
=            CUSTOM FUNCTIONS            =
========================================*/
function toggleNav() {
    if ($('#site-wrapper').hasClass('show-nav')) {
        // Do things on Nav Close
        $('#site-wrapper').removeClass('show-nav');
        $('#site-wrapper').css("overflow", "");
    } else {
        // Do things on Nav Open
        $('#site-wrapper').addClass('show-nav');
        $('#site-wrapper').css("overflow", "hidden");
    }

    //$('#site-wrapper').toggleClass('show-nav');
};


/*
(function() {
  [].slice.call(document.querySelectorAll('.navbar')).forEach(function(menu) {
    var menuItems = menu.querySelectorAll('.nav-link'),
      setCurrent = function(ev) {
        ev.preventDefault();

        var item = ev.target.parentNode; // li

        // return if already current
        if (classie.has(item, 'nav-item--current')) {
          return false;
        }
        // remove current
        classie.remove(menu.querySelector('.nav-item--current'), 'nav-item--current');
        // set current
        classie.add(item, 'nav-item--current');
      };

    [].slice.call(menuItems).forEach(function(el) {
      el.addEventListener('click', setCurrent);
    });
  });

  [].slice.call(document.querySelectorAll('.link-copy')).forEach(function(link) {
    link.setAttribute('data-clipboard-text', location.protocol + '//' + location.host + location.pathname + '#' + link.parentNode.id);
    new Clipboard(link);
    link.addEventListener('click', function() {
      classie.add(link, 'link-copy--animate');
      setTimeout(function() {
        classie.remove(link, 'link-copy--animate');
      }, 300);
    });
  });
})(window);
*/


$(function() {

  $('#login-form-link').click(function(e) {
  $("#login-form").delay(100).fadeIn(100);
  $("#register-form").fadeOut(100);
  $('#register-form-link').removeClass('active');
  $(this).addClass('active');
  e.preventDefault();
  });
  $('#register-form-link').click(function(e) {
  $("#register-form").delay(100).fadeIn(100);
  $("#login-form").fadeOut(100);
  $('#login-form-link').removeClass('active');
  $(this).addClass('active');
  e.preventDefault();
  });

});


document.querySelector(".card-flip").classList.toggle("flip");
