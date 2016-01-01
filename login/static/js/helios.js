/**
 * Created by alejandrojnm on 11/16/14.
 */
$(document).ready(function () {
    $('[data-toggle="popover"]').popover({trigger: 'hover', 'placement': 'bottom'});
    $('[data-toggle="tooltip"]').tooltip();

    //multiple select tr
    //$("#data tr").click(function () {
    //    $(this).toggleClass("highlight");
    //});

    //only select one tr
    //$("#data tr").click(function () {
    //    var selected = $(this).hasClass("highlight");
    //    //console.log($(this).attr('id'))
    //    $("#data tr").removeClass("highlight");
    //    if (!selected)
    //        $(this).addClass("highlight");
    //});
});