const board_url = 'http://127.0.0.1:5000/board';

//init function
load_board();

//통신을 통하여 해당 url 정보를 json화 해서 반환
function fetch_tojson(url){
  return fetch(url).then(function(response) {
    if(response.ok){
      return response.json();
    }
    else{
      alert("HTTP-ERROR: " + response.status);
    }
  });

}

//게시판 글 태그 만들기 
function paint_board(board){
  const board_html =   
  '<section class="board__lists__item">'+
  '<h3>'+board.subject+'</h3>'+
  '<p>'+board.content+'</p>' +
  '<ul>'+
  '<li>'+board.id+'</li>'+
  '<li>'+board.create_date+'</li>'+
  '</ul>'+'</section>'; 
  return board_html;
}

// 게시글 조회, 비동기함수 async는 await가 완료될때 까지 대기후 실행
async function load_board(){
    //board_url변수를 통해 json형식의 board정보를 boards변수에 저장
    try{
      const boards = await fetch_tojson(board_url);
      //게시판 tag 생성
      let text ='';
      for (var i = boards.length-1; i >=0; i--) {
        text += paint_board(boards[i]);
      }
      document.querySelector('.board__lists').innerHTML = text;
    } catch(error){
      console.log(error);
    }

  }


function input_board(){
// 입력창 박스를 만들고 , 엔터치면 이벤트헨들러로 데이터 전송, 페인트 함수 호출 

}