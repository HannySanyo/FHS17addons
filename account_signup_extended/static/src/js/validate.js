
// This is a javascript to validate the birtday example. We may want to write a script to validate whether they inputted a calid
// phone number or something here eventually. But it's not needed for this to work rn.

// This script should not be referenced as of right now.

$(document).ready(function () {
   
var dtToday = new Date();
  var month = dtToday.getMonth() + 1;     
  var day = dtToday.getDate();
  var year = dtToday.getFullYear();
  if(month < 10){
      month = '0' + month.toString();
  }
  if(day < 10){
      day = '0' + day.toString();
  }

  var maxDate = year + '-' + month + '-' + day;
  $('#birthday').attr('max', maxDate);
});
