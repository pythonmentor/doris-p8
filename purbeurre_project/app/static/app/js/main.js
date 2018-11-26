jQuery(document).ready(function() {

    $('.ajax_save_product').submit(function(event) {
        event.preventDefault();
        var form = $(this);
        var btn_save = $(this).find('.btn_save');
        console.log(btn_save);


        $.ajax({
          type: "POST",
          cache: false,
          data:form.serialize(),
          url: "/search/record_favorite",
          dataType: "json",
          success: function(data) {
            console.log('success');
            if (data.validation === "save") {
                btn_save.removeClass("btn-primary").addClass("btn-success");
                btn_save.html('Sauvegardé !');
                $.notify("Et un produit sain sauvegardé ! Continuez, vous êtes sur la bonne voie", "success"
                );
                console.log('saved');
            }

            else if (data.validation === "exists") {
                $.notify("Vous avez déjà sauvegardé ce produit. Quel succès !", "error"
                );
                console.log('exists');
            }

          },
          error: function(data) {
            alert("error: " + data.status + " : erreur dans l'application, veuillez effectuer une nouvelle recherche");
            }
        });
    });

    $('.ajax_delete_product').submit(function(event) {
        event.preventDefault();
        var form = $(this);
        var btn_delete = $(this).find('.btn_delete');
        console.log(btn_delete);


        $.ajax({
          type: "POST",
          cache: false,
          data:form.serialize(),
          url: "/search/remove_favorite",
          dataType: "json",
          success: function(data) {
            console.log('success');
            if (data.validation === "delete") {
              $.notify("Produit supprimé avec succès ! Ne soyez pas triste, vous trouverez votre bonheur", "success"
              );
              console.log('deleted');
              setTimeout(function(){
                location.reload();
              }, 1000);
            }
          },
          error: function(data) {
            alert("error: " + data.status + " : erreur dans l'application, veuillez effectuer une nouvelle recherche");
            }
        });
    });
});
