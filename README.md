# Object detection

This program will start video capture with default webcam and draw a rectangle around objects,  
that will be detected by pre-trained haar cascades, such as face, smile, cat's face, full human body.


## Features
- Video capture from default webcam
- Object detection
- Rectangle frame drawing on detected objects
- Detection / frame drawing configuration
- Some pre-trained cascades already included

## Installation
1. Clone project
```bash
git clone https://github.com/gennadis/everything-recognition.git
cd everything-recognition
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Run (press 'q' for quit)
```bash
python run.py
```

## Configuration
Program settings that can be tweaked in `config.py`:
- detection frame color in RGB `"color": (255, 0, 0)`
- detection frame drawing `"draw": True`
- other pre-trained cascades can be added in `config.py` from haarcascades folder (look for `.xml` files)

---

## Modules

### is_user_wants_quit()
Check if 'q' key is pressed

### show_frame(frame)
Open 'Video' window with a single frame captured from a webcam

### draw_sqare(frame, color)
Draw a rectangle around detected object with 2 pixels line thickness

### get_cascades()
Get pre-trained cascades from config.py with 'draw' key == True
