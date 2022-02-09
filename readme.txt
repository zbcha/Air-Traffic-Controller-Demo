Basic Operations:
1. Open the ATC.exe file to run the application.
2. A plane will spawn and land in lane#1 by default.
3. Push button "To Lane#1" or "To Lane2" to land the plane on corresponding lane.
4. Push button "Restart" to respawn the plane at the edge of the airport.

Implementation:
- Using PyQt5 library to accomplish this application, following in functions are all from this package.
- Using built-in function "Pen" and "Label" function to build the sence.
- Using built-in object "QtWidgets" to simbolized the plane.
- Using built-in object "QFrame" to creat animation frame.
- Using built-in function "QPropertyAnimation" and "QSequentialAnimationGroup" for animation movement.
- Before landing, the movement of the plane is controlled by the "Lane" buttons, which tells the plane fly towards the corresponding start of the lane.
- After landing, the plane go along with the lane by default.
- After telling the plane to hold, plane will fly in a fixed circle pattern.

Exisiting Problems:
1. Can not spawn more than one plane randomly.
2. Can not delete "plane" when it finishes the landing.
3. Can not customize the number of landing lanes.
4. The holding pattern is fixed.

Note:
Sorry for the incapability of spawning random nomber of planes in the applicatin within 10 hours.
There are more similar projects in my Github page under "OpenGL" repository, including a star trek and a flight simulation games.
To be honest, the incapability of spawning real time object and deletion process still exist in the projects mentioned above, which
should be the main challenge I should solve in future projects.