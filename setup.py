from setuptools import setup

requirements = [
    # TODO: put your package requirements here
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-faulthandler',
    'pytest-mock',
    'pytest-qt',
    'pytest-xvfb',
]

setup(
    name='cuencos',
    version='0.0.1',
    description="The Cuencos App",
    author="Tiago Coutinho",
    author_email='coutinhotiago@gmail.com',
    url='https://github.com/tiagocoutinho/cuencos',
    packages=['cuencos', 'cuencos.images',
              'cuencos.tests'],
    package_data={'cuencos.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'Cuencos=cuencos.Cuencos:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='cuencos',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
