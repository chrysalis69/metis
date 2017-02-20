function align_cell_right(td, cellData, rowData, row, col){
	        $(td).css('text-align', 'right');
}
function render_to_fixed_2(data, type, full, meta){
	return data.toFixed(2);
}
function render_to_fixed_0(data, type, full, meta){
	return data.toFixed(0);
}
function render_date(data, type, full, meta){
	date = new Date(data);
	return date.toLocaleString();
}

function render_seconds(data, type, full, meta){
	var seconds = parseInt(data%60),
	    minutes = parseInt((data/60)%60),
	    hours = parseInt((data/(60*60))%60);
	hours = (hours < 10)?"0"+hours:hours;
	minutes = (minutes < 10)?"0"+minutes:minutes;
	seconds = (seconds < 10)?"0"+seconds:seconds;
	return hours+":"+minutes+":"+seconds;
}

function draw_pie(domID, label, used, max){
	var pie = new d3pie(domID,{
		header: {
			title: {
				text: label
			},
			subtitle: {
				text: used + " of " + max
			}
		},
		size: {
			canvasHeight: 250,
			canvasWidth: 250,
			pieInnerRadius: "50%",
			pieOuterRadius: "90%"
		},
		data: {
			content:[{
				value: used,
				color: (used/max < 0.75)?'#0066ff':(used/max < 0.9)?'#ff8000':'#ff4000'
			},{
				value: (max - used),
				color: '#808080'
			}]
		},
		labels: {
			outer: {
				format: "none"
			},
			inner: {
				format: "none"
			}
		}
	});
	return pie;
}
