## Goal

1- you have a cube and one single joint deforming the cube.

2- write a Maya Python script that:
    * exports the cube to a USD file.
    * exports the joint to a USD file.
    * creates a USD-Skel definition that binds the geometry and the joint.

3- write a Houdini Python Script that:
    * reads the USD-Skel file generated at step 2.
    * makes the cube with the deforming joint available to the artist in the viewport.



## Sturcture


    |>> modules
        |>> usd
            |>> lib.py >> usd modules

    |>> apps

        |>> maya
            |>> lib.py >> maya modules
            |>> create_rig.py

        |>> houdini
            |>> lib.py >> houdini modules
            |>> load_rig.py