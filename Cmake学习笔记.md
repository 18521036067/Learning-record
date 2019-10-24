# gcc/g++/cmake学习笔记

## 1.程序编译的四个阶段

| 预处理  | 编译   | 汇编   | 链接    |
| ---- | ---- | ---- | ----- |
| .i文件 | .s文件 | .o文件 | 可执行文件 |

+ 预处理：

  > 编译器将C程序的头文件编译进来，还有宏的替换，可以用gcc的参数-E来参看。
  > 
  > 命令：unix>gcc –o hello hello.c
  > 
  > 作用：将hello.c预处理输出hello.i

+ 编译：

  > 这个阶段编译器主要做词法分析、语法分析、语义分析等，在检查无错误后后，把代码翻译成汇编语言[。可用gcc的参数-S来参看。 编译器(ccl)将文本文件hello.i 翻译成文本文件hello.s, 它包含一个汇编语言程序，一条低级机器语言指令。 
  > 
  > 命令：gcc -S hello.i -o hello.s 
  > 
  > 作用：将预处理输出文件hello.i汇编成hello.s文件

+ 汇编：

  > 汇编器as 将hello.s 翻译成机器语言保存在hello.o 中（二进制文本形式）。

+ 链接：

  > printf函数存在于一个名为printf.o的单独预编译目标文件中。必须得将其并入到hello.o的程序中，链接器就是负责处理这两个的并入，结果得到hello文件，它就是一个可执行的目标文件。

## 2.gcc/g++命令

简单编译(预处理编译汇编)

```powershell
g++ main.cpp
```

指定输出文件名 -o

```powershell
g++ -o main main.cpp
g++ -o main.exe main.cpp
g++ main.cpp -o main
```

包含头文件 -I (大写i)

```powershell
g++ main.cpp -I ./include/ -o main.exe
I区分大小写，且I后面可以不空格
```

包含库文件 -L

```powershell
g++ main.cpp -L usr/local/lib
```

链接库 -l (小写L)

```powershell
g++ main.cpp -L usr/local/lib -l opencv_world343
不加后缀.so和前缀lib
```

> -I后面紧跟着用户设定的编译器头文件查找路径
> 
> 如：    -I/my_include_path/
> 
> -L后面紧跟着用户设定的编译器库文件查找路径
> 
> 如:     -L/my_lib_search_path/
> 
> -l用来指明编译器要链接哪些库
> 
> 如：   gcc test.c -o test  -lmylibname

OpenCV集成的链接参数

```powershell
pkg-config --cflags --libs opencv
输入后可以看到一系列-L -l -I
g++ main `pkg-config --cflags --libs opencv`
```

C++11语法支持

```powershell
g++ main.cpp -o mian -std=c++11
```

## 3 cmake命令

CMakeLists.txt 的语法比较简单，由命令、注释和空格组成，其中命令是不区分大小写的。符号`#`后面的内容被认为是注释。命令由命令名称、小括号和参数组成，参数之间使用空格进行间隔。

### 3.1 cmake使用流程

1.编写CMakeLists.txt

2.`cmake PATH`，如果是当前目录:`cmake .`(生成Makefile)

3.`make`(生成可执行文件)

### 3.2 多目录多文件项目的两种CMakeLists.txt写法

结构一：添加子目录(子目录中同时含有头文件和源文件)，在子目录中也编写CMakeLists.txt,生成链接库

结构二：单个CMakeLists.txt文件，头文件源文件分离，依次指明编译文件的路径

#### 3.2.1 结构一：

**文件结构：**

```
./Demo3
    |
    +--- main.cc
    |
    +--- math/
          |
          +--- MathFunctions.cc
          |
          +--- MathFunctions.h
```

> 对于这种情况，需要分别在项目根目录 Demo3 和 math 目录里各编写一个 CMakeLists.txt 文件。为了方便，我们可以先将 math 目录里的文件编译成静态库再由 main 函数调用。

**根目录CMakeLists.txt**

```makefile
# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)
# 项目信息
project (Demo3)
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)
# 添加 math 子目录

add_subdirectory(math)
# 指定生成目标 
add_executable(Demo main.cc)
# 添加链接库
target_link_libraries(Demo MathFunction)
```

> 该文件添加了下面的内容: 第4行，使用命令`add_subdirectory`指明本项目包含一个子目录 math，这样 math 目录下的 CMakeLists.txt 文件和源代码也会被处理 。第6行，使用命令`target_link_libraries`指明可执行文件 Demo 需要连接一个名为 MathFunctions 的链接库 。

```makefile
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_LIB_SRCS 变量
aux_source_directory(. DIR_LIB_SRCS)
# 生成链接库
add_library (MathFunctions ${DIR_LIB_SRCS})
```

> 在该文件中使用命令`add_library`将 src 目录中的源文件编译为静态链接库。

#### 3.2.2结构二：

**文件结构：**

```
./HelloWorld

    |

    +--- main.cpp

    |

    +--- include/

          |

          +--- HelloWorld.h

    +--- src/

          |

          +--- HelloWorld.cpp
```

> 对于这种情况，采用只在根目录编写一个CMakeLists.txt 文件。

**根目录CMakeLists.txt**

```makefile
# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)
# 项目信息
project (HelloWorld)
#包含目录
include_directories(
    ${PROJECT_SOURCE_DIR}
    ${PROJECT_SOURCE_DIR}/include
)
# 指定生成目标
add_executable(main main.cpp ./src/HelloWorld.cpp)
```

### 3.3 CMakelists.txt模板

```makefile
# DC's Simple Template
# 21825064@zju.edu.cn
cmake_minimum_required (VERSION 2.8)
project (hello_world)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_BUILD_TYPE Release)

find_package(OpenCV 3 REQUIRED)

message(STATUS "---------------------------------------------------")
message(STATUS "Architecture  :  ${CMAKE_LIBRARY_ARCHITECTURE}")
message(STATUS "System        :  ${CMAKE_SYSTEM}")
message(STATUS "OpenCV version:  ${OpenCV_VERSION}")
message(STATUS "---------------------------------------------------" \n)

add_definitions(-D __FLAG__)

set(BUILD_NAME hello)

include_directories(
        ${PROJECT_SOURCE_DIR}
        ${PROJECT_SOURCE_DIR}/include
        ${OpenCV_INCLUDE_DIR}
)

set(SOURCE_FILES
        ${PROJECT_SOURCE_DIR}/src/HelloWorld.cpp
        )

set(EXECUTABLE_OUTPUT_PATH ./bin)

add_executable(${BUILD_NAME} main.cpp ${SOURCE_FILES})

target_link_libraries(${BUILD_NAME}
        ${OpenCV_LIBS}
        )
```
