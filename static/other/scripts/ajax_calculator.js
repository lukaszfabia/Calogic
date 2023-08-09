$(document).ready(function() {
        $("#calculator-form").on("submit", function(e) {
            e.preventDefault();
            const userInput = $("#user_input").val();
            $.ajax({
                type: "POST",
                url: "/calculator",
                data: { user_input: userInput },
                success: function(response) {
                    $("#output_result").val(response.output_value);
                }
            });
        });
    });