include_directories(
        ${IKFAST_PYBIND_EXTERNAL}
        ${IKFAST_PYBIND_SOURCE_DIR}
        ${IKFAST_INCLUDES}
)

add_subdirectory(kuka_kr6_r900)
add_subdirectory(abb_irb4600_40_255)
add_subdirectory(ur3)
add_subdirectory(ur5)
add_subdirectory(ur5e)
add_subdirectory(eth_rfl)
add_subdirectory(franka_panda)
add_subdirectory(kawasaki_rs010n)
add_subdirectory(kuka_iiwa)

# keep adding folders here...
# add_subdirectory(abb_4600_xxx)
