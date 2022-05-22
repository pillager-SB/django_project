window.onload = function() {
    $('.basket_list').on('click', 'input[type="number"]', function(event) {
        var input_element = event.target;
        $.ajax({
            url: "/basket/edit/" + input_element.name + "/" + input_element.value + "/",
            success: function(data) {
                $('.basket_list').html(data);
            },
        });
        event.preventDefault();
    });
}