var WIDTH = screen.width,
  HEIGHT = screen.height;
var number_parts = 36;
var JSON_data;
var isdraw = false;
var objDetails = [];
var myCanvas;

function preload() {
  loadJSON('../../output.json', printData);
}

function setup() {
  var prevRad = 0;
  myCanvas = createCanvas(WIDTH, HEIGHT);
  background(255);
  drawPatterns(1);
}


function drawPatterns(num) {
	for(var i =0;i<num;i++) { //noprotect
    var drawStatus = true;
    objNo = floor(random(0,JSON_data.Data.length));
    stroke(255);
		var rad = redrawJSON(JSON_data.Data[objNo].split(''),true).radius;
		var x = random(10,WIDTH-10);
		var y = random(10,HEIGHT-10);
    for(var j =0;j<objDetails.length;j++){

      drawStatus = drawStatus && checkDist(objDetails[j],x,y,rad);

    }
    // console.log('*****');
    if( drawStatus ) {
      push();
      translate(x,y);
      // console.log(drawStatus);
      objDetails.push({"rad":rad,"x":x, "y":y});
      fill(255);
      // fill(255,244,212);
      // colorMode(HSB);
      // stroke(random(0,360),45,85);
      stroke(0)
      ellipse(0,0,rad*2+10, rad*2+10);
      ellipse(0,0,rad*2, rad*2);

      noFill();
      strokeWeight(0.8);
      redrawJSON(JSON_data.Data[objNo].split(''),false)
      pop();
    }

	}
}


function printData(data) {
  JSON_data = data; //.Data[1].split(',');
}


function redrawJSON(mouse_array, iscalculate) {
  max_mouse_x  = WIDTH / 2 +1;
  max_mouse_y = HEIGHT / 2 +1;
  p_mouse_x = WIDTH / 2 +1;
  p_mouse_y = HEIGHT / 2 +1;
  mouse_x = WIDTH / 2 +1;
  mouse_y = HEIGHT / 2 +1;
  max_rad = 0;
  // mouse_array.unshift('e');
  for (var i = 0; i < mouse_array.length; i++) {

    if (!mouse_array[i].localeCompare('a')) {
      p_mouse_x = mouse_x;
      p_mouse_y = mouse_y;
      mouse_x = p_mouse_x + 0.5;

    } else if (!mouse_array[i].localeCompare('b')) {
      p_mouse_x = mouse_x;
      p_mouse_y = mouse_y;
      mouse_x = p_mouse_x - 0.5;
    } else if (!mouse_array[i].localeCompare('c')) {
      p_mouse_x = mouse_x;
      p_mouse_y = mouse_y;
      mouse_y = p_mouse_y + 0.5;
    } else if (!mouse_array[i].localeCompare('d')) {
      p_mouse_x = mouse_x;
      p_mouse_y = mouse_y;
      mouse_y = p_mouse_y - 0.5;
    } else if (!mouse_array[i].localeCompare('f')) {
      isdraw = false;
    } else if (!mouse_array[i].localeCompare('e')) {
      isdraw = true;
    } else if (!mouse_array[i].localeCompare('z')) {
      number_parts = 4;
    } else if (!mouse_array[i].localeCompare('y')) {
      number_parts = 8;
    } else if (!mouse_array[i].localeCompare('x')) {
      number_parts = 36;
    } else if (!mouse_array[i].localeCompare('w')) {
      number_parts = 72;
    }


    // translate(WIDTH / 2, HEIGHT / 2);
    if (isdraw) {
      for (var j = 0; j < number_parts; j++) {
        angleMode(DEGREES);
        rotate(360 / number_parts);


        if(!iscalculate){
          line(p_mouse_x - WIDTH / 2, p_mouse_y - HEIGHT / 2, mouse_x - WIDTH / 2, mouse_y - HEIGHT / 2);
          line(p_mouse_x - WIDTH / 2, HEIGHT - p_mouse_y - HEIGHT / 2, mouse_x - WIDTH / 2, HEIGHT - mouse_y - HEIGHT / 2);

        }
        var rad = sqrt((mouse_y- HEIGHT / 2)*(mouse_y- HEIGHT / 2) + (mouse_x- WIDTH / 2)*(mouse_x- WIDTH / 2));
        if( rad > max_rad) {
          max_rad = rad;
        }
      }
    } else {
    }
  }
  // console.log(max_rad);

  return ({
    radius : max_rad
  });

}

function checkDist(tempObj,x,y,rad) {
  var status = false;
  var dist = sqrt((tempObj.x - x)*(tempObj.x - x)+(tempObj.y - y)*(tempObj.y - y));
  // console.log(dist);
  if( dist > (rad + tempObj.rad )*0.55 )
  {
    // console.log('true');
    status = true;
  }
  return status;
}

function keyPressed() {

  if (keyCode === RIGHT_ARROW) {
    console.log('saving');
    saveCanvas(myCanvas, 'output', 'jpg');
  }
}
