See some results on Youtube:

[![Disintegration loops](http://img.youtube.com/vi/KygR7csXVYI/1.jpg)](http://www.youtube.com/watch?v=KygR7csXVYI)

This uses OpenMVG and OpenMVS to repeatedly reconstruct a model and texture from turntable renders created by Houdini, inspired by iq's tweet: https://twitter.com/iquilezles/status/895865845854855169

Each step took about 4 minutes to render and solve.  After 23 steps OpenMVG could no longer determine enough structure to continue.

The rather banal main problem is that the scene tends to come out at an odd scale and orientation, so it has to be fitted back to an upright position in front of the camera in Houdini.  This process is not very accurate, so most of the distortion here is probably a result of the model moving each time.

One could either do better shape fitting with PCA to keep it upright, or provide OpenMVG with hints about scene scale and up vector, as extrinsic camera parameters.

Original model CC alban, from https://sketchfab.com/models/deead583a6fb48c6aa43fea5f2936349
