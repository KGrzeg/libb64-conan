cmake_minimum_required(VERSION 3.15)
project(libb64 CXX)

add_library(libb64 src/libb64.cpp)
target_include_directories(libb64 PUBLIC include)

set_target_properties(libb64 PROPERTIES PUBLIC_HEADER "include/libb64.h")
install(TARGETS libb64)
