#ifndef _BASEAFF_HXX_
#define _BASEAFF_HXX_

#include "hunvisapi.h"
<<<<<<< HEAD

class LIBHUNSPELL_DLL_EXPORTED AffEntry
{
protected:
    char *         appnd;
    char *         strip;
    unsigned char  appndl;
    unsigned char  stripl;
=======
#include <string>

class LIBHUNSPELL_DLL_EXPORTED AffEntry
{
private:
    AffEntry(const AffEntry&);
    AffEntry& operator = (const AffEntry&);
protected:
    AffEntry()
      : numconds(0)
      , opts(0)
      , aflag(0)
      , morphcode(0)
      , contclass(NULL)
      , contclasslen(0)
    {
    }
    std::string    appnd;
    std::string    strip;
>>>>>>> 8f88d9931e4741e079f22440220798dbe7ab334c
    char           numconds;
    char           opts;
    unsigned short aflag;
    union {
        char       conds[MAXCONDLEN];
        struct {
            char   conds1[MAXCONDLEN_1];
            char * conds2;
        } l;
    } c;
    char *           morphcode;
    unsigned short * contclass;
    short            contclasslen;
};

#endif
