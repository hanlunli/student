---
layout: default
title: Hanlun's Blog
---
<style>
 p{font-family: sans-serif;}
  hr{background-color: #7e92d6;}
  .color{color:#7e92d6;}
  body {
    padding: 25px;
    background-color: #282b30;
    color: #7e92d6;
    transition-duration: 0.2s;
  }
  hr{background-color: #7e92d6;}
  .board {
      display: grid;
      grid-template-columns: repeat(3, 100px);
      grid-gap: 2px;
    }
         .cell {
      width: 100px;
      height: 100px;
      border: 1px solid #7e92d6;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      cursor: pointer;
</style>


<script>

var IsLoggedIn1 = "true";
function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-mode");
  var elem = document.querySelectorAll("#border");
  elem.forEach(function(border) {
    border.classList.toggle("border-dark");
    });
  var bars = document.querySelectorAll("#bar");
  bars.forEach(function(bar) {
    bar.classList.toggle("bar-dark");
    });
  var cellz = document.querySelectorAll("#cells");
  cellz.forEach(function(cells) {
    cells.classList.toggle("cell");
    cells.classList.toggle("cells-dark");
    });
}
</script>


<p style="font-size:40px;font-weight:bold;"> Hanlun's Blog </p>
<hr id="bar">
<p>This is my freeform picture, containing details on my life:</p>

<img id="border" src = "{{site.baseurl}}/images/freeform.png">
<hr id="bar">

<iframe width="560" height="315" src="https://www.youtube.com/embed/tdCN5ZP8Kfs?si=9odSQ-QoAPcgwqNl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<br />