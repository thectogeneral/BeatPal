class Pulse {
  constructor(frameRate = 30) {
    this.avgRed = [];
    this.rgbImgs = [];
    this.distance = [];
    this.sigmoids = [];
    this.frameRate = frameRate;
    this.dim = new cv.Size(320, 240);
  }
}
