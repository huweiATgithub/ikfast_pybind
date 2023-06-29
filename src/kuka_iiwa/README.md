1. The `IK` is generated based on the [iiwa14.urdf](iiwa14.urdf) which is copied and simplified (only properties related to kinematics plus link's inertia are kept) from [iiwa14_spheres_collision.urdf](https://github.com/RobotLocomotion/drake/blob/master/manipulation/models/iiwa_description/urdf/iiwa14_spheres_collision.urdf).
2. We use [pyikfast](https://github.com/cyberbotics/pyikfast) to help generate the IK solver.
    ```bash
    openrave.py --database inversekinematics --robot=robot.xml --iktype=transform6d --iktests=100
    ```
3. OpenRAVE automatically selects the third joint to be the free joint. To assign free joint, one can add an option `--freejoint=<name-of-free-join>` to the command `openrave.py`.
