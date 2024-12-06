function initializeChart() {
    const heartRateCtx = document.getElementById("heartRate").getContext("2d");
    const oxygenSaturationCtx = document.getElementById("oxygenSaturation").getContext("2d");
    const respiratoryRateCtx = document.getElementById("respiratoryRate").getContext("2d");

    const heartRateChart = new Chart(heartRateCtx, {
        type: "line",
        data: {
            labels: Array.from({ length: 100 }, () => ""),
            datasets: [
                {
                    borderColor: "#9933FF",
                    borderWidth: 2,
                    fill: false,
                    tension: 0.4,
                    data: Array.from({ length: 100 }, () => 75),
                },
            ],
        },
        options: {
            responsive: true,
            animation: false,
            plugins: { legend: { display: false } },
            scales: { x: { display: false }, y: { display: false } },
            elements: { point: { radius: 0 } },
        },
    });

    const oxygenSaturationChart = new Chart(oxygenSaturationCtx, {
        type: "line",
        data: {
            labels: Array.from({ length: 100 }, () => ""),
            datasets: [
                {
                    borderColor: "#9933FF",
                    borderWidth: 2,
                    fill: false,
                    tension: 0.4,
                    data: Array.from({ length: 100 }, () => 98),
                },
            ],
        },
        options: {
            responsive: true,
            animation: false,
            plugins: { legend: { display: false } },
            scales: { x: { display: false }, y: { display: false } },
            elements: { point: { radius: 0 } },
        },
    });

    const respiratoryRateChart = new Chart(respiratoryRateCtx, {
        type: "line",
        data: {
            labels: Array.from({ length: 100 }, () => ""),
            datasets: [
                {
                    borderColor: "#9933FF",
                    borderWidth: 2,
                    fill: false,
                    tension: 0.4,
                    data: Array.from({ length: 100 }, () => 20),
                },
            ],
        },
        options: {
            responsive: true,
            animation: false,
            plugins: { legend: { display: false } },
            scales: { x: { display: false }, y: { display: false } },
            elements: { point: { radius: 0 } },
        },
    });

    return { heartRateChart, oxygenSaturationChart, respiratoryRateChart };
}

function updateCharts(charts, vitalData) {
    // Update Heart Rate
    charts.heartRateChart.data.datasets[0].data.push(vitalData.heart_rate || 75);
    if (charts.heartRateChart.data.datasets[0].data.length > 100) {
        charts.heartRateChart.data.datasets[0].data.shift();
    }
    charts.heartRateChart.update();

    // Update Oxygen Saturation
    charts.oxygenSaturationChart.data.datasets[0].data.push(vitalData.oxygen_saturation || 98);
    if (charts.oxygenSaturationChart.data.datasets[0].data.length > 100) {
        charts.oxygenSaturationChart.data.datasets[0].data.shift();
    }
    charts.oxygenSaturationChart.update();

    // Update Respiratory Rate
    charts.respiratoryRateChart.data.datasets[0].data.push(vitalData.respiratory_rate || 20);
    if (charts.respiratoryRateChart.data.datasets[0].data.length > 100) {
        charts.respiratoryRateChart.data.datasets[0].data.shift();
    }
    charts.respiratoryRateChart.update();
}

function fetchVitalData(bed_id) {
    const charts = initializeChart();

    setInterval(() => {
        $.ajax({
            url: `/get-vital-data/{{bed_id}}`,
            method: "GET",
            success: function (response) {
                const vitalData = response;
                console.log(vitalData)
                updateCharts(charts, vitalData);

                document.getElementById("heart-rate-value").innerText = Math.round(vitalData.heart_rate || 75);
                document.getElementById("oxygen-saturation-value").innerText = Math.round(vitalData.oxygen_saturation || 98);
                document.getElementById("respiratory-rate-value").innerText = Math.round(vitalData.respiratory_rate || 20);
            },
            error: function () {
                console.error("Gagal mengambil data vital");
            },
        });
    }, 1000); // Interval 1 detik
}
