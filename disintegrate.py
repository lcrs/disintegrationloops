# Repeatedly render a turntable and do photogrammetry on the rendered images to recover the model and texture
# lewis@lewissaunders.com

# To render initial images for step 0001:
# for ((i=1; i<26; i++)); do PREVSTEP=0000 STEP=0001 hrender -e -f $i $i -d mantra1 /works/disintegrationloops/disintegrationloops/step.hip & sleep 0.3; done; wait; echo doneit

import os
root = '/works/disintegrationloops'

for step in range(1, 2):
	print step

	os.system('mkdir -p %s/steps/%04d/mvs' % (root, step))
	os.chdir('%s/steps/%04d/mvs' % (root, step))

	if(step > 1):
		os.system('for ((i=1; i<26; i++)); do PREVSTEP=%04d STEP=%04d hrender -e -f $i $i -d mantra1 %s/disintegrationloops/step.hip & sleep 0.3; done; wait' % (step-1, step, root))

	os.system('python %s/disintegrationloops/sfm.py %s/steps/%04d/images %s/steps/%04d' % (root, root, step, root, step))

	os.system('%s/openmvg/openMVG_Build/Darwin-x86_64-RELEASE/openMVG_main_openMVG2openMVS -i %s/steps/%04d/reconstruction_global/sfm_data.bin -o %s/steps/%04d/mvs/scene.mvs' % (root, root, step, root, step))
	
	os.system('%s/openmvs/openMVS_build/bin/DensifyPointCloud %s/steps/%04d/mvs/scene.mvs' % (root, root, step))
	os.system('%s/openmvs/openMVS_build/bin/ReconstructMesh %s/steps/%04d/mvs/scene_dense.mvs' % (root, root, step))
	os.system('%s/openmvs/openMVS_build/bin/TextureMesh --export-type obj %s/steps/%04d/mvs/scene_dense_mesh.mvs' % (root, root, step))

	print '\n'
