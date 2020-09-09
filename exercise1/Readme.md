# excercise 1 kth formula student

Here is the code for exercise one


Terminal 1
```bash
cd YOUR_CATKIN_ENV
source devel/setup.bash
catkin_make
roscore
```

Terminal 2
```bash
rosrun exc1 broadcaster.py
```

Terminal 3
```bash
rosrun exc1 receiver.py
```

Terminal 4
```bash
rosrun plotjuggler PlotJuggler
```
When plotjugger opens go to `Streaming>Start ROS Topic Subscriber` and choose topics `xamin` and `/kthfs/result`

then select them and drag them into the plot.