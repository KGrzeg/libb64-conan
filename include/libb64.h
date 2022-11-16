#pragma once

#ifdef _WIN32
  #define libb64_EXPORT __declspec(dllexport)
#else
  #define libb64_EXPORT
#endif

libb64_EXPORT void libb64();
