$(document).ready(onload);
function onload() {
    var $button = $('#btn');
    function draw_graph(from, to, step, fun_str, canvas) {
        var array_of_dots = [];
        var x = from;
        var refreshInterval = setInterval(function () {
                var dot = [x, eval(fun_str)];
                array_of_dots.push(dot);
                $.plot(canvas, [
                        {
                            label: fun_str,
                            data: array_of_dots
                        }
                    ], {
                        series: {
                            lines: {show: true},
                            points: {show: false}
                        },
                        xaxis: {
                            min: from,
                            max: to,
                            ticks: 20
                        },
                        yaxis: {
                            ticks: 10,
                            tickDecimals: 2
                        }
                    }
                );
                x = x + step;
                if (x > to) clearInterval(refreshInterval);
            },100);
        console.log("end of drawing");
    }

    $button.click(function (e) {
        e.preventDefault();
        var from_val = parseFloat($('#from').val());
        var to_val = parseFloat($('#to').val());
        var fun_str = $('#fun').val();
        var $canvas = $("#plot_canvas");
        var step_val = parseFloat($('#step').val());
        draw_graph(from_val, to_val, step_val, fun_str, $canvas);
    });
}

