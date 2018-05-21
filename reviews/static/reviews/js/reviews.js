$(function () {

  $(".strain-review").click(function () {
    console.log('hello')
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
