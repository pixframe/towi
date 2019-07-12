$(document).ready(function () {
    $("#towiCalendar").zabuto_calendar({
      cell_border: true,
      today: true,
      weekstartson: 0,
      language: "es",
      legend: [
        {type: "block", label: "Completó el entrenamiento", classname: "evento-progreso"}
      ],
      nav_icon: {
        prev: '<i class="fa fa-chevron-left"></i>',
        next: '<i class="fa fa-chevron-right"></i>'
      }
    });
});
