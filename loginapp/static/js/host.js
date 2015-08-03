/**
 * Created by alejandrojnm on 12/29/14.
 */
$('.helios-thumbnail').click(function(){
    var btn = $(this);
    //$('#'+btn.data('helios-host')+'-info').toggleClass('hide').slideDown()
    console.log(btn.data('helios-host'))

})

//$('.helios-thumbnail').click(function () {
//    var btn = $(this);
//    btn[0].parentNode
//
//    $('#'+btn.data('helios-host')).after('<div class="col-md-12"><div style="background-color: #cecece; padding: 9px">'+btn.data('helios-host')+'</div></div>').slideDown(1000,  "easeInBack");
//
//    console.log(btn.data('helios-host'))
//    //var selectedPos = $(this).index(); // get selected position //
//    //// find wrap element:
//    ////var containerWidth = container.width();
//    ////var elementsInRow = Math.floor(containerWidth / 100 );
//    //var elementsInRow = 4; // use this if container's width is fixed
//    //var row = Math.floor(selectedPos / elementsInRow) + 1;
//    //var wrapPos = (row * elementsInRow);
//    //
//    //// if selected is on last row, use as wrap the last element:
//    //var size = elements.length;
//    //if (wrapPos >= size) {
//    //    wrapPos = size;
//    //}
//    //wrapPos = wrapPos - 1;
//    //console.log(selectedPos);
//    //console.log(elementsInRow);
//    //var pointerPos = 40 + ((selectedPos % elementsInRow) * 110)
//    //console.log(selectedPos % elementsInRow);
//    //console.log((selectedPos % elementsInRow) * 110);
//    //console.log('left: ' + pointerPos);
//    //console.log(size);
//    //// next line added by CrocoDillon, didn't do any cleanup of old calculations :P
//    //pointerPos = $(this).position().left + $(this).width() / 2 - 10;
//    //// end edit;
//    //if (wrapPos == oldWrapPos) {
//    //    $('.info-pc').css("left", pointerPos + 'px');
//    //} else {
//    //    oldWrapPos = wrapPos;
//    //    elements.removeClass('edge');
//    //    $(elements[wrapPos]).addClass('edge');
//    //    $('.info-bg').slideUp(function () {
//    //        $(this).remove();
//    //    });
//    //    $('.edge').after('<div class="info-bg"><div class="info-pc" style="left:'
//    //        + pointerPos + 'px"></div><div class="info-cl"></div></div>');
//    //    $('.info-bg').slideDown();
//    //}
//});