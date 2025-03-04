cmake_minimum_required(VERSION 3.19 FATAL_ERROR)
project(math_tool)

add_subdirectory(pybind11)
pybind11_add_module(math_tool src/main.cpp)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(math_tool PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
