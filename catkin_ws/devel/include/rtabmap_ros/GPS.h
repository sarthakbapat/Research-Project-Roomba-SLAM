// Generated by gencpp from file rtabmap_ros/GPS.msg
// DO NOT EDIT!


#ifndef RTABMAP_ROS_MESSAGE_GPS_H
#define RTABMAP_ROS_MESSAGE_GPS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rtabmap_ros
{
template <class ContainerAllocator>
struct GPS_
{
  typedef GPS_<ContainerAllocator> Type;

  GPS_()
    : stamp(0.0)
    , longitude(0.0)
    , latitude(0.0)
    , altitude(0.0)
    , error(0.0)
    , bearing(0.0)  {
    }
  GPS_(const ContainerAllocator& _alloc)
    : stamp(0.0)
    , longitude(0.0)
    , latitude(0.0)
    , altitude(0.0)
    , error(0.0)
    , bearing(0.0)  {
  (void)_alloc;
    }



   typedef double _stamp_type;
  _stamp_type stamp;

   typedef double _longitude_type;
  _longitude_type longitude;

   typedef double _latitude_type;
  _latitude_type latitude;

   typedef double _altitude_type;
  _altitude_type altitude;

   typedef double _error_type;
  _error_type error;

   typedef double _bearing_type;
  _bearing_type bearing;





  typedef boost::shared_ptr< ::rtabmap_ros::GPS_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rtabmap_ros::GPS_<ContainerAllocator> const> ConstPtr;

}; // struct GPS_

typedef ::rtabmap_ros::GPS_<std::allocator<void> > GPS;

typedef boost::shared_ptr< ::rtabmap_ros::GPS > GPSPtr;
typedef boost::shared_ptr< ::rtabmap_ros::GPS const> GPSConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rtabmap_ros::GPS_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rtabmap_ros::GPS_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace rtabmap_ros

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'rtabmap_ros': ['/home/ubuntu/catkin_ws/src/rtabmap_ros/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::rtabmap_ros::GPS_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rtabmap_ros::GPS_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rtabmap_ros::GPS_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rtabmap_ros::GPS_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rtabmap_ros::GPS_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rtabmap_ros::GPS_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rtabmap_ros::GPS_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0acde0d09a1ab74993cf4e41ff4eae49";
  }

  static const char* value(const ::rtabmap_ros::GPS_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0acde0d09a1ab749ULL;
  static const uint64_t static_value2 = 0x93cf4e41ff4eae49ULL;
};

template<class ContainerAllocator>
struct DataType< ::rtabmap_ros::GPS_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rtabmap_ros/GPS";
  }

  static const char* value(const ::rtabmap_ros::GPS_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rtabmap_ros::GPS_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
float64 stamp      # in seconds\n\
float64 longitude  # DD format\n\
float64 latitude   # DD format\n\
float64 altitude   # in meters\n\
float64 error      # in meters\n\
float64 bearing    # North 0->360 deg\n\
";
  }

  static const char* value(const ::rtabmap_ros::GPS_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rtabmap_ros::GPS_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.stamp);
      stream.next(m.longitude);
      stream.next(m.latitude);
      stream.next(m.altitude);
      stream.next(m.error);
      stream.next(m.bearing);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GPS_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rtabmap_ros::GPS_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rtabmap_ros::GPS_<ContainerAllocator>& v)
  {
    s << indent << "stamp: ";
    Printer<double>::stream(s, indent + "  ", v.stamp);
    s << indent << "longitude: ";
    Printer<double>::stream(s, indent + "  ", v.longitude);
    s << indent << "latitude: ";
    Printer<double>::stream(s, indent + "  ", v.latitude);
    s << indent << "altitude: ";
    Printer<double>::stream(s, indent + "  ", v.altitude);
    s << indent << "error: ";
    Printer<double>::stream(s, indent + "  ", v.error);
    s << indent << "bearing: ";
    Printer<double>::stream(s, indent + "  ", v.bearing);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RTABMAP_ROS_MESSAGE_GPS_H
