#ifndef _HUNSPELL_VISIBILITY_H_
#define _HUNSPELL_VISIBILITY_H_

#if defined(HUNSPELL_STATIC)
#  define LIBHUNSPELL_DLL_EXPORTED
#elif defined(_MSC_VER)
#  if defined(BUILDING_LIBHUNSPELL)
#    define LIBHUNSPELL_DLL_EXPORTED __declspec(dllexport)
#  else
#    define LIBHUNSPELL_DLL_EXPORTED __declspec(dllimport)
#  endif
<<<<<<< HEAD
#elif BUILDING_LIBHUNSPELL && 1
=======
#elif defined(BUILDING_LIBHUNSPELL) && 1
>>>>>>> 8f88d9931e4741e079f22440220798dbe7ab334c
#  define LIBHUNSPELL_DLL_EXPORTED __attribute__((__visibility__("default")))
#else
#  define LIBHUNSPELL_DLL_EXPORTED
#endif

#endif
