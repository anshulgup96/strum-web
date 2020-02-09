$(document).ready(function(){
    
    $("#signup-button").click(function(){
        var new_user = {
            "username": $('#signup-email').val(),
            "password": $('#signup-password').val(),
        };
        
        $.ajax({
            type: 'GET',
            url: 'https://strum-task-manager.herokuapp.com/api/users',
            success: function(data){
                console.log(data);
            }
        });
        return false;
        
    });
        /*
        console.log('hello world');
        var new_user = {
            "username": $('#signup-email').val(),
            "password": $('#signup-password').val(),
        };

        $.ajax({
            type: 'POST',
            url: 'text.txt',
            data: new_user,
            success: function(data){
                console.log(data);
            }
        });
        
    });
    
*/
});




//.ajax to send a request

//.each(data, function(i, order)) to run a function for each item in some data



/*
$.ajax({
  type: "POST",
  beforeSend: function(request) {
    request.setRequestHeader("Authority", authorizationToken);
  },
  url: "entities",
  data: "json=" + escape(JSON.stringify(createRequestObject)),
  processData: false,
  success: function(msg) {
    $("#results").append("The result =" + StringifyPretty(msg));
  }
});

*/