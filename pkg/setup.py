from setuptools import find_packages, setup

package_name = 'pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shams-saied',
    maintainer_email='shams-saied@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "temp=pkg.temperature:main",
            "humid=pkg.humidity:main",
            "press=pkg.pressure:main",
            "agg=pkg.aggregator:main"
        ],
    },
)
