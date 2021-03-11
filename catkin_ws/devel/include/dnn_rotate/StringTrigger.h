// Generated by gencpp from file dnn_rotate/StringTrigger.msg
// DO NOT EDIT!


#ifndef DNN_ROTATE_MESSAGE_STRINGTRIGGER_H
#define DNN_ROTATE_MESSAGE_STRINGTRIGGER_H

#include <ros/service_traits.h>


#include <dnn_rotate/StringTriggerRequest.h>
#include <dnn_rotate/StringTriggerResponse.h>


namespace dnn_rotate
{

struct StringTrigger
{

typedef StringTriggerRequest Request;
typedef StringTriggerResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct StringTrigger
} // namespace dnn_rotate


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::dnn_rotate::StringTrigger > {
  static const char* value()
  {
    return "da58e600b06edde376097686d032b550";
  }

  static const char* value(const ::dnn_rotate::StringTrigger&) { return value(); }
};

template<>
struct DataType< ::dnn_rotate::StringTrigger > {
  static const char* value()
  {
    return "dnn_rotate/StringTrigger";
  }

  static const char* value(const ::dnn_rotate::StringTrigger&) { return value(); }
};


// service_traits::MD5Sum< ::dnn_rotate::StringTriggerRequest> should match 
// service_traits::MD5Sum< ::dnn_rotate::StringTrigger > 
template<>
struct MD5Sum< ::dnn_rotate::StringTriggerRequest>
{
  static const char* value()
  {
    return MD5Sum< ::dnn_rotate::StringTrigger >::value();
  }
  static const char* value(const ::dnn_rotate::StringTriggerRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::dnn_rotate::StringTriggerRequest> should match 
// service_traits::DataType< ::dnn_rotate::StringTrigger > 
template<>
struct DataType< ::dnn_rotate::StringTriggerRequest>
{
  static const char* value()
  {
    return DataType< ::dnn_rotate::StringTrigger >::value();
  }
  static const char* value(const ::dnn_rotate::StringTriggerRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::dnn_rotate::StringTriggerResponse> should match 
// service_traits::MD5Sum< ::dnn_rotate::StringTrigger > 
template<>
struct MD5Sum< ::dnn_rotate::StringTriggerResponse>
{
  static const char* value()
  {
    return MD5Sum< ::dnn_rotate::StringTrigger >::value();
  }
  static const char* value(const ::dnn_rotate::StringTriggerResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::dnn_rotate::StringTriggerResponse> should match 
// service_traits::DataType< ::dnn_rotate::StringTrigger > 
template<>
struct DataType< ::dnn_rotate::StringTriggerResponse>
{
  static const char* value()
  {
    return DataType< ::dnn_rotate::StringTrigger >::value();
  }
  static const char* value(const ::dnn_rotate::StringTriggerResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // DNN_ROTATE_MESSAGE_STRINGTRIGGER_H
