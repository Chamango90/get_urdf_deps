cmake_minimum_required(VERSION 2.8.3)
project(get_urdf_deps)
find_package(catkin REQUIRED)

catkin_install_python(PROGRAMS 
  scripts/create_def_proj
  scripts/get_mesh_deps
  scripts/save_urdf
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

