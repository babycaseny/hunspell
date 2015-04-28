#ifndef _DICTMGR_HXX_
#define _DICTMGR_HXX_

#include "hunvisapi.h"

#define MAXDICTIONARIES 100
#define MAXDICTENTRYLEN 1024

struct dictentry {
  char * filename;
  char * lang;
  char * region;
};


class LIBHUNSPELL_DLL_EXPORTED DictMgr
{
<<<<<<< HEAD

=======
private:
  DictMgr(const DictMgr&);
  DictMgr& operator = (const DictMgr&);
private:
>>>>>>> 8f88d9931e4741e079f22440220798dbe7ab334c
  int                 numdict;
  dictentry *         pdentry;

public:
 
  DictMgr(const char * dictpath, const char * etype);
  ~DictMgr();
  int get_list(dictentry** ppentry);
            
private:
  int  parse_file(const char * dictpath, const char * etype);
  char * mystrsep(char ** stringp, const char delim);
  char * mystrdup(const char * s);
  void mychomp(char * s);

};

#endif
