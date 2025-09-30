/* globals Chart:false */

// () => { } :이름 없는 즉시 실행 함수
(() => {
  'use strict'

  // Graphs
  // 문서(html) 안에 있는 ID가 myChart인 태그를 선택하여 ctx 변수에 저장
  const ctx = document.getElementById('myChart')
  // ctx에 그래프를 그려준다.
  new Chart(ctx, {
    // type: 어떤 그래프를 그릴 것인가?
    type: 'bar',
    data: {
      // labels: x축의 데이터를 대입
      labels: {{x | tojson}},
      // datasets: y축의 데이터를 대입 (복수 대입 가능)
      datasets: [{
        // data: 실제 y축 데이터
        data: {{y | tojson}},
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          boxPadding: 3
        }
      }
    }
  })
})()
