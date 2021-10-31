from setuptools import setup

setup(
    name='Numpy',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/kungurtzevKS/Numpy',
    author='Kungurtsev Konstantin',
    author_email='kungurtzev_ks@mail.ru',
    license='BSD 2-clause',
    packages=['Numpy'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Windows',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.7',
	'Programming Language :: Python :: 3.9',
    ],
)