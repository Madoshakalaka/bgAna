# bgAna - Background Analyzer
![travis-badge](https://travis-ci.org/Madoshakalaka/bgAna.svg?branch=master)

Heuristics to get the background color of any image

It's useful when you want to embed image in a bigger frame. This can be used to determine the color of the bigger frame.

## Showcase

It does a pretty good job

![showcase1](https://raw.githubusercontent.com/Madoshakalaka/bgAna/master/readme_assets/showcase1.png)
![showcase1](https://raw.githubusercontent.com/Madoshakalaka/bgAna/master/readme_assets/showcase2.png)


## How to Use

It supports python 3.5 3.6 3.7 and most possibly future versions

`pip install bgAna`

```python
from bgAna import analyze_bg
img = cv2.imread('/home/matt/studyResource/.secretWeebFolder/waifu_no_435.jpg')
res = analyze_bg(img) # img can be just a filename or an np.ndarray as shown here. caution: color is in BGR


>>> print(type(res), res)
np.ndarray [125,125,125]
```

It also creates command line executable entry point by default

You should be able to run the following commands anywhere.

- `$ bgAna thonk.png`
    - output: `(125, 125, 125)`

- `$ bgAna -h` for more help

