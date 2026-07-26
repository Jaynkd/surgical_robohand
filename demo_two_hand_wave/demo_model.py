import os
import mujoco

def get_dual_hands_spec():
    right_xml_path = "shadow_hand/right_hand.xml"
    if not os.path.exists(right_xml_path):
        import urllib.request
        url = "https://raw.githubusercontent.com/google-deepmind/mujoco_menagerie/main/shadow_hand/right_hand.xml"
        urllib.request.urlretrieve(url, right_xml_path)

    # 1. Main scene spec
    main_spec = mujoco.MjSpec()

    # Worldbody & environment setup
    main_spec.worldbody.add_light(pos=[0, 0, 1.5], dir=[0, 0, -1], diffuse=[0.8, 0.8, 0.8])
    main_spec.worldbody.add_geom(type=mujoco.mjtGeom.mjGEOM_PLANE, size=[1.5, 1.5, 0.05], pos=[0, 0, -0.2])

    # 2. Add mounting sites for left and right hands
    left_mount = main_spec.worldbody.add_site(
        name="left_mount", pos=[-0.30, 0, 0.1], quat=[0.5, 0.5, 0.5, 0.5]
    )
    right_mount = main_spec.worldbody.add_site(
        name="right_mount", pos=[0.30, 0, 0.1], quat=[0.5, -0.5, -0.5, 0.5]
    )

    # 3. Load hand specs and attach using main_spec.attach()
    left_spec = mujoco.MjSpec.from_file("shadow_hand/left_hand.xml")
    main_spec.attach(left_spec, site=left_mount, prefix="lh_")

    right_spec = mujoco.MjSpec.from_file("shadow_hand/right_hand.xml")
    main_spec.attach(right_spec, site=right_mount, prefix="rh_")

    return main_spec

def load_dual_hands_model():
    spec = get_dual_hands_spec()
    return spec.compile()
