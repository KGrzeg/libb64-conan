cmake_minimum_required(VERSION 3.15)
project(libb64 LANGUAGES C CXX VERSION 1.2.1)

add_library(libb64 STATIC
  src/cdecode.c
  src/cencode.c
)

target_include_directories(libb64 PUBLIC ${PROJECT_SOURCE_DIR}/include)

set (MY_PUBLIC_HEADERS
  ${PROJECT_SOURCE_DIR}/include/b64/cencode.h
  ${PROJECT_SOURCE_DIR}/include/b64/cdecode.h
)

set_target_properties(libb64 PROPERTIES PUBLIC_HEADER "${MY_PUBLIC_HEADERS}")
install(TARGETS libb64)
