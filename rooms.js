var json_url = 'http://localhost/ex.json?ver=1';
fetch(json_url)
  .then(function(response) {
    return response.json();
  })
  .then(function(json) {
  	// console.log(JSON.stringify(json));
  	var text ='';
    for (var i = 0; i <=json.length-1; i++) {
	    var boards_html = 	
	    			'<section class="board__lists__item">'+
	    			'<h3>'+json[i].subject+'</h3>'+
					'<p>'+json[i].content+'</p>' +
					'<ul>'+
						'<li>'+json[i].id+'</li>'+
						'<li>'+json[i].create_date+'</li>'+
					'</ul>'+'</section>';
		text += boards_html;
    }
    console.log(text);
    document.querySelector('.board__lists').innerHTML = text;
  });