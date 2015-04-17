from setuptools import find_packages
from setuptools import setup


major_version = '0.1'
minor_version = '0'
name = 'lca'

version = "%s.%s" % (major_version, minor_version)

if __name__ == "__main__":
    setup(
        name=name,
        version=version,
        description='Lowest common ancestor algorithm',
        classifiers=[
            'Development Status :: 1 - Beta',
            'Programming Language :: Python',
        ],
        author='Aleksey Kutepov',
        author_email='kutepoff@gmail.com',
        packages=find_packages(),
        zip_safe=False,
        entry_points={
            'console_scripts': [
                'lca=lca.main:main'
            ]
        }
    )
