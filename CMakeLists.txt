cmake_minimum_required(VERSION 3.20.3)

project(BrumSkyOS VERSION 1.0.2 DESCRIPTION "Just for fun, I know it's no way close to being an actual OS.")

set(CMAKE_CXX_STANDARD 23)

set(CMAKE_CXX_STANDARD_REQUIRED True)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0")

file(GLOB SOURCES "src/*.cpp")

add_executable(BrumSkyOS.o ${SOURCES})

target_include_directories(BrumSkyOS.o PRIVATE include)


