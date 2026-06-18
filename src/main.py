import numpy as np
import mujoco as mj
import mujoco.viewer

def main():
    model = mj.MjModel.from_xml_path("master_models/master_scene.xml")
    data = mj.MjData(model)


    with mujoco.viewer.launch_passive(model, data) as viewer:
        
        # Camera parameters
        viewer.cam.type = mj.mjtCamera.mjCAMERA_FREE
        viewer.cam.lookat[:] = np.array([1., 0., 1.])
        viewer.cam.distance = 2.
        viewer.cam.azimuth = 180
        viewer.cam.elevation = -15

        while viewer.is_running():
            t = data.time




if __name__ == "__main__":
    main()