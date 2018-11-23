jQuery(document).ready(function() {

    $('.ajax_save_product').submit(function(event) {
        event.preventDefault();
        var form = $(this);

        $.ajax({
          type: "POST",
          cache: false,
          data:form.serialize(),
          url: "{% url search:save %}",
          dataType: "json",
          beforeSend: function(xhr) {
          },
          success: function(data) {
            console.log(data.validation);
            console.log('success');
            if (data.validation === "save products") {
              console.log('pass');
              $('#btn_sauv').addClass("<button class='btn btn-success'>" + "Sauvegardé" + "</button>");
            }
            else if (data.validation === "delete products") {
              $('#btn_sauv').removeClass("<button class='btn btn-success'>" + "Sauvegardé" + "</button>");
              console.log('fail');
            }
          },
          error: function(data) {
            alert("error: " + data.status + " : erreur dans l'application, veuillez effectuer une nouvelle recherche");
            }
        });
    });
});
