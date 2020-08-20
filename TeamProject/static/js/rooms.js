const board_url = 'http://127.0.0.1:5000/board';

//init function
init();

function init(){
  load_board();
  hide_input();
}

///////////////////조회 ///////////////
//통신을 통하여 해당 url 정보를 json화 해서 반환
function fetch_tojson(){
  return fetch(board_url).then(function(response) {
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
  '<section class="board__lists__item" onclick = "board_big()">'+
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
      const boards = await fetch_tojson();
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

///////////////////입력 ///////////////

function fetch_insert(data){
  return fetch(board_url,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(data)
  }).then(function(response) {
    if(response.ok){
      return response.json();
    }
    else{
      alert("HTTP-ERROR: " + response.status);
    }
  });

}
function input_board(){
// 입력후 페인트함수 호출 , 내용 추출객체 반환 
  const input_subject = document.querySelector('.input__subject');
  const input_content = document.querySelector('.input__article');
  
  let object = {
    subject : input_subject.value,
    content : input_content.value
  };
  input_subject.value = "";
  input_content.value = "";
  return object;
}


//입력창 만들기//
function paint_input(){
  const html = '<div class="input__on"><input type="text" placeholder="제목을 입력하세요" class="input__subject">' +
      '<textarea name="article" class="input__article" placeholder="내용을 입력하세요"></textarea>' +
      '<input type="button" class="input__button" onclick="input__click();" value="글쓰기" /> </div>'
  document.querySelector('.Board__input').innerHTML = html;
}
//입력창 숨기기//
function hide_input(){
  const html ='<div class = "input__off"><textarea placeholder="게시글을 작성해보세요" onclick="paint_input()"></textarea></div>';
  document.querySelector('.Board__input').innerHTML = html;
}

//버튼 이벤트 헨들러
async function input__click(){
  const data = input_board();
  await fetch_insert(data);
  init();
}

//보드 확대
function board_big(){
  console.log("AsdfdF");
}