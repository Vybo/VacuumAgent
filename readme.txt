[ Used algorithm ]

The solution uses naive algorithm. It works like this:
	1. If agent can enter room in its direction and agent did not yet vacuum it, enter that room and vacuum it.
	2. Else, go back to previously visited rooms until there is a room next to agent that can be entered and was not vacuumed yet. After found, enter it and continue from step 1.
	3. If there is no more rooms in memory to return to, cleaning is finished.

The algorithm is quite successful in cleaning, however each backtracking stores unnecessary steps, which the agent will again follow when it's backtracking. One solution would be to erase the memory when a new vacuumable room is found, however that would result in the robot cleaning already cleaned rooms.

[ How to run the script ]
Python 3 and newer must be installed on the machine where the program will be used.

There is a prepared 'run.bat' script, which will run the program with maze from the assignment pdf (n=8). If you want to specify your own settings, please use the script in the following way:

> python vacuum.py -n INTEGER -c [list of locked rooms]

Example:
> python vacuum.py -n 8 -c a2,b2,c2,d2,f1,g3,e4,h4,c5,d5,f5,b6,b7,f7,g7

[ Results and Answers to questions ]
n	squares visited		locked rooms
6	152			a2,b2,c2,d2,f1,e4,c5,d5,f5
8	256			a2,b2,c2,d2,f1,g3,e4,h4,c5,d5,f5,b6,b7,f7,g7
10	329			a2,b2,c2,d2,f1,g3,e4,h4,c5,d5,f5,b6,b7,f7,g7,b8,e8,g8,i4,b9,e9,g9,j4
12	288			a2,b2,c2,d2,f1,g3,e4,h4,c5,d5,f5,b6,b7,f7,g7,b8,e8,g8,i4,b9,e9,g9,j4,b10,b11,e10,e11,g10,g11,k4

Does the necessary run-time of each world variation increase linearly or non-linearly?
The run-time increases non-linearly.

 Why do you think the agent consumes that linear or non-linear time? Try to explain it.
This problem is undeterministic and also the algorithm uses backtracking, which consumes a lot of steps. Each blind path causes twice as many steps taken as its length.

[ Bonus functionality ]

There are few videos of the vacuum cleaner running through the maze and cleaning it in the project folder. They are named outN.mp4 and can be played. To enable rendering of runs to such videos, do the following (if you use Windows):

1. Install Python packages 'matplotlib' and 'numpy'.

2. Install FFMpeg according to this tutorial: https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg.

3. The feature should be enabled automatically and the rendering warning should go away.

If everything went fine, after each script run, the output will be rendered as a video file named 'out.mp4' that can be played in any usual media player.

If you're on other operating systems, FFMpeg must be installed in a way that it can be used from terminal by calling the 'ffmpeg' command.

