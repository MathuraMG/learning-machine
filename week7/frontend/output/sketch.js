var WIDTH = screen.width,
  HEIGHT = screen.height;
var number_parts = 36;
var JSON_data;
var isdraw = false;


function preload() {
  loadJSON('../../output.json', printData);
}

function setup() {
  var prevRad = 0;
  createCanvas(WIDTH, HEIGHT);

  // colorMode(HSB);
  i = 0;

   translate(10, 20);
  for(i = 0;i<JSON_data.Data.length;i++) {
  // for(i = 0;i<1;i++) {

    push();
    translate(random(10,WIDTH-10),random(10,HEIGHT-10));
    // translate(floor(i/2)*400,i%2*400)
    var radius = redrawJSON(JSON_data.Data[i].split('')).radius;
    prevRad = radius;
    fill(255);
    stroke(0);
    strokeWeight(2);

    ellipse(0,0,radius*2+20, radius*2+20);
    ellipse(0,0,radius*2, radius*2);
    redrawJSON(JSON_data.Data[i].split(''))
    pop();
    console.log('drew - ' + i + ' - out of - ' + JSON_data.Data.length );
  }
console.log('finishing up..');
}


function printData(data) {
  JSON_data = data; //.Data[1].split(',');
}

function draw() {
}

function redrawJSON(mouse_array) {
  max_mouse_x  = WIDTH / 2 +1;
  max_mouse_y = HEIGHT / 2 +1;
  p_mouse_x = WIDTH / 2 +1;
  p_mouse_y = HEIGHT / 2 +1;
  mouse_x = WIDTH / 2 +1;
  mouse_y = HEIGHT / 2 +1;
  max_rad = 0;
  mouse_array.unshift('e');
  for (var i = 0; i < mouse_array.length; i++) {

    if (!mouse_array[i].localeCompare('a')) {
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
      mouse_y = p_mouse_y + 1;
    } else if (!mouse_array[i].localeCompare('d')) {
      p_mouse_x = mouse_x;
      p_mouse_y = mouse_y;
      mouse_y = p_mouse_y - 1;
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
    colorMode(HSB);
    if (isdraw) {
      for (var j = 0; j < number_parts; j++) {
        angleMode(DEGREES);
        rotate(360 / number_parts);

        noFill();
        strokeWeight(2);
        stroke(20,0,100);
        // var rad = sqrt((mouse_y- HEIGHT / 2)*(mouse_y- HEIGHT / 2) + (mouse_x- WIDTH / 2)*(mouse_x- WIDTH / 2));
        // ellipse(0,0,rad*2, rad*2);

        stroke(320, 60, 10);
        strokeWeight(2);
        line(p_mouse_x - WIDTH / 2, p_mouse_y - HEIGHT / 2, mouse_x - WIDTH / 2, mouse_y - HEIGHT / 2);
        line(p_mouse_x - WIDTH / 2, HEIGHT - p_mouse_y - HEIGHT / 2, mouse_x - WIDTH / 2, HEIGHT - mouse_y - HEIGHT / 2);
        // if(mouse_y > max_mouse_y) { max_mouse_y = mouse_y; }
        // if(mouse_x > max_mouse_x) { max_mouse_x = mouse_x; }

        max_mouse_x = mouse_x;
        max_mouse_y = mouse_y;
      }
    } else {
      strokeWeight(5);
      stroke(200, 60, 80);
      // line(p_mouse_x - WIDTH / 2, p_mouse_y - HEIGHT / 2, mouse_x - WIDTH / 2, mouse_y - HEIGHT / 2);
      var rad = sqrt((mouse_y- HEIGHT / 2)*(mouse_y- HEIGHT / 2) + (mouse_x- WIDTH / 2)*(mouse_x- WIDTH / 2));
      if( rad > max_rad) {
        max_rad = rad;
      }

    }
  }
  stroke(255,45,100);
  // var rad = sqrt((max_mouse_y- HEIGHT / 2)*(max_mouse_y- HEIGHT / 2) + (max_mouse_x- WIDTH / 2)*(max_mouse_x- WIDTH / 2));
  console.log('finishing');
  return ({
    radius : max_rad
  });

}
