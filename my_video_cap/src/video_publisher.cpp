#include <iostream> // for standard I/O
#include <string>   // for strings
#include <iomanip>  // for controlling float print precision
#include <sstream>  // string to number conversion
#include <opencv2/core.hpp>     // Basic OpenCV structures (cv::Mat, Scalar)
#include <opencv2/imgproc.hpp>  // Gaussian Blur
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>  // OpenCV window I/O

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
 
using namespace std;
using namespace cv;

int main(int argc, char** argv)
{
  ros::init(argc, argv, "video_publisher");
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
  image_transport::Publisher pub = it.advertise("camera/image", 1);
  VideoCapture capture(0);


//ros::Rate loop_rate(1);
  while(nh.ok())
  {
   Mat frame, image;  //定义mat变量，用于存储每一帧的图像
   capture >> frame; //读取当前帧
   cvtColor(frame,image, COLOR_BGR2GRAY);

  
  sensor_msgs::ImagePtr msg = cv_bridge::CvImage(std_msgs::Header(), "mono8", image).toImageMsg();
 
  pub.publish(msg);
  //loop_rate.sleep();
  }
}
