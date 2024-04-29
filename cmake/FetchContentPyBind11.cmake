find_package(PythonInterp 3)
find_package(PythonLibs   3)

FetchContent_Declare( pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG master
    GIT_SHALLOW TRUE
    GIT_PROGRESS TRUE
    USES_TERMINAL_DOWNLOAD TRUE
)

FetchContent_GetProperties(pybind11)
if (NOT pybind11_POPULATED)
    message(STATUS "Fetching Pybind11 ${PYBIND11_VERSION}")
    FetchContent_Populate(pybind11)
    add_subdirectory(${pybind11_SOURCE_DIR} ${pybind11_BINARY_DIR} )
endif()