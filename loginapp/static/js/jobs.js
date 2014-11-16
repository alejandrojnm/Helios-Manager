/**
 * Created by alejandrojnm on 11/15/14.
 */
$('.jobs').click(function (e) {
    /*
    $.ajax().always(function () {
        btn.button('reset')
        btn.html('Pending Request');
    });
    */
    var btn = $(this)
    var id = btn.data('id');

    $('.modal-body').load('/job/show/', {id: id});
    $('#job').modal('toggle')

});