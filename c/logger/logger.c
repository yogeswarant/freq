#include <stdio.h>
#include <stdarg.h>
#include "logger.h"

/*
 * Util function to print to stdout 
 */
int debug(char *file, char *function, int line, char *fmt, ...)
{
        int ret = 0;
        va_list argp;
        fprintf(stdout, "[%s:%s:%d]", file, function, line);
        va_start(argp, fmt);
        ret = vfprintf(stdout, fmt, argp);
        va_end(argp);
        return ret;
}

/*
 * Util function to print to stderr 
 */
int error(char *file, char *function, int line, char *fmt, ...)
{
        int ret = 0;
        va_list argp;
        fprintf(stderr, "[%s:%s:%d]", file, function, line);
        va_start(argp, fmt);
        ret = vfprintf(stderr, fmt, argp);
        va_end(argp);
        return ret;
}
