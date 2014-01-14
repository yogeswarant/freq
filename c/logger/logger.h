#ifndef __LOGGER_H__
#define __LOGGER_H__
extern char verbose;
#define dprint(...) debug(__FILE__, (char*)__FUNCTION__, __LINE__, __VA_ARGS__)
#define eprint(...) error(__FILE__, (char*)__FUNCTION__, __LINE__, __VA_ARGS__)
#endif //__LOGGER_H__
