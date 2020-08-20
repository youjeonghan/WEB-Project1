const board_url = 'http://127.0.0.1:5000/board';
const user_url = '';

paint_board();
console.log(asdf);
// fetch(json_url)
//   .then(function(response) {
//     return response.json();
//   })
//   .then(function(json) {
//   	console.log(JSON.stringify(json));
//   	var text ='';
//     for (var i = 0; i <=json.length-1; i++) {
// 	    var boards_html = 	
// 	    			'<section class="board__lists__item">'+
// 	    			'<h3>'+json[i].subject+'</h3>'+
// 					'<p>'+json[i].content+'</p>' +
// 					'<ul>'+
// 						'<li>'+json[i].id+'</li>'+
// 						'<li>'+json[i].create_date+'</li>'+
// 					'</ul>'+'</section>';
// 		text += boards_html;
//     }

//     document.querySelector('.board__lists').innerHTML = text;
//   });

//통신을 통하여 해당 url 정보를 json화 해서 반환
  function fetch_tojson(url){
    return fetch(url).then(function(response) {
      return response.json();
    });

  }
// 비동기함수 async는 await가 완료될때 까지 대기후 실행, 게시글 조회
  async function paint_board(){
    //user_url변수를 통해 json형식의 user정보를 user변수에 저장
    // const user = await fetch_tojson(user_url);
    //board_url변수를 통해 json형식의 board정보를 boards변수에 저장
    const boards = await fetch_tojson(board_url);
    //게시판 tag 생성
    const text ='';
    for (var i = 0; i <=boards.length-1; i++) {
      const boards_html =   
              '<section class="board__lists__item">'+
              '<h3>'+boards[i].subject+'</h3>'+
            '<p>'+boards[i].content+'</p>' +
            '<ul>'+
              '<li>'+boards[i].id+'</li>'+
              '<li>'+boards[i].create_date+'</li>'+
            '</ul>'+'</section>';
      //로그인한 유저정보 id 값과 게시글 id값이 같으면 수정 or 삭제가능 
      // if(user.id === boards[i]){
      //     //x 버튼과 수정 버튼 구현해서 태그에 저장
      //     boards_html +='tags~';
      // }
      text += boards_html;
    }

    document.querySelector('.board__lists').innerHTML = text;
  }