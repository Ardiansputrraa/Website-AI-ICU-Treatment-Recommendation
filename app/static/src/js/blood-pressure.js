function fetchBloodPressureData(bed_id) {
  setInterval(() => {
    $.ajax({
      url: `/get-blood-pressure-data/${bed_id}`,
      method: "GET",
      success: function (response) {
        document.getElementById(
          "blood-pressure-value"
        ).innerText = `${response.systolic}/${response.diastolic}`;
        document.getElementById(
          "temperature-value"
        ).innerText = `${response.temperature}`;
      },
      error: function () {
        console.error("Gagal mengambil data tekanan darah");
      },
    });
  }, 1000); // Interval 1 detik
}
