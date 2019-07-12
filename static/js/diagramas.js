// Diagrama de linea
  var ctx = document.getElementById("indiceChart");
  var myChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: ["Taxi Aeropuerto - Choques", "Taxi Aeropuerto - Sin Salida", "Taxi Aeropuerto - Cruces", "Sala de Espera - Correcta", "Empacar - Progresión", "Empacar - Regresión", "Sala de Espera - Omisiones**", "Jarron de Monedas - Correctas", "Jarron de Monedas - Tiempo", "Jarron de Monedas - Omisiones**", "Taxi Aeropuerto - Tiempo", "Taxi Aeropuerto - Latencia", "Jarron de Monedas - Tiempo", "Desempacar - Recuerdo de Objetos", "Acomodar Cuarto - Correcto", "Empacar - Progresión", "Empacar - Regresión", "Sala de Espera - Incorrecto**"],
          datasets: [{
            label: "1era prueba",
            fill: false,
            backgroundColor: "rgba(18,132,136,0.4)",
            borderColor: "rgba(18,132,136,1)",
            pointBorderColor: "#fff",
            pointBackgroundColor: "rgba(18,132,136,1)",
            pointHoverBackgroundColor: "rgba(18,132,136,1)",
            pointHoverBorderColor: "rgba(220,220,220,0.2)",
            pointRadius: 3,
            data: [10, 16, 8, 10, 5, 9, 12, 17, 15, 14, 12, 5, 8, 1, 19, 3, 15, 10],
          }]
      }
  });

// Diagrama de barras
  var ctx = document.getElementById("barChart");
  var barChart = new Chart(ctx, {
      type: 'horizontalBar',
      data: {
          labels: ["Planeación", "Atencional", "Atención Selectiva", "Velocidad de Procesamiento", "Mnésico"],
          datasets: [{
              label: "PROMEDIO ESCALARES",
              backgroundColor: [
                'rgba(250, 185, 35, 0.5)',
                'rgba(116, 210, 100, 0.5)',
                'rgba(255, 110, 5, 0.5)',
                'rgba(0, 175, 235, 0.5)',
                'rgba(218, 8, 150, 0.5)'
              ],
              borderColor: [
                'rgba(250, 185, 35, 1)',
                'rgba(116, 210, 100, 1)',
                'rgba(255, 110, 5, 1)',
                'rgba(0, 175, 235, 1)',
                'rgba(218, 8, 150, 1)'
              ],
              borderWidth: 1,
              data: [10, 9, 15, 8, 8, 0]
          }]
        }
  });

// Diagrama de radar
  var ctx = document.getElementById("habilidadChart");
  var habilidadChart = new Chart(ctx, {
      type: 'radar',
      data: {
          labels: ["Atención", "Memoria", "Funciones Ejecutivas", "Velocidad de Procesamiento", "Automonitoreo y Verificación"],
          datasets: [{
              label: "Habilidades",
              backgroundColor: "rgba(255, 110, 5, 0.2)",
              borderColor: "rgba(255, 110, 5, 1)",
              pointBackgroundColor: "rgba(255, 110, 5, 1)",
              pointBorderColor: "#fff",
              pointHoverBackgroundColor: "#fff",
              pointHoverBorderColor: "rgba(255, 110, 5, 1)",
              data: [8, 10, 9, 7, 5]
          }]
        }
  });

// Diagrama de radar
  var ctx = document.getElementById("desHabilidadesChart");
  var desHabilidadChart = new Chart(ctx, {
      type: 'radar',
      data: {
          labels: ["Atención M-Progresión", "Atención SE-Detección Correcta", "Atención JM-Recolección Correcta", "Memoria D-Recuerdo Correcta", "Memoria AC-Tot-Correcta", "Funciones Ejecutivas M-Regresión", "Funciones Ejecutivas TA-Tot-Sin Salida", "Funciones Ejecutivas TA-Tot_Tiempo", "Funciones Ejecutivas C-Cabina Correcta", "Funciones Ejecutivas TA-Tot-Choques", "Funciones Ejecutivas TA-Tot-Cruces", "Funciones Ejecutivas TA-Tot-Latencia" ],
          datasets: [{
              label: "Habilidades",
              backgroundColor: "rgba(116, 210, 100, 0.2)",
              borderColor: "rgba(116, 210, 100, 1)",
              pointBackgroundColor: "rgba(116, 210, 100, 1)",
              pointBorderColor: "#fff",
              pointHoverBackgroundColor: "#fff",
              pointHoverBorderColor: "rgba(116, 210, 100, 1)",
              data: [10, 9, 4, 9, 11, 15, 10, 10, 5, 6, 3, 9]
          }]
        }
  });

// Diagrama de pastel
  var ctx = document.getElementById("pieChart");
  var pieChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels: ["Nunca", "Algunas veces", "Casi siempre"],
          datasets: [{
              backgroundColor: [
                "rgba(0, 175, 235, 0.2)",
                "rgba(250, 185, 35, 0.2)",
                "rgba(116, 210, 100, 0.2)"
              ],
              borderColor: [
                "rgba(0, 175, 235, 1)",
                "rgba(250, 185, 35, 1)",
                "rgba(116, 210, 100, 1)"
              ],
              data: [180, 120, 50]
          }]
        }
  });
