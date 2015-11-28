
$(document).ready(function() {
    var pierogi_table = $('#pierogi_table')
    pierogi_table.DataTable();

    var jsonData = '[{"name": "Pierog", "location": "ZnanyLekarz","date": "28/11/2015"}, {"name": "Pierog", "location": "ZnanyLekarz","date": "28/11/2015"},{"name": "Pierog", "location": "ZnanyLekarz","date": "28/11/2015"}]';

    var obj = JSON.parse(jsonData);
    $.each(obj, function(index, data_object) {
        console.log(generate_row(data_object));
        $("#pierogi_table > tbody").append(generate_row(data_object));
    });


} );


var generate_row = function(data_object) {
    return  "<tr><td>" + data_object.name + "</td><td>" + data_object.location + "</td><td>" + data_object.date + "</td></tr>"
};
