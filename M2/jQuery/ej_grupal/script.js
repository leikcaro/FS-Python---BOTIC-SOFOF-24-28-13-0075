
$(document).ready(function() {
  let modal = new bootstrap.Modal(document.getElementById('reservaModal'));

  $('.reservar').click(function() {
    let titulo = $(this).data('title');
    $('#pelicula').val(titulo);
    $('#confirmacion').hide();
    $('#formReserva')[0].reset();
    $('#pelicula').val(titulo);
    modal.show();
  });

  $('#formReserva').submit(function(e) {
    e.preventDefault();
    let pelicula = $('#pelicula').val();
    let horario = $('#horario').val();
    let asientos = $('#asientos').val();
    let pago = $('#pago').val();

    $('#confirmacion').html(`Reserva confirmada para <strong>${pelicula}</strong> a las <strong>${horario}</strong>. Asientos: <strong>${asientos}</strong>. Pago: <strong>${pago}</strong>.`).fadeIn();
  });
});
