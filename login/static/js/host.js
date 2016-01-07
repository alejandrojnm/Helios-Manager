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
            var jobName = result.job.split(':');
            if (result.status == 'OK') {
                $('#addjob').modal('toggle');
                $('.top-right').notify({
                    message: {html: 'Job <strong>'+ jobName[0]+':'+jobName[1] +'</strong> was deploy success'},
                    closable: false,
                    type: 'heliosmanager'
                }).show();
            }
            if (result.status == 'JOB_ALREADY_DEPLOYED') {
                $('#addjob').modal('toggle');
                $('.top-right').notify({
                    message: {html: 'Job <strong>'+ jobName[0]+':'+jobName[1] +'</strong> is already deployed in this host'},
                    closable: false,
                    type: 'heliosmanager'
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

