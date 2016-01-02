/**
 * Created by alejandrojnm on 11/15/14.
 */
$('.removejob').click(function (e) {

    var btn = $(this);
    var idjob = btn.data('job');

    var dataString = "job=" + idjob;

    $.ajax({
        url: "/job/remove/",
        type: "POST",
        data: dataString,
        dataType: "json",
        success: function (result) {
            var jobName = result.job.split(':');
            if (result.status == 'OK') {
                $('.top-right').notify({
                    message: {text: 'Removing job ' + jobName[0]+':'+jobName[1] + ' success'},
                    closable: false,
                    type: 'bangTidy'
                }).show();
            }
            if(result.status == 'FAIL'){
                $('.top-right').notify({
                    message: {text: 'Error removing job ' + jobName[0]+':'+jobName[1] + ' still in use'},
                    closable: false,
                    type: 'bangTidy'
                }).show();
            }
            if(result.status == 'JOB_NOT_FOUND'){
                $('.top-right').notify({
                    message: {text: 'The job ' + jobName[0]+':'+jobName[1] + ' not exist'},
                    closable: false,
                    type: 'bangTidy'
                }).show();
            }
            //else {
            //    console.log('Undepoy jobs Fails')
            //}
        },
        error: function (jqXHR, status, error) {
            console.log("status:", status);
        }
    });
});

$('.undeploy').click(function (e) {

    var btn = $(this);
    var idhost = btn.data('host');
    var idjob = btn.data('job');

    var dataString = "host=" + idhost + "&job=" + idjob;

    $.ajax({
        url: "/job/undeploy/",
        type: "POST",
        data: dataString,
        dataType: "json",
        success: function (result) {
            var jobName = result.job.split(':');
            if (result.status == 'OK') {
                $('.top-right').notify({
                    message: {text: 'Undepoy job ' + jobName[0]+':'+jobName[1] + ' success'},
                    closable: false,
                    type: 'bangTidy'
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

$('.start-stop').click(function (e) {

    var btn = $(this);
    var idhost = btn.data('host');
    var idjob = btn.data('job');
    var statusjob = btn.data('status');

    var dataString = "host=" + idhost + "&job=" + idjob + "&status=" + statusjob;

    $.ajax({
        url: "/job/start-stop/",
        type: "POST",
        data: dataString,
        dataType: "json",
        success: function (result) {
            var jobName = result.job.split(':');
            if (result.status == 'OK') {
                $('.top-right').notify({
                    message: {text: 'The job ' + jobName[0]+':'+jobName[1] + ' in ' + result.host + ' was ' + statusjob + ' success'},
                    closable: false,
                    type: 'bangTidy'
                }).show();
            }
            else {
                console.log('Stop job Fails')
            }
        },
        error: function (jqXHR, status, error) {
            console.log("status:", status);
        }
    });
});