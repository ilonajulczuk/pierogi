$(document).ready(function() {
    var pierogi_table = $('#pierogi_table')
    pierogi_table.DataTable();
    var obj = undefined
    var jsonData = '[{"name": "Pierog", "location": "ZnanyLekarz","date": "28/11/2015"}, {"name": "Pierog", "location": "ZnanyLekarz","date": "28/11/2015"},{"name": "Pierog", "location": "ZnanyLekarz","date": "28/11/2015"}]';

    $.ajax({
      type: 'GET',
      url: 'http://172.27.133.4:8000/food/',
      headers: {
          'Authorization': 'Token 7a6749b6725072b41050b004e0ca6d126ac025e8'
      },
      xhrFields: {
          withCredentials: true
      },
      success: function(data) {
          console.log('success');
      obj = data.results;

    $.each(obj, function(index, data_object) {
        $("#pierogi_table > tbody").append(generate_row(data_object));
    });

      },
      error: function() {
          console.log('failure');
      }
    });



} );


var generate_row = function(data_object) {
    return  "<tr><td>" + data_object.name + "</td><td>" + data_object.giver + "</td><td><center><img height='100' width='100' src='" + data_object.image + "'></center></td><td>" + generate_button(data_object) +  "</td></tr>"  
};
var generate_button = function(data_object) {
if(!data_object.taker)
    {
return "<button type='button' class='btn btn-default' aria-label='Left Align' onclick='zbierz("+ data_object.id + ")'>ZBIERZ PIEROGA</button>"
    }
    else
        return ''
}

var zbierz = function (id) {
    $.ajax({
      type: 'GET',
      url: 'http://172.27.133.4:8000/food/'+id+'/claim/',
      headers: {
          'Authorization': 'Token 7a6749b6725072b41050b004e0ca6d126ac025e8'
      },
      xhrFields: {
          withCredentials: true
      },
      success: function(data) {
          console.log('zakosiles pierogsa');
      },
      error: function() {
          console.log('failure');
      }
    });

}
