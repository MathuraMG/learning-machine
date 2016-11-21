var WIDTH = 1000,
  HEIGHT = 500;
var number_parts = 36;
var drawing = [];

function setup() {
  createCanvas(WIDTH, HEIGHT);
  background(0);
  parts_header = createElement('h4', 'No of parts');
  // parts_slider = createSlider(4,72,36);
  parts_radio = createRadio();
  parts_radio.option('4', 4);
  parts_radio.option('8', 8);
  parts_radio.option('36', 36);
  parts_radio.option('72', 72);
  thickness_header = createElement('h4', 'Stroke Thickness');
  thickness_slider = createSlider(1, 10, 2);
  hue_header = createElement('h4', 'Stroke Hue');
  hue_slider = createSlider(1, 360, 0);
  draw_radial();
  colorMode(HSB);

}

function draw() {
  number_parts = parts_radio.value();
}

function draw_radial() {

  translate(WIDTH / 2, HEIGHT / 2);
  strokeWeight(0.5);
  for (var i = 0; i < number_parts; i++) {
    angleMode(DEGREES);
    rotate(360 / number_parts);
    stroke(200);
    line(0, 0, WIDTH / 2, HEIGHT / 2);
  }
}

function mouseDragged() {
  console.log('drag');
  if (mouseX < WIDTH && mouseY < HEIGHT) {

    translate(WIDTH / 2, HEIGHT / 2);
    colorMode(HSB);
    for (var i = 0; i < number_parts; i++) {
      angleMode(DEGREES);
      rotate(360 / number_parts);
      stroke(hue_slider.value(), 60, 80);
      strokeWeight(thickness_slider.value());
      line(pmouseX - WIDTH / 2, pmouseY - HEIGHT / 2, mouseX - WIDTH / 2, pmouseY - HEIGHT / 2);
      line(pmouseX - WIDTH / 2, mouseY - HEIGHT / 2, mouseX - WIDTH / 2, mouseY - HEIGHT / 2);
      line(pmouseX - WIDTH / 2, HEIGHT - pmouseY - HEIGHT / 2, mouseX - WIDTH / 2, HEIGHT - pmouseY - HEIGHT / 2);
      line(pmouseX - WIDTH / 2, HEIGHT - mouseY - HEIGHT / 2, mouseX - WIDTH / 2, HEIGHT - mouseY - HEIGHT / 2);
    }
    if (mouseX > pmouseX) {
      for (var i = 0; i < (mouseX - pmouseX); i++) {
        drawing.push('a');
      }
    } else if (mouseX < pmouseX) {
      for (var i = 0; i < (pmouseX - mouseX); i++) {
        drawing.push('b');
      }
    }
    if (mouseY > pmouseY) {
      for (var i = 0; i < (mouseY - pmouseY); i++) {
        drawing.push('c');
      }
    } else if (mouseY < pmouseY) {
      for (var i = 0; i < (pmouseY - mouseY); i++) {
        drawing.push('d');
      }
    }
    
  }

}


function mousePressed() {
  drawing.push('e');
}

function mouseReleased() {
  drawing.push('f');
}

function mouseMoved() {
  if (mouseX > pmouseX) {
      for (var i = 0; i < (mouseX - pmouseX); i++) {
        drawing.push('a');
      }
    } else if (mouseX < pmouseX) {
      for (var i = 0; i < (pmouseX - mouseX); i++) {
        drawing.push('b');
      }
    }
    if (mouseY > pmouseY) {
      for (var i = 0; i < (mouseY - pmouseY); i++) {
        drawing.push('c');
      }
    } else if (mouseY < pmouseY) {
      for (var i = 0; i < (pmouseY - mouseY); i++) {
        drawing.push('d');
      }
    }
}
function keyPressed() {
  if (keyCode === LEFT_ARROW) {
    print(drawing);
  }

  if (keyCode === RIGHT_ARROW) {
    // print(mouse_array);
  }
}