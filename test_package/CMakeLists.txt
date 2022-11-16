cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(libb64 CONFIG REQUIRED)

add_executable(example src/example.cpp)
target_link_libraries(example libb64::libb64)
