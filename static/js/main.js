// Para que el menú sea del mismo tamaño que la sección fuera de él

  function htmlbodyHeightUpdate() {
    var height3 = $(window).height();
    var height1 = $('.nav').height() + 50;
    height2 = $('.container-main').height();
    if (height2 > height3) {
        $('html').height(Math.max(height1, height3, height2) + 10);
        $('body').height(Math.max(height1, height3, height2) + 10);
    } else
    {
        $('html').height(Math.max(height1, height3, height2));
        $('body').height(Math.max(height1, height3, height2));
    }

  }

(function( $ ){
    $.fn.get_csrf = function() {
        var end, start;
        start = document.cookie.indexOf('csrftoken=');
        end = document.cookie.indexOf(";", start);
        if (-1 === end) {
            end = document.cookie.length;
        }
        csrftoken = document.cookie.substring(start, end).replace('csrftoken=', '');
        return csrftoken;
    };
})( $ );

  $(document).ready(function () {
    htmlbodyHeightUpdate();
    $(window).resize(function () {
        htmlbodyHeightUpdate();
    });
    $(window).scroll(function () {
        height2 = $('.container-main').height();
        htmlbodyHeightUpdate();
    });
    $('.modificacionNombreGrupo').on('click', function(){
        $.ajax({
            type: 'POST',
            url: '/groups/',
            headers: {
                 'x-csrftoken': $().get_csrf()
            },
            data: {
                'groupName': $('#groupName-'+this.id.replace('cambiarNombre-', '')).val(),
                'action': 'modificacion',
                'groupId': this.id.replace('cambiarNombre-', '')
            },
            success: function(){
                location.reload();
            },
            error: function(){
            }
        })
    });

    $('.eliminarGrupoButton').on('click', function(){
        $.ajax({
            type: 'POST',
            url: '/groups/',
            headers: {
                 'x-csrftoken': $().get_csrf()
            },
            data: {
                'action': 'eliminar',
                'groupId': this.id.replace('eliminarNombre-', '')
            },
            success: function(){
                location.reload();
            },
            error: function(){
            }
        });
    });

    $('.agregarPaciente').on('click', function(){
        var pacientes = []
        $.map($('input:checked'), function(n, i){
            pacientes.push(parseInt(n.id.replace('pacient-', '')));
        });
        if (pacientes.length < 1){
            return false;
        }
        $.ajax({
            type: 'POST',
            url: '/groups/',
            headers: {
                'x-csrftoken': $().get_csrf()
            },
            data: {
                'action': 'agregarPacientes',
                'groupId': this.id.replace('agregarPaciente-', ''),
                'childs[]': pacientes
            },
            success: function(){
                location.reload();
            },
            error: function(){
            }
        })
    });

    $('.eliminarPaciente').on('click', function(){
        $.ajax({
            type: 'POST',
            url: '/patients/',
            headers: {
                 'x-csrftoken': $().get_csrf()
            },
            data: {
                'action': 'eliminar',
                'childrenId': this.id.replace('deleteChildren-', '')
            },
            success: function(){
                location.reload()
            },
            error: function(data){
                console.log(data);
            }
        })
    });

    $('.selectedGroup').on('click', function(){
        $('.accordionGroup').hide();
        if (this.id == 0){
            $('.accordionGroup').show();
        }
        else {
            $('#accordion-'+this.id).show();
        }
        var form = jQuery('#formi');
        $('.groupSelected').val(this.id)
        form.get(0).submit();
    });
  });


// Se cambia la apariencia de todos los file input
  $(function() {
    // We can attach the `fileselect` event to all file inputs on the page
    $(document).on('change', ':file', function() {
      var input = $(this),
          numFiles = input.get(0).files ? input.get(0).files.length : 1,
          label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
      input.trigger('fileselect', [numFiles, label]);
    });
    // We can watch for our custom `fileselect` event like this
    $(document).ready( function() {
        $(':file').on('fileselect', function(event, numFiles, label) {

            var input = $(this).parents('.input-group').find(':text'),
                log = numFiles > 1 ? numFiles + ' files selected' : label;

            if( input.length ) {
                input.val(log);
            } else {
                if( log ) alert(log + ' ha sido seleccionado');
            }

        });
    });
  });

// Muestra flecha para saber si el acordeon está abierto o cerrado
  $('.collapse').on('shown.bs.collapse', function(){
    $(this).parent().find(".fa-caret-down").removeClass("fa-caret-down").addClass("fa-caret-up");
    }).on('hidden.bs.collapse', function(){
    $(this).parent().find(".fa-caret-up").removeClass("fa-caret-up").addClass("fa-caret-down");
  });

// Se cambia apariencia de radio input
  $(document).ready(function () {
    $('.select-input').click(function () {
      $('input:not(:checked)').parent().removeClass("active");
      $('input:checked').parent().addClass("active");
    });
  });
