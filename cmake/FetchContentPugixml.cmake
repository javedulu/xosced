FetchContent_Declare(Pugixml 
    GIT_REPOSITORY https://github.com/zeux/pugixml.git
    GIT_TAG master
    GIT_SHALLOW TRUE
    GIT_PROGRESS TRUE
    USES_TERMINAL_DOWNLOAD TRUE
    VERBOSE
)

if(NOT Pugixml_POPULATED)
        message(STATUS "Fetching PugiXml ${PUGIXML_VERSION}")
        #set(BUILD_SHARED_LIBS OFF CACHE BOOL "Disabled Build Shared libs")                                        
        FetchContent_Populate(Pugixml)
        FetchContent_GetProperties(Pugixml
                                        SOURCE_DIR Pugixml_SOURCE_DIR 
                                        BINARY_DIR Pugixml_BINARY_DIR
                                        POPULATED Pugixml_POPULATED
                                    )
        set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
        add_subdirectory(${Pugixml_SOURCE_DIR} ${Pugixml_BINARY_DIR} )
        add_library(Pugixml::Pugixml ALIAS pugixml)
endif()
