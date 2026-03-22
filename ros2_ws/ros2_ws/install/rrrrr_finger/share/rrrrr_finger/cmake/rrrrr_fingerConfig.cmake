# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_rrrrr_finger_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED rrrrr_finger_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(rrrrr_finger_FOUND FALSE)
  elseif(NOT rrrrr_finger_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(rrrrr_finger_FOUND FALSE)
  endif()
  return()
endif()
set(_rrrrr_finger_CONFIG_INCLUDED TRUE)

# output package information
if(NOT rrrrr_finger_FIND_QUIETLY)
  message(STATUS "Found rrrrr_finger: 0.0.0 (${rrrrr_finger_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'rrrrr_finger' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${rrrrr_finger_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(rrrrr_finger_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${rrrrr_finger_DIR}/${_extra}")
endforeach()
