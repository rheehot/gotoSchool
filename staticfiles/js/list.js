$(document).ready(function() {
    // SCROLL TO BOTTOM OF MESSAGES
      var objDiv = document.getElementById('content');
      objDiv.scrollTop = objDiv.scrollHeight;
    // AVATARS
    $('.them .avatar').on('click',function(){
      if (!$(this).is(':animated')) {
        $(this).toggleClass('check',300,'swing');
      }
    });
    $('.you .avatar').on('click',function(){
      if (!$(this).is(':animated')) {
        $(this).toggleClass('check',300,'swing');
      }
    });
      // BACK & LATEST
      $('#back, .latest').on('click',function(){
      if (!$('.button').is(':animated')) {
        $('.button').fadeToggle(150);
      }
      if (!$('#links').is(':animated')) {
            $('#links').toggleClass('links-close',300,'easeInOutSine');
      }
      if (!$('#content').is(':animated')) {
            $('#content').toggleClass('content-open',300,'easeInOutSine');
      }
      });
    // HEADER
    $('.latest').on('click',function(){
      $('#header h1').text('White Wolf Wizard');
      if (!$('#footer').is(':animated')) {
        $('#footer').toggle('puff',150);
      }
    });
    $('#back').on('click',function(){
      $('#header h1').text('Messages');
      if (!$('#footer').is(':animated')) {
        $('#footer').delay(150).toggle('puff',150);
      }
    });
    // DROP
    $('#edit').on('click',function(){
      if (!$('#drop ol').is(':animated')) {
        $('#drop ol').toggle('drop',300);
      }
    });
    // CAMERA
    $('#camera').on('click',function(){
      if (!$('#flash').is(':animated')) {
        $('#flash').toggle('puff',100).toggle('puff',100);
      }
    });
  });