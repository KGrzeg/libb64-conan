cmake_minimum_required(VERSION 3.0)

############################################################
# Project
############################################################

project(libb64 LANGUAGES C CXX VERSION 1.2.1)

############################################################
# Library
############################################################

add_library(libb64 STATIC
    src/cdecode.c
    src/cencode.c
)

target_include_directories(libb64
    PUBLIC
        ${PROJECT_SOURCE_DIR}/include
)

target_compile_definitions(libb64
    PUBLIC
        LIBB64_BUFFERSIZE=16777216
)

install(TARGETS libb64)
