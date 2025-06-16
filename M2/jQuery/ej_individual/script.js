$(document).ready(function() {
  const images = $(".thumb").toArray();
  let currentIndex = 0;

  function showModal(index) {
    const imgSrc = $(images[index]).attr("src");
    $("#modal-img").attr("src", imgSrc);
    $("#modal").fadeIn();
    currentIndex = index;
  }

  $(".thumb").click(function() {
    const index = parseInt($(this).data("index"));
    showModal(index);
  });

  $(".close, #modal").click(function(e) {
    if (e.target.id === "modal" || e.target.className === "close") {
      $("#modal").fadeOut();
    }
  });

  $("#next").click(function(e) {
    e.stopPropagation();
    currentIndex = (currentIndex + 1) % images.length;
    showModal(currentIndex);
  });

// construya el para el siguiente botón
});
