document.addEventListener("DOMContentLoaded", function() {
    // Initialize the chart
    const ctx = document.getElementById('expensesChart').getContext('2d');
    const expensesChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Amount Spent', 'Account Balance'],
            datasets: [{
                label: 'Expenses',
                data: [60.8, 39.2],
                backgroundColor: ['#ff6384', '#36a2eb'],
                hoverBackgroundColor: ['#ff6384', '#36a2eb']
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    // Handle frequency change
    document.querySelectorAll('input[name="frequency"]').forEach((elem) => {
        elem.addEventListener("change", function(event) {
            let value = event.target.value;
            // Update chart data based on the selected frequency
            updateChartData(expensesChart, value);
        });
    });
});

// Dummy function to update chart data based on frequency
function updateChartData(chart, frequency) {
    if (frequency === 'daily') {
        chart.data.datasets[0].data = [10, 90]; // Example values
    } else if (frequency === 'weekly') {
        chart.data.datasets[0].data = [30, 70]; // Example values
    } else if (frequency === 'monthly') {
        chart.data.datasets[0].data = [60.8, 39.2]; // Example values
    }
    chart.update();
}