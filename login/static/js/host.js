/**
 * Created by alejandrojnm on 12/29/14.
 */
//$('.helios-thumbnail').click(function(){
//    var btn = $(this);
//    //$('#'+btn.data('helios-host')+'-info').toggleClass('hide').slideDown()
//    console.log(btn.data('helios-host'))
//
//})

$('#deployJob').click(function(e){
    var idjob = $('#jobList').val();
    var idhost = $('#jobList').data('host');

    var dataString = "host=" + idhost + "&job=" + idjob;

    $.ajax({
        url: "/job/deploy/",
        type: "POST",
        data: dataString,
        dataType: "json",
        success: function (result) {
            if (result.status == 'OK') {
                $('#addjob').modal('toggle');
                $('.top-right').notify({
                    message: {text: 'Job ' + result.job + ' was deploy success'},
                    closable: true,
                    type: 'info'
                }).show();
            }
            else {
                console.log('Deploy jobs Fails')
            }
        },
        error: function (jqXHR, status, error) {
            console.log("status:", status);
        }
    });

});

