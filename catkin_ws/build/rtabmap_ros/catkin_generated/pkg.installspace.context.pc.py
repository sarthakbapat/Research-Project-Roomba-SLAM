# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/opt/ros/kinetic/lib/arm-linux-gnueabihf/rtabmap-0.19/../../../include/rtabmap-0.19;/opt/ros/kinetic/include/opencv-3.3.1-dev;/opt/ros/kinetic/include/opencv-3.3.1-dev/opencv".split(';') if "${prefix}/include;/opt/ros/kinetic/lib/arm-linux-gnueabihf/rtabmap-0.19/../../../include/rtabmap-0.19;/opt/ros/kinetic/include/opencv-3.3.1-dev;/opt/ros/kinetic/include/opencv-3.3.1-dev/opencv" != "" else []
PROJECT_CATKIN_DEPENDS = "cv_bridge;roscpp;rospy;sensor_msgs;std_msgs;std_srvs;nav_msgs;geometry_msgs;visualization_msgs;image_transport;tf;tf_conversions;tf2_ros;eigen_conversions;laser_geometry;pcl_conversions;pcl_ros;nodelet;dynamic_reconfigure;message_filters;class_loader;rosgraph_msgs;stereo_msgs;move_base_msgs;image_geometry;costmap_2d;octomap_msgs;rviz;find_object_2d".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lrtabmap_ros;/opt/ros/kinetic/lib/arm-linux-gnueabihf/librtabmap_core.so;/opt/ros/kinetic/lib/arm-linux-gnueabihf/librtabmap_utilite.so;/opt/ros/kinetic/lib/arm-linux-gnueabihf/librtabmap_gui.so;/usr/lib/arm-linux-gnueabihf/libz.so;/opt/ros/kinetic/lib/libg2o_core.so;/opt/ros/kinetic/lib/libg2o_types_slam2d.so;/opt/ros/kinetic/lib/libg2o_types_slam3d.so;/opt/ros/kinetic/lib/libg2o_types_sba.so;/opt/ros/kinetic/lib/libg2o_stuff.so;/opt/ros/kinetic/lib/libg2o_solver_csparse.so;/opt/ros/kinetic/lib/libg2o_csparse_extension.so;/usr/lib/arm-linux-gnueabihf/libcxsparse.so;/opt/ros/kinetic/lib/libg2o_solver_cholmod.so;/usr/lib/arm-linux-gnueabihf/libcholmod.so;/usr/lib/arm-linux-gnueabihf/libfreenect.so;/usr/lib/arm-linux-gnueabihf/libfreenect_sync.so;/opt/ros/kinetic/lib/liboctomap.so;/opt/ros/kinetic/lib/liboctomath.so;/usr/lib/arm-linux-gnueabihf/libvtkGUISupportQt-6.2.so.6.2.0;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_calib3d3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_core3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_dnn3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_features2d3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_flann3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_highgui3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_imgcodecs3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_imgproc3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_ml3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_objdetect3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_photo3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_shape3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_stitching3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_superres3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_video3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_videoio3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_videostab3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_viz3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_aruco3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_bgsegm3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_bioinspired3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_ccalib3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_cvv3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_datasets3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_dpm3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_face3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_fuzzy3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_hdf3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_img_hash3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_line_descriptor3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_optflow3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_phase_unwrapping3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_plot3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_reg3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_rgbd3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_saliency3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_stereo3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_structured_light3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_surface_matching3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_text3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_tracking3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_xfeatures2d3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_ximgproc3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_xobjdetect3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_xphoto3.so.3.3.1".split(';') if "-lrtabmap_ros;/opt/ros/kinetic/lib/arm-linux-gnueabihf/librtabmap_core.so;/opt/ros/kinetic/lib/arm-linux-gnueabihf/librtabmap_utilite.so;/opt/ros/kinetic/lib/arm-linux-gnueabihf/librtabmap_gui.so;/usr/lib/arm-linux-gnueabihf/libz.so;/opt/ros/kinetic/lib/libg2o_core.so;/opt/ros/kinetic/lib/libg2o_types_slam2d.so;/opt/ros/kinetic/lib/libg2o_types_slam3d.so;/opt/ros/kinetic/lib/libg2o_types_sba.so;/opt/ros/kinetic/lib/libg2o_stuff.so;/opt/ros/kinetic/lib/libg2o_solver_csparse.so;/opt/ros/kinetic/lib/libg2o_csparse_extension.so;/usr/lib/arm-linux-gnueabihf/libcxsparse.so;/opt/ros/kinetic/lib/libg2o_solver_cholmod.so;/usr/lib/arm-linux-gnueabihf/libcholmod.so;/usr/lib/arm-linux-gnueabihf/libfreenect.so;/usr/lib/arm-linux-gnueabihf/libfreenect_sync.so;/opt/ros/kinetic/lib/liboctomap.so;/opt/ros/kinetic/lib/liboctomath.so;/usr/lib/arm-linux-gnueabihf/libvtkGUISupportQt-6.2.so.6.2.0;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_calib3d3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_core3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_dnn3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_features2d3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_flann3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_highgui3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_imgcodecs3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_imgproc3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_ml3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_objdetect3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_photo3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_shape3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_stitching3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_superres3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_video3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_videoio3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_videostab3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_viz3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_aruco3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_bgsegm3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_bioinspired3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_ccalib3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_cvv3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_datasets3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_dpm3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_face3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_fuzzy3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_hdf3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_img_hash3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_line_descriptor3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_optflow3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_phase_unwrapping3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_plot3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_reg3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_rgbd3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_saliency3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_stereo3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_structured_light3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_surface_matching3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_text3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_tracking3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_xfeatures2d3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_ximgproc3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_xobjdetect3.so.3.3.1;/opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_xphoto3.so.3.3.1" != "" else []
PROJECT_NAME = "rtabmap_ros"
PROJECT_SPACE_DIR = "/home/ubuntu/catkin_ws/install"
PROJECT_VERSION = "0.19.3"
