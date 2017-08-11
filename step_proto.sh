

#render initial images:
#for ((i=1; i<26; i++)); do PREVSTEP=0000 STEP=0001 hrender -e -f $i $i -d mantra1 /works/disintegrationloops/disintegrationloops/step.hip & sleep 0.3; done; wait; echo done!!



python /works/disintegrationloops/disintegrationloops/sfm.py /works/disintegrationloops/steps/0001/images /works/disintegrationloops/steps/0001

mkdir /works/disintegrationloops/steps/0001/mvs/
cd /works/disintegrationloops/steps/0001/mvs/
/works/disintegrationloops/openmvg/openMVG_Build/Darwin-x86_64-RELEASE/openMVG_main_openMVG2openMVS -i /works/disintegrationloops/steps/0001/reconstruction_global/sfm_data.bin -o /works/disintegrationloops/steps/0001/mvs/scene.mvs

/works/disintegrationloops/openmvs/openMVS_build/bin/DensifyPointCloud /works/disintegrationloops/steps/0001/mvs/scene.mvs

/works/disintegrationloops/openmvs/openMVS_build/bin/ReconstructMesh /works/disintegrationloops/steps/0001/mvs/scene_dense.mvs

/works/disintegrationloops/openmvs/openMVS_build/bin/TextureMesh --export-type obj /works/disintegrationloops/steps/0001/mvs/scene_dense_mesh.mvs
cd -