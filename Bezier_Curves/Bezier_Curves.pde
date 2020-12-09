class Point {  
  public int x, y;
  
  Point(int X, int Y) {
    x = X;
    y = Y;
  }
}

int frame=0;
int X0=60, Y0=350;
int X1=110, Y1=70;
int X2=320, Y2=210;

Point P0 = new Point(X0, Y0);
Point P1 = new Point(X1, Y1);
Point P2 = new Point(X2, Y2);

void setup() {
  size(400,400);
  frameRate(36);
  
  background(0);
  stroke(255);
  line(P0.x,P0.y,P1.x,P1.y);
  line(P1.x,P1.y,P2.x,P2.y);
}

void draw() {
  float U1 = map(frame, 0, 100, P0.x ,P1.x); 
  float V1 = map(frame, 0, 100, P0.y ,P1.y);
 
  float U2 = map(frame, 0, 100, P1.x ,P2.x); 
  float V2 = map(frame, 0, 100, P1.y ,P2.y);
 
  if(mousePressed || key=='A') {
    frame+=1;
    stroke(150,70);
    line(U1,V1,U2,V2);
    
    frame=frame>100 ? 100 : frame;
  }
}
