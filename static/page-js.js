var obj = {tasks: ['get milk', 'drink milk'], deadlines: ['20/10/2010', '10/11/2020']};


$(document).ready(function(){
    for(i = 0; i < obj.tasks.length; i++){
        code = "<li class='list-group-item task'><input type='checkbox' class='task-done'> " + obj.tasks[i] + " <span class='date'>Deadline: " + obj.deadlines[i] + "</span></li>";
        $('#task-section').append(code);
    }

    
    $('.task-done').click(function(){
        $(this).parent().fadeOut("slow");
    });

    $('#new-task-button').click(function(){
        $('#new-task-input').toggle();
    });
    
    $('#new-team-button').click(function(){
        $('#new-team-input').toggle();
    });

    //to get data from form submissions

    $('#new-task-input').submit(function(){
        var formData = new FormData($(this)[0]); 
        console.log(formData);
    });


    var num = obj.tasks.length;
    $('#my-tasks').append(' (' + num + ')');
    
    $('input').click(function(){
        return false;
    });
    
});
