# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1

# Include any dependencies generated for this target.
include src/bin/jp2/CMakeFiles/opj_dump.dir/depend.make

# Include the progress variables for this target.
include src/bin/jp2/CMakeFiles/opj_dump.dir/progress.make

# Include the compile flags for this target's objects.
include src/bin/jp2/CMakeFiles/opj_dump.dir/flags.make

src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o: src/bin/jp2/CMakeFiles/opj_dump.dir/flags.make
src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o: src/bin/jp2/opj_dump.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/opj_dump.dir/opj_dump.c.o   -c /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2/opj_dump.c

src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/opj_dump.dir/opj_dump.c.i"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -E /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2/opj_dump.c > CMakeFiles/opj_dump.dir/opj_dump.c.i

src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/opj_dump.dir/opj_dump.c.s"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -S /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2/opj_dump.c -o CMakeFiles/opj_dump.dir/opj_dump.c.s

src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o.requires:
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o.requires

src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o.provides: src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o.requires
	$(MAKE) -f src/bin/jp2/CMakeFiles/opj_dump.dir/build.make src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o.provides.build
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o.provides

src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o.provides.build: src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o

src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o: src/bin/jp2/CMakeFiles/opj_dump.dir/flags.make
src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o: src/bin/jp2/convert.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/opj_dump.dir/convert.c.o   -c /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2/convert.c

src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/opj_dump.dir/convert.c.i"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -E /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2/convert.c > CMakeFiles/opj_dump.dir/convert.c.i

src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/opj_dump.dir/convert.c.s"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -S /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2/convert.c -o CMakeFiles/opj_dump.dir/convert.c.s

src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o.requires:
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o.requires

src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o.provides: src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o.requires
	$(MAKE) -f src/bin/jp2/CMakeFiles/opj_dump.dir/build.make src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o.provides.build
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o.provides

src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o.provides.build: src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o

src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o: src/bin/jp2/CMakeFiles/opj_dump.dir/flags.make
src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o: src/bin/jp2/index.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/opj_dump.dir/index.c.o   -c /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2/index.c

src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/opj_dump.dir/index.c.i"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -E /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2/index.c > CMakeFiles/opj_dump.dir/index.c.i

src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/opj_dump.dir/index.c.s"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -S /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2/index.c -o CMakeFiles/opj_dump.dir/index.c.s

src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o.requires:
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o.requires

src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o.provides: src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o.requires
	$(MAKE) -f src/bin/jp2/CMakeFiles/opj_dump.dir/build.make src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o.provides.build
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o.provides

src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o.provides.build: src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o: src/bin/jp2/CMakeFiles/opj_dump.dir/flags.make
src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o: src/bin/common/color.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/CMakeFiles $(CMAKE_PROGRESS_4)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/opj_dump.dir/__/common/color.c.o   -c /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/common/color.c

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/opj_dump.dir/__/common/color.c.i"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -E /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/common/color.c > CMakeFiles/opj_dump.dir/__/common/color.c.i

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/opj_dump.dir/__/common/color.c.s"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -S /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/common/color.c -o CMakeFiles/opj_dump.dir/__/common/color.c.s

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o.requires:
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o.requires

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o.provides: src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o.requires
	$(MAKE) -f src/bin/jp2/CMakeFiles/opj_dump.dir/build.make src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o.provides.build
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o.provides

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o.provides.build: src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o: src/bin/jp2/CMakeFiles/opj_dump.dir/flags.make
src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o: src/bin/common/opj_getopt.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/CMakeFiles $(CMAKE_PROGRESS_5)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o   -c /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/common/opj_getopt.c

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.i"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -E /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/common/opj_getopt.c > CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.i

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.s"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && /usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -S /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/common/opj_getopt.c -o CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.s

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o.requires:
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o.requires

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o.provides: src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o.requires
	$(MAKE) -f src/bin/jp2/CMakeFiles/opj_dump.dir/build.make src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o.provides.build
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o.provides

src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o.provides.build: src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o

# Object files for target opj_dump
opj_dump_OBJECTS = \
"CMakeFiles/opj_dump.dir/opj_dump.c.o" \
"CMakeFiles/opj_dump.dir/convert.c.o" \
"CMakeFiles/opj_dump.dir/index.c.o" \
"CMakeFiles/opj_dump.dir/__/common/color.c.o" \
"CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o"

# External object files for target opj_dump
opj_dump_EXTERNAL_OBJECTS =

bin/opj_dump: src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o
bin/opj_dump: src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o
bin/opj_dump: src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o
bin/opj_dump: src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o
bin/opj_dump: src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o
bin/opj_dump: src/bin/jp2/CMakeFiles/opj_dump.dir/build.make
bin/opj_dump: bin/libopenjp2.so.2.0.1
bin/opj_dump: /usr/lib/x86_64-linux-gnu/libpng.so
bin/opj_dump: /usr/lib/x86_64-linux-gnu/libz.so
bin/opj_dump: /usr/lib/x86_64-linux-gnu/libtiff.so
bin/opj_dump: /usr/lib/x86_64-linux-gnu/libz.so
bin/opj_dump: /usr/lib/x86_64-linux-gnu/libtiff.so
bin/opj_dump: src/bin/jp2/CMakeFiles/opj_dump.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable ../../../bin/opj_dump"
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/opj_dump.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/bin/jp2/CMakeFiles/opj_dump.dir/build: bin/opj_dump
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/build

src/bin/jp2/CMakeFiles/opj_dump.dir/requires: src/bin/jp2/CMakeFiles/opj_dump.dir/opj_dump.c.o.requires
src/bin/jp2/CMakeFiles/opj_dump.dir/requires: src/bin/jp2/CMakeFiles/opj_dump.dir/convert.c.o.requires
src/bin/jp2/CMakeFiles/opj_dump.dir/requires: src/bin/jp2/CMakeFiles/opj_dump.dir/index.c.o.requires
src/bin/jp2/CMakeFiles/opj_dump.dir/requires: src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/color.c.o.requires
src/bin/jp2/CMakeFiles/opj_dump.dir/requires: src/bin/jp2/CMakeFiles/opj_dump.dir/__/common/opj_getopt.c.o.requires
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/requires

src/bin/jp2/CMakeFiles/opj_dump.dir/clean:
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 && $(CMAKE_COMMAND) -P CMakeFiles/opj_dump.dir/cmake_clean.cmake
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/clean

src/bin/jp2/CMakeFiles/opj_dump.dir/depend:
	cd /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1 /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1 /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2 /home/ken/Desktop/ia-1-2015/openjpeg-2.0.1/src/bin/jp2/CMakeFiles/opj_dump.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/bin/jp2/CMakeFiles/opj_dump.dir/depend

