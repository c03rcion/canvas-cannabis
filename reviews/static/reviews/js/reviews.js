$(function () {
  $(".strain-review").click(function () {
    let url = $(this).data('url')
    $.ajax({
      url: url,
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-review").modal("show");
      },
      success: function (data) {
        $("#modal-review .modal-content").html(data.html_form);
        console.log(data)
      }
    });
  });
});

$("#modal-review").on("submit", ".review-create-form", function () {
    let form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function(data) {
        if(data.form_is_valid) {
          $("#modal-review").modal("hide");
        } else {
          $("#modal-review .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });
