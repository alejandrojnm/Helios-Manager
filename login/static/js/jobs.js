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
    $('.modal-body').html('');
    $('.modal-body').load('/job/show/', {id: id});
    $('#job').modal('toggle')

});

$('.undeploy').click(function (e) {

    var btn = $(this)
    var idhost = btn.data('host');
    var idjob = btn.data('job');

    var dataString = "host=" + idhost + "&job=" + idjob;

    $.ajax({
        url: "/job/undeploy/",
        type: "POST",
        data: dataString,
        dataType: "json",
        success: function (result) {
            if (result.status == 'OK') {
                $('.top-right').notify({
                    message: {text: 'Undepoy job ' + result.job + ' success'},
                    closable: false
                }).show();
            }
            else {
                console.log('Undepoy jobs Fails')
            }
        },
        error: function (jqXHR, status, error) {
            console.log("status:", status);
        }
    });
});