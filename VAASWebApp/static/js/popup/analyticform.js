function loadForm(){
    var selectedOption=$('#selection_type').val();
    $.ajax({
        url: '/get_analyticform/',
        type:'GET',
        data:{option:selectedOption},
        success:function(response){
            $('#analyticForm').html(response);
        }
    })
}