import os
root = '/works/disintegrationloops'

for step in range(1, 50):
	print step

	os.system('mkdir -p %s/steps/%04d/mvs' % (root, step))
	os.chdir('%s/steps/%04d/mvs' % (root, step))

	if(step > 1):
		os.system('PREVSTEP=%04d STEP=%04d hrender -e -f 1 20 -d mantra1 -v %s/step.hip' % root)

	os.system('python %s/disintegrationloops/sfm.py %s/steps/%04d/images %s/steps/%04d' % (root, root, step, root, step))

	os.system('%s/openmvg/openMVG_Build/Darwin-x86_64-RELEASE/openMVG_main_openMVG2openMVS -i %s/steps/%04d/reconstruction_global/sfm_data.bin -o %s/steps/%04d/mvs/scene.mvs' % (root, root, step, root, step))
	
	os.system('%s/openmvs/openMVS_build/bin/DensifyPointCloud %s/steps/%04d/mvs/scene.mvs' % (root, root, step))
	os.system('%s/openmvs/openMVS_build/bin/ReconstructMesh %s/steps/%04d/mvs/scene_dense.mvs' % (root, root, step))
	os.system('%s/openmvs/openMVS_build/bin/TextureMesh --export-type obj %s/steps/%04d/mvs/scene_dense_mesh.mvs' % (root, root, step))

	print '\n'
