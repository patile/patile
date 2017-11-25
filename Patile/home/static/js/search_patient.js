$("#search_form").on("click", function (event) {
    event.preventDefault();
    var form = $(this);
    var csrf = form.find("input[name='csrfmiddlewaretoken']").val();
    var patient_id = form.find("input[name='patient_id']").val();
    var url = window.location.protocol + "//" + window.location.host + "/set-category";
    $.ajax({
        type: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken: csrf,
            patient_id: patient_id
        },
        success: function (data) {
            if (data) {

            }
        }
    });
});