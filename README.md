# YOLT (You Only Look Twice)

This repository contains a small script to merge the capabilities of two different algorithms:

1. [3D Photography using Context-aware Layered Depth Inpainting](https://github.com/vt-vl-lab/3d-photo-inpainting)
2. [You Only Look Once (YOLO)](https://github.com/AlexeyAB/darknet)

By using the `3d-photo-inpainting` method we can brign an extra dimension to our picture, which will eventually help `yolo` to better detect "occluded" objects and improve the accuracy of the detection (for some of the frames).

## Pre-requisites

Clone the respective repositories that you can find on their original GitHub (see links above) and follow their instructions to test that the code is properly set up and up and running.

Inside the `3d-photo-inpainting` folder change the `argument.yml` to:

```
...
src_folder: ../images
video_folder: ../videos
...
```

Inside the `darknet` folder change the `Makefile` to (before bulding the project):

```
...
OPENCV=1
...
```

## How to use

Place your test images inside the `images` folder and run the following command:

`python yolt.py`

This will save the output of the `3d-in-painting` method in the `videos` folder, with the following: four rendered videos with zoom-in, swing, and circle motion and dolly zoom-in effect, respectively). Once this step is completed, the program will run the YOLOv4 detector on the rendered videos.

The resulting videos will be allocated in the `videos` folder.

## Other considerations

If you are using CPU instead of GPU, in `argument.yml` inside the `3d-photo-inpainting` folder change the `gpu_ids` to a negative number, e.g.:

```
...
gpu_ids: -1
...
```

For simplicity, you can continue working on the venv created with conda for the `3d-photo-inpainting` and install the necessary packages to run `darknet`, most likely you would only have to install OpenCV.

To make this run on MacOS (YOLO only comes for Windows and Linux distribution), make sure that you have `Homebrew` installed, and install the following package:

`brew install pkg-config`

Then you have to install the OpenCV dependency as well, running the following command:

`brew install opencv`