from setuptools import find_packages, setup

package_name = 'my_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/my_first_launch.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xxx',
    maintainer_email='xxx@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher = my_first_package.simple_publisher:main', 
            'simple_subscriber = my_first_package.simple_subscriber:main'
        ],
    },
)
