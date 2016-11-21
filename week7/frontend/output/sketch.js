var WIDTH = 1000,
  HEIGHT = 500;
var number_parts = 36;
var JSON_data;
var isdraw = false;


function preload() {
  loadJSON('../../output.json', printData);
}

function setup() {
  createCanvas(WIDTH, HEIGHT);

  colorMode(HSB);
  i = 0;
}


function printData(data) {
  JSON_data = data; //.Data[1].split(',');
}

function draw() {
  // print(frameCount);
  if (frameCount < JSON_data.Data.length) {
    background(0);
    draw_radial();
    redrawJSON(JSON_data.Data[i].split(','));
  }
  i = i + 1;
}

function draw_radial() {

  translate(WIDTH / 2, HEIGHT / 2);

  // ellipse(0,0,20,20);
  strokeWeight(0.5);
  for (var i = 0; i < number_parts; i++) {
    angleMode(DEGREES);
    rotate(360 / number_parts);
    stroke(200);
    line(0, 0, WIDTH / 2, HEIGHT / 2);
  }
}

function redrawJSON(mouse_array) {
  p_mouse_x = 0;
  p_mouse_y = 0;
  mouse_x = 200;
  mouse_y = 200;
  for (var i = 0; i < mouse_array.length; i++) {

    if (!mouse_array[i].localeCompare('a')) {
      console.log(mouse_array[i]);
      p_mouse_x = mouse_x;
      p_mouse_y = mouse_y;
      mouse_x = p_mouse_x + 1;

    } else if (!mouse_array[i].localeCompare('b')) {
      p_mouse_x = mouse_x;
      p_mouse_y = mouse_y;
      mouse_x = p_mouse_x - 1;
    } else if (!mouse_array[i].localeCompare('c')) {
      p_mouse_x = mouse_x;
      p_mouse_y = mouse_y;
      mouse_y = p_mouse_y - 1;
    } else if (!mouse_array[i].localeCompare('d')) {
      p_mouse_x = mouse_x;
      p_mouse_y = mouse_y;
      mouse_y = p_mouse_y - 1;
    } else if (!mouse_array[i].localeCompare('f')) {
      isdraw = false;
    } else if (!mouse_array[i].localeCompare('e')) {
      isdraw = true;
    }


    // translate(WIDTH / 2, HEIGHT / 2);
    colorMode(HSB);
    if (isdraw) {
      for (var j = 0; j < number_parts; j++) {
        angleMode(DEGREES);
        rotate(360 / number_parts);
        stroke(0, 60, 80);
        noFill();
        strokeWeight(2);
        line(p_mouse_x - WIDTH / 2, p_mouse_y - HEIGHT / 2, mouse_x - WIDTH / 2, mouse_y - HEIGHT / 2);
        line(p_mouse_x - WIDTH / 2, HEIGHT - p_mouse_y - HEIGHT / 2, mouse_x - WIDTH / 2, HEIGHT - mouse_y - HEIGHT / 2);
      }
    }
  }

}
